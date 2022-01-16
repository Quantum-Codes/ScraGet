import requests
from typing import Union
from ScraGet.Exceptions import UserNotFound
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
#"https://scratch.mit.edu/discuss/topic/96414/?page=11#post-1624859"
#"https://scratchdb.lefty.one/v3/docs/"
class get_user:
  def __init__(self):
    pass
  
  def updateScratchDB(self,user : str) -> None:
    """
    Requests to ScratchDB API made by DatOneLefty for user data.
    Look at https://github.com/Quantum-Codes/ScraGet/wiki for more info.
   P arams: user - Mandatory. Put the username in str format.
    """

    info = requests.get(f"https://scratchdb.lefty.one/v3/user/info/{user}")
    self.response_object = info
    self.response_time = info.elapsed.total_seconds()
    self.status_code = info.status_code
    if self.status_code == 200:
      info = info.json()
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
    
    elif self.status_code == 404:
      raise UserNotFound("User '{user}' not found.")

  def updateScratch(self, user: str) -> None:
    """
    Requests to Scratch API for user data .
    Look at https://github.com/Quantum-Codes/ScraGet/wiki for more info.    
    Params: user - Mandatory. Put the username in str format.
    """

    info = requests.get(f"https://api.scratch.mit.edu/users/{user}",headers = headers)
    self.response_object = info
    self.response_time = info.elapsed.total_seconds()
    self.status_code = info.status_code
    if self.status_code == 200:
      info = info.json()
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
    
    elif self.status_code == 404:
      raise UserNotFound(f"User '{user}' not found.")

class get_user_extra:
  def __init__(self):
    pass
  
  def get_message_count(self, user : str) -> None:
    """
    Requests to Scratch API for message count.
    Look at https://github.com/Quantum-Codes/ScraGet/wiki for more info.
    
    Params: user - Mandatory. Put the username in str format.
    """

    
    info = requests.get(f"https://api.scratch.mit.edu/users/{user}/messages/count",headers=headers)
    self.messages_response_object = info
    self.messages_response_time = info.elapsed.total_seconds()
    self.messages_status_code = info.status_code
    
    if self.messages_status_code == 200:
      info = info.json()
      self.messages = info["count"]
      
    elif self.messages_status_code == 404:
      raise UserNotFound(f"User '{user}' not found.")

  def get_profile(self, user : str) -> None:
    """
    Requests to Scratch API for profile extra info.
    Look at https://github.com/Quantum-Codes/ScraGet/wiki for more info.
    
    Params: user - Mandatory. Put the username in str format.
    """

    info = requests.get(f"https://scratch.mit.edu/site-api/users/all/{user}",headers=headers)
    self.profile_response_object = info
    self.profile_status_code = info.status_code
    self.profile_response_time = info.elapsed.total_seconds()
    
    if self.profile_status_code == 200:
      info = info.json()
      self.label_name = info["featured_project_label_name"]
      self.featured_project_data = info["featured_project_data"]
      self.featured_project_id = info["featured_project"]
      self.creator_id = info["user"]["pk"]
      self.user = info["user"]["username"]
      
      if self.featured_project_data != None:
        self.creator = self.featured_project_data["creator"]
        self.change_time = self.featured_project_data["datetime_modified"]
        self.title = self.featured_project_data["title"]
        self.featured_project_label_id = info["featured_project_label_id"]
        self.thumbnail = f"https://cdn2.scratch.mit.edu/get_image/project/{self.featured_project_id}_480x360.png"
      else:
        self.creator = None
        self.change_time = None
        self.featured_project_label_id = None
        self.title = None
        self.thumbnail = None
  
      self.pfp = f"https://cdn2.scratch.mit.edu/get_image/user/{self.creator_id}_90x90.png?v="
      self.id = info["id"] #WAT IS THIS

  def get_followers(self, user : str, offset : int = 0) -> None:
    """
    Requests to Scratch API for followers
    Look at https://github.com/Quantum-Codes/ScraGet/wiki for more info.
    
    Params: 
    user - Mandatory. Put the username in str format.
    offset - Optional(default=0). Offset the list of followers by this number. (int format)
    
    """
    responses = []
    followers = []
    print("start")
    while True:
      x = requests.get(f"https://api.scratch.mit.edu/users/{user}/followers/?limit=40&offset={offset}")
      responses.append(x)
      x = x.json()
      offset += 40
      print(len(followers))
      for I in x:
        followers.append(I["username"])

      if len(x) != 40:
        self.followers_response_object = responses
        self.followers = followers
        self.follower_count = len(followers)
        break

  def check_user(self, user : str) -> None:
    """
    Requests to Scratch API for whether the username exists or not. It can also be used to check if username is valid or not!!
    
    Look at https://github.com/Quantum-Codes/ScraGet/wiki for more info.
    
    Params: user - Mandatory. Put the username in str format.
    """
    info = requests.get(f"https://scratch.mit.edu/accounts/check_username/{user}/")
    self.user_response_object = info
    self.user_response_time = info.elapsed.total_seconds()
    self.user_status_code = info.status_code
    
    if self.user_status_code == 200:
      info = info.json()[0]
      self.username = info["username"]
      if "exists" in info["msg"]:
        self.valid = True
        self.taken = True
      elif "invalid" in info["msg"]:
        self.valid = False
        self.taken = False
      else:
        self.valid = True
        self.taken = False
        
    elif self.user_status_code == 404:
      self.username = user
      self.valid = False
      self.taken = False
