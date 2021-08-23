import requests
#"https://scratch.mit.edu/discuss/topic/96414/?page=11#post-1624859"
#"https://scratchdb.lefty.one/v3/docs/"
class user_get:
  def __init__(self):
    pass
      
  def update(self,user):
    link ="https://scratchdb.lefty.one/v3/user/info/"
    status = requests.get(link+user)
    info = status.json()
    if status.status_code != 200:
      self.status = "error"
      return "Error"
    self.status = "good"
    self.username = info["username"]
    self.id = info["id"]
    self.sys_id = info["sys_id"]
    self.join_date = info["joined"]
    self.country = info["country"]
    self.bio = info["bio"]
    self.work = info["work"]
    self.status = info["status"]
    self.school = info["school"]
    self.stats = info["statistics"]
    self.rank = info["statistics"]["ranks"]["country"]
    self.nat_love_rank=info["statistics"]["ranks"]["country"]["loves"]
    self.nat_fav_rank = info["statistics"]["ranks"]["country"]["favorites"]
    self.nat_com_rank = info["statistics"]["ranks"]["country"]["comments"]
    self.nat_view_rank = info["statistics"]["ranks"]["country"]["views"]
    self.nat_follower_rank=info["statistics"]["ranks"]["country"]["followers"]
    self.nat_follow_rank=info["statistics"]["ranks"]["country"]["following"]
    self.love_rank = info["statistics"]["ranks"]["loves"]
    self.fav_rank = info["statistics"]["ranks"]["favorites"]
    self.com_rank = info["statistics"]["ranks"]["comments"]
    self.view_rank = info["statistics"]["ranks"]["views"]
    self.follower_rank = info["statistics"]["ranks"]["followers"]
    self.follow_rank = info["statistics"]["ranks"]["following"]
    self.love = info["statistics"]["loves"]
    self.fav = info["statistics"]["favorites"]
    self.com = info["statistics"]["comments"]
    self.view = info["statistics"]["views"]
    self.follower = info["statistics"]["followers"]
    self.follow = info["statistics"]["following"]
    return info

API = user_get()
API.update("Ankit_Anmol")
print(API.follower,API.follower_rank,API.nat_follower_rank,API.join_date[:-14])
print(API.update("Ankit_Anmol"))