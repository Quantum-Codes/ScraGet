import requests
from ScraGet.Exceptions import ProjectNotFound

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

class get_project:
  def __init__(self):
    pass
  
  def updateScratchDB(self,ID : str) -> None:
    """
    Requests to ScratchDB API made by DatOneLefty for project data.

    Params: ID - Mandatory. Put the post ID in str format.
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

