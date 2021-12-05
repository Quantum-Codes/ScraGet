import requests
from ScraGet.Exceptions import StudioNotFound

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

class get_studio:
  def __init__(self):
    pass
  
  def updateScratch(self,ID : str) -> None:
    """
    Requests to Scratch API for studio data.

    Params: ID - Mandatory. Put the studio ID in str format.
    """

    info = requests.get(f"https://api.scratch.mit.edu/studios/{ID}",headers=headers)
    self.response_object = info
    self.response_time = info.elapsed.total_seconds()
    self.status_code = info.status_code
    
    if self.status_code == 200:
      info = info.json()
      self.id = info["id"]
      self.title = info["title"]
      self.host_id = info["host"]
      self.description = info["description"]
      self.visibility = info["visibility"]
      self.public = info["public"]
      self.open = info["open_to_all"]
      self.com_allow = info["comments_allowed"]
      self.image = info["image"]
      self.created = info["history"]["created"]
      self.modified = info["history"]["modified"]
      self.history = info["history"]
      self.stats = info["stats"]
    
    elif self.status_code == 404:
      raise StudioNotFound(f"Studio with id '{str(ID)}' not found.")