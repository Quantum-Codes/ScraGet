import requests

class get_project:
  def __init__(self):
    pass
  
  def updateScratchDB(self,ID):
    info = requests.get(f"https://scratchdb.lefty.one/v3/project/info/{ID}")
    
    self.status_code = info.status_code
    
    if self.status_code == 200:
      info = info.json()
      self.id = info["id"]
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
    
  def updateScratch(self, ID):
    info = requests.get(f"https://api.scratch.mit.edu/projects/{ID}")
    
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