import requests
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
#"https://scratch.mit.edu/discuss/topic/96414/?page=11#post-1624859"
#"https://scratchdb.lefty.one/v3/docs/"
class get_user:
  def __init__(self):
    pass
  
  def updateScratchDB(self,user):
    info = requests.get(f"https://scratchdb.lefty.one/v3/user/info/{user}")
    self.status_code = info.status_code
    info = info.json()
    if self.status_code == 200:
      self.username = info["username"]
      self.id = info["id"]
      self.pfp = f"https://cdn2.scratch.mit.edu/get_image/user/{self.id}_90x90.png?v="
      self.sys_id = info["sys_id"]
      self.join_date = info["joined"]
      self.country = info["country"]
      self.AboutMe = info["bio"]
      self.wiwo = info["work"]
      self.status = info["status"]
      self.school = info["school"]
      self.country_rank = info["statistics"]["ranks"]["country"]
      del info["statistics"]["ranks"]["country"]
      self.rank = info["statistics"]["ranks"]
      del info["statistics"]["ranks"]
      self.stats = info["statistics"]
      
  def updateScratch(self,user):
    info = requests.get(f"https://api.scratch.mit.edu/users/{user}",headers = headers)
    self.status_code = info.status_code
    info = info.json()
    if self.status_code == 200:
      self.username = info["username"]
      self.id = info["id"]
      self.join_date = info["history"]["joined"]
      self.scratchteam = info["scratchteam"]
      self.profile_stats = info["profile"]
      self.profile_id = info["profile"]["id"]
      self.pfp = info["profile"]["images"]["90x90"]
      self.country = info["profile"]["country"]
      self.AboutMe = info["profile"]["bio"]
      self.wiwo = info["profile"]["status"]

class get_user_extra:
  def __init__(self):
    pass
  
  def updateScratch(self,user):
    
    info = requests.get(f"https://api.scratch.mit.edu/users/{user}/messages/count",headers=headers)    
    self.status_code = info.messages_status_code
    if self.status_code == 200:
      info = info.json()
      self.messages = info["count"]

    info = requests.get(f"https://scratch.mit.edu/site-api/users/all/{user}",headers=headers)    
    self.status_code = info.profile_status_code
    if self.status_code == 200:
      info = info.json()
      self.label_name = info["featured_project_label_name"]
      self.featured_project_data = info["featured_project_data"] #need to extract further 