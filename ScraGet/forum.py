import requests
from ScraGet.Exceptions import PostNotFound, TopicNotFound

class get_post:
  def __init__(self):
    pass
  
  def updateScratchDB(self,ID : str) -> None:
    """
    Requests to ScratchDB API made by DatOneLefty for post data.

    Params: ID - Mandatory. Put the post ID in str format.
    """
    info = requests.get(f"https://scratchdb.lefty.one/v3/forum/post/info/{ID}")
    self.response_object = info
    self.response_time = info.elapsed.total_seconds()
    self.status_code = info.status_code
    
    if self.status_code == 200:
      info = info.json()
      self.id = info["id"]
      self.username = info["username"]
      self.deleted = info["deleted"]
      self.editor = info["editor"]
      self.posted = info["time"]["posted"]
      self.last_edited = info["time"]["edited"]
      self.contentHTML = info["content"]["html"]
      self.contentBB = info["content"]["bb"]
      self.topic_id = info["topic"]["id"]
      topic = get_topic()
      topic.updateScratchDB(self.topic_id)
      if topic.status_code == 200:
        self.title = topic.title
        self.category = topic.category
        self.closed = topic.closed
        self.deleted = topic.deleted
        self.topic_posts = topic.post_count
      else:
        self.title = info["topic"]["title"]
        self.category = info["topic"]["category"]
        self.closed = info["topic"]["closed"]
        self.deleted = info["topic"]["deleted"]
    
    elif self.status_code == 404:
      raise PostNotFound(f"Post with id '{str(ID)}' not found.")

class get_topic:
  def __init__(self):
    pass
  
  def updateScratchDB(self,ID : str) -> None:
    """
    Requests to ScratchDB API made by DatOneLefty for topic data.

    Params: ID - Mandatory. Put the topic ID in str or int format.
    """

    info = requests.get(f"https://scratchdb.lefty.one/v3/forum/topic/info/{ID}")
    self.response_object = info
    self.response_time = info.elapsed.total_seconds()
    self.status_code = info.status_code
    
    if self.status_code == 200:
      info = info.json()
      self.id = info["id"]
      self.title = info["title"]
      self.category = info["category"]
      self.closed = info["closed"]
      self.deleted = info["deleted"]
      self.post_count = info["post_count"]
    
    elif self.status_code == 404:
      raise TopicNotFound(f"Topic with id '{str(ID)}' not found.")