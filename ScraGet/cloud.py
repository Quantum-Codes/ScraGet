import requests, time, json
from ScraGet.Exceptions import ProjectNotFound, InvalidValue
from threading import Thread

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

class get_cloud_data:
  def __init__(self):
    pass
  
  def updateCloud(self, ID : str, limit : str= "10", offset : str="0") -> None:
    """
    Requests to Scratch API for clouddata.

    Params:
      ID - Mandatory. Put the project ID in str format.
      limit - Optional (Default:10) Specify number of logs to be returned in str format. Specify: "all" to return all log items.
      offset - Optional (Default:0) Specify the offset for each log item in str format.
  """
    if limit.lower() == "all":
      limit = "0"
    info = requests.get(f"https://clouddata.scratch.mit.edu/logs?projectid={ID}&limit={limit}&offset={offset}")
    self.response_object = info
    self.response_time = info.elapsed.total_seconds()
    self.status_code = info.status_code
    
    if self.status_code == 200:
      info = info.json()
      self.cloud_data = info


class cloud:
  def __init__(self):
    self.stop = False
  
  def scan(self, ID: str, delay: float = 1.0, NewThread: bool = True) -> None:
    """
    Scans clouddata continuously every few seconds (duration to be defined by you while making the cloud class) for any changes.

    Params:
      ID - Mandatory. Put project ID in str format.
      delay - Optional(default=1.0). Put the time delay between 2 scan updates in float format. Minimum: 0.1 secs
      NewThread - Optional(default=True). Specify Ture if you need to run in a separate thread, specify False if you need to run in main thread. (bool format)
    """

      
    def inner_dec(func):
      y = requests.get(f"https://clouddata.scratch.mit.edu/logs?projectid={ID}&limit=10000&offset=0", headers=headers)
      
      if y.status_code == 200:
        y = y.json()
        y = [json.dumps(item) for item in y]
        while True:
          time.sleep(delay)
          if self.stop:
            if NewThread:
              exit(0)
            break
          x = requests.get(f"https://clouddata.scratch.mit.edu/logs?projectid={ID}&limit=10000&offset=0", headers=headers)
          if x.status_code != 200: #can get 504
            continue
          x = x.json()

          x = [json.dumps(item) for item in x]
          if x != y:
            z = list(set(x) - set(y))
            z = [json.loads(item) for item in z]
            y = x
            self.change_log = z
            self.recent = z[0]
            self.user = z[0]["user"]
            self.type = z[0]["verb"]
            self.var = z[0]["name"]
            self.value = z[0]["value"]
            self.time = z[0]["timestamp"]
            func(self)

      else:
        raise ProjectNotFound(f"Project with ID {ID} returned a status codes of: {y.status_code}")

    def threaded_dec(func):
      scan_thread = Thread(target=inner_dec, args=(func,))
      scan_thread.setDaemon(True)
      scan_thread.start()
      self.thread = scan_thread

    if delay < 0.2:
      raise InvalidValue("Delay is less than 0.2. Try making the delay more than 0.2")
    else:
      if NewThread:
        return threaded_dec
      return inner_dec
