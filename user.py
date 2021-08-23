import requests
#"https://scratch.mit.edu/discuss/topic/96414/?page=11#post-1624859"
#"https://scratchdb.lefty.one/v3/docs/"
class get_user:
  def __init__(self):
    pass
      
  def update(self,user):
    link ="https://scratchdb.lefty.one/v3/user/info/"
    status = requests.get(link+user)
    info = status.json()
    self.status_code = status
    if status.status_code == 200:
      self.username = info["username"]
      self.id = info["id"]
      self.sys_id = info["sys_id"]
      self.join_date = info["joined"]
      self.country = info["country"]
      self.AboutMe = info["bio"]
      self.WIWO = info["work"]
      self.status = info["status"]
      self.school = info["school"]
      self.country_rank = info["statistics"]["ranks"]["country"]
      del info["statistics"]["ranks"]["country"]
      self.rank = info["statistics"]["ranks"]
      del info["statistics"]["ranks"]
      self.stats = info["statistics"]