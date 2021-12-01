import requests
from ScraGet.Exceptions import PageNotFound

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}

class get_frontpage:
  def __init__(self):
    pass
  
  def updateScratch(self):
    """
    Requests to Scratch API for frontpage data.
    """

    info = requests.get(f"https://api.scratch.mit.edu/proxy/featured",headers=headers)
    self.response_object = info
    self.response_time = info.elapsed.total_seconds()
    self.status_code = info.status_code
    
    if self.status_code == 200:
      info = info.json()
      self.new_projects = info["community_newest_projects"]
      self.top_remixed = info["community_most_remixed_projects"]
      self.design_studio = info["scratch_design_studio"]
      self.curated_projects = info["curator_top_projects"]
      self.featured_studios = info["community_featured_studios"]
      self.top_loved = info["community_most_loved_projects"]
      self.featured_projects = info["community_featured_projects"]
      
    elif self.status_code == 404:
      raise PageNotFound("There was a 404 error in API...")