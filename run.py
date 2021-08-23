import project, user
user = user.get_user()
user.update("griffpatch")
print(user.stats,user.nat_rank,user.rank)

"""
project = project.get_project()
project.updateScratchDB(476678019)
print(project.stats,"\n",project.ranks)
"""