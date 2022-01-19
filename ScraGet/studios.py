import requests
from typing import Union
from ScraGet.Exceptions import StudioNotFound

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

class get_studio:
  def __init__(self):
    pass
  
  def updateScratch(self,ID : Union[str,int]) -> None:
    """
    Requests to Scratch API for studio data.

    Params: ID - Mandatory. Put the studio ID in *str* or *int* format.
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
      raise StudioNotFound(f"Studio with id '{ID}' not found.")

class studio_extras:
  def __init__(self):
    pass
  def get_comments(self, ID: Union[int,str], count: int = 40) -> None:
    """
    Requests to Scratch API for studio comments.
    It makes multiple requests (gets 40 comments per request). Use it responsively. Don't try getting too many comments unless required.    
    Look at https://github.com/Quantum-Codes/ScraGet/wiki for more info.
    
    **Params:**\n
    `ID` - Mandatory. Put the studio ID in *str* format.\n
    `count` - Optional(default=40). Input how many comments you need in *int* format.
    """
    self.comments = []
    self.comments_response_objects = []
    if count > 0:
      req = int((count // -40))* -1
    else:
      raise ValueError(f"Values such as {count} is not allowed. Only natural numbers i.e. 1,2,3,4... allowed")
    for I in range(req):
      x = requests.get(f"https://api.scratch.mit.edu/studios/{ID}/comments/?offset={I*40}&limit=40")
      self.comments_response_objects.append(x)
      if x.status_code == 200:
        if count >= 40:
          self.comments += x.json()
        elif count < 40:
          self.comments += x.json()[:count]
        count -= 40
        if len(x.json()) < 40:
          break
      else:
        raise StudioNotFound(f"Studio with ID '{ID}' not found.")

  def get_projects(self, ID : Union[str,int], offset: Union[int,str] = 0) -> None:
    """
    Requests to Scratch API for list of projects of studio.
    Look at https://github.com/Quantum-Codes/ScraGet/wiki for more info.
    
    **Params**:\n
    `ID` - Mandatory. Put the studio ID in *str* or *int* format.\n
    `offset` - Optional(default=0). Offset the list of projects by this number. (*int* or *str* format).
    """
    self.projects_response_objects = []
    self.projects = []
    while True:
      x = requests.get(f"https://api.scratch.mit.edu/studios/{ID}/projects/?limit=40&offset={offset}")
      self.projects_response_objects.append(x)
      if x.status_code == 200:
        x = x.json()
        self.projects += x

        if len(x) != 40:
          self.project_count = len(self.projects)
          break
      else:
        raise StudioNotFound(f"Studio '{ID}' doesn't exist.")
      offset += 40
