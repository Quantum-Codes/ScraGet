#MAKING GET_USER_EXTRA.GET_FOLLOWS! NOT TESTED

#from ScraGet import project, user, forum, studios, frontpage
from ScraGet import ScraGet
import time
user = ScraGet.get_user_extra()

for I in ("me","you","h","hajajsjska","?!"):
  user.check_user(I)
  print(user.username,
       user.valid,
       user.taken)
"""
user = ScraGet.get_user()
user.updateScratch(100)
print(user.updateScratch.__annotations__)
print(user.id)

project = ScraGet.get_cloud_data()
project.updateCloud("431041540")
print(len(project.cloud_data))
print("\n")
"""
"""
cloud = ScraGet.cloud()
#542800922
#https://scratch.mit.edu/projects/612229554/
@cloud.scan(ID="612229554",delay=1,NewThread=False)
def hello(change):
  print(change.user)
  cloud.stop = True

#print(cloud.thread.is_alive())
print("----------------------")
"""
"""
Frontpage = ScraGet.get_frontpage()
self = ScraGet.get_frontpage()
self.updateScratch()
print(self.updateScratch.__doc__)

print(self.top_remixed[1]["thumbnail_url"], self.response_time)
print(self.response_object)
#self.design_studio
#self.curated_projects
#self.featured_studios
#self.top_loved
#self.featured_projects

#from ScraGet import ScraGet #import package
studios = ScraGet.get_studio() #create object
studios.updateScratch(28380734) #update data
print(studios.host_id) #print required info from data*


data = ["hello"]

#from ScraGet import ScraGet
cloud = ScraGet.encoder()
print(cloud.encode(data))
print(cloud.decode("05"))


lol = ScraGet.get_studio()
lol.updateScratch(208695)
print(lol.title)

"""
"""
user = ScraGet.get_user_extra()
user.get_profile("griffpatch_tutor")
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

user.get_followers("Ankit_Anmol")
print(user.follower_count)
"""
"""
project = ScraGet.get_project()
project.updateScratch(476678019)
print(project.images,"\n",project.id)


forum = ScraGet.get_post()
forum.updateScratchDB(537944)
print(forum.id,forum.username,forum.updateScratchDB.__doc__)
"""