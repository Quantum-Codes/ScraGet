from scraget import project, user, forum

user = user.get_user_extra()
user.updateScratch("griffpatch")
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
project = project.get_project()
project.updateScratch(476678019)
print(project.images,"\n",project.id)
"""
"""
forum = forum.get_post()
forum.updateScratchDB(537944)
print(forum.id,forum.username)
"""