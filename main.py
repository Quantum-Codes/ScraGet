#from ScraGet import project, user, forum, studios, frontpage
from ScraGet import ScraGet
Frontpage = ScraGet.get_frontpage()
self = ScraGet.get_frontpage()
self.updateScratch()

print(self.top_remixed[1]["thumbnail_url"], self.response_time)
#self.design_studio
#self.curated_projects
#self.featured_studios
#self.top_loved
#self.featured_projects
"""
lol = studios.get_studio()
lol.updateScratchDB(208695)
print(lol.title)
"""
"""
user = user.get_user_extra()
user.updateScratch("griffpatch_tutor")
print(user.label_name,user.profile_status_code,"\n",
      user.featured_project_data,
      user.featured_project_id,
      user.featured_project_label_id,
      user.creator,
      user.creator_id,
      user.change_time,
      user.title,
      user.thumbnail,
      user.pfp,
      user.id)
"""
"""
project = project.get_project()
project.updateScratch(476678019)
print(project.images,"\n",project.id)
"""
"""
forum = forum.get_post()
forum.updateScratchDB(537944)
print(forum.id,forum.username)
"""