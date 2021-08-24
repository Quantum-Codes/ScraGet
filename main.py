import project, user, forum
"""
user = user.get_user()
user.updateScratchDB("griffpatch")
print(user.pfp,user.id)
"""

project = project.get_project()
project.updateScratch(476678019)
print(project.images,"\n",project.id)
"""
forum = forum.get_post()
forum.updateScratchDB(537944)
print(forum.id,forum.username)
"""