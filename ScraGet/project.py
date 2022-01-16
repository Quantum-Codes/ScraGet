import requests
from typing import Union
from ScraGet.Exceptions import ProjectNotFound, UserNotFound

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

class get_project:
  def __init__(self):
    pass
  
  def updateScratchDB(self,ID : str) -> None:
    """
    Requests to ScratchDB API made by DatOneLefty for project data.

    Params: ID - Mandatory. Put the project ID in str format.
    """

    info = requests.get(f"https://scratchdb.lefty.one/v3/project/info/{ID}")
    self.response_object = info
    self.response_time = info.elapsed.total_seconds()
    self.status_code = info.status_code
    
    if self.status_code == 200:
      info = info.json()
      self.id = info["id"]
      self.thumbnail = f"https://cdn2.scratch.mit.edu/get_image/project/{self.id}_480x360.png"
      self.title  = info["title"]
      self.description = info["description"]
      self.instructions = info["instructions"]
      #self.visibility = info["visibility"]
      self.public = info["public"]
      self.commenting = info["comments_allowed"]
      #self.published = info["is_published"]
      self.author = info["username"]
      #self.thumbnail = info["image"]
      #self.images = info["images"]
      self.created = info["times"]["created"]
      self.last_modified = info["times"]["modified"]
      self.shared = info["times"]["shared"]
      self.ranks = info["statistics"]["ranks"]
      del info["statistics"]["ranks"]
      self.stats = info["statistics"]
      self.remix = info["remix"]
      self.metadata = info["metadata"]
    
    elif self.status_code == 404:
      raise ProjectNotFound(f"Project with id '{str(ID)}' not found.")
    
  def updateScratch(self, ID : str) -> None:
    """
    Requests to Scratch API for project data.

    Params: ID - Mandatory. Put the project ID in str format.
    """

    info = requests.get(f"https://api.scratch.mit.edu/projects/{ID}",headers=headers)
    self.response_object = info
    self.response_time = info.elapsed.total_seconds()
    self.status_code = info.status_code
    
    if self.status_code == 200:
      info = info.json()
      self.id = info["id"]
      self.title  = info["title"]
      self.description = info["description"]
      self.instructions = info["instructions"]
      self.visibility = info["visibility"]
      self.public = info["public"]
      self.commenting = info["comments_allowed"]
      self.published = info["is_published"]
      self.author = info["author"]
      self.thumbnail = info["image"]
      self.images = info["images"]
      self.created = info["history"]["created"]
      self.last_modified = info["history"]["modified"]
      self.shared = info["history"]["shared"]
      self.stats = info["stats"]
      self.remix = info["remix"]
    
    elif self.status_code == 404:
      raise ProjectNotFound(f"Project with id '{str(ID)}' not found.")


class project_comments:
  def __init__(self):
    pass
  def get_comments(self, ID: Union[int,str],author: str = "" , count: int = 40) -> None:
    """
    Requests to Scratch API for user profile comments.
    It makes multiple requests (gets 40 comments per request). Use it responsively. Don't try getting too many comments unless required.    
    Look at https://github.com/Quantum-Codes/ScraGet/wiki for more info.
    
    **Params:**\n
    `ID` - Mandatory. Put the project ID in *str* format.\n
    `author` - Optional(default=""). You may input the creator of the project in *str* if you know to reduce 1 request. If you don't put, the package will make an additional request to API for the creator. **Do not request to API yourself as package already does that.**\n
    `count` - Optional(default=40). Input how many comments you need in *int* format
    """
    if author == "":
      self.author  = requests.get(f"https://api.scratch.mit.edu/projects/{ID}")
      self.author_status_code = self.author.status_code
      if self.author_status_code == 200:
        self.author = self.author.json()["author"]["username"]
      else:
        raise ProjectNotFound(f"Project with ID {ID} does not exist.")
    else:
      self.author = author
    self.comments = []
    self.response_objects = []
    if count > 0:
      req = int((count // -40))* -1
    else:
      raise IndexError(f"Values such as {count} is not allowed. Only natural numbers i.e. 1,2,3,4... allowed")
    for I in range(req):
      x = requests.get(f"https://api.scratch.mit.edu/users/{self.author}/projects/{ID}/comments/?offset={I*40}&limit=40")
      self.response_objects.append(x)
      if x.status_code == 200:
        if count >= 40:
          self.comments += x.json()
        elif count < 40:
          self.comments += x.json()[:count]
        count -= 40
        if len(x.json()) < 40:
          break
      else:
        if author:
          raise UserNotFound(f"User {self.author} does not own project with ID {ID}.")
