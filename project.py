import requests

class get_project:
  def __init__(self):
    pass
  
  def updateScratchDB(self,ID):
    info = requests.get(f"https://scratchdb.lefty.one/v3/project/info/{ID}")
    
    self.status = info.status_code
    
    if self.status == 200:
      info = info.json()
    
    def updateScratch(self, ID):
    info = requests.get(f"https://api.scratch.mit.edu/projects/{ID}")
    
    self.status = info.status_code
    
    if self.status == 200:
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
"""
a = get_project()
a.update(10128067)
print(a.status,"\n",a.id,"\n",a.title,"\n")
"""
"""
  a.description,"\n",
  a.instructions,"\n",
  a.visibility,"\n",
  a.public,"\n",
  a.commenting,"\n",
  a.published,"\n",
  a.author,"\n",
  a.thumbnail,"\n",
  a.images,"\n",
  a.created,"\n",
  a.last_modified,"\n",
  a.shared,"\n",
  a.stats,"\n",
  a.remix,"\n"
  )
"""