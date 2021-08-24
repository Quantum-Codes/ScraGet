import requests

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

class get_studio:
  def __init__(self):
    pass
  
  def updateScratchDB(self,ID):
    info = requests.get(f"https://api.scratch.mit.edu/studios/{ID}",headers=headers)
    
    self.status_code = info.status_code
    
    if self.status_code == 200:
      info = info.json()