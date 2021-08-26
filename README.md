# ScraGet
ScraGet - A Scratch API package for Python<br>
This is a package that makes it easy to get data form:.<br>
1. Scratch -- Made by [Scratch developers](https://github.com/LLK/scratch-rest-api)
2. ScratchDB -- Made by [@DatOneLefty](https://Scratch.mit.edu/users/DatOneLefty)<br>

This package is used **without any password!**<br>
You don't need to Memorize any links!

## To install:<br>
`pip install ScraGet`<br>

WIP currently

## Docs:
documentation coming soon on wiki page

## Basic usage:
### Get user ID from scratch
```python
import ScraGet #import package
user = ScraGet.get_user() #create object
user.updateScratch("griffpatch") #update data
print(user.id) #print required info
```
### Get user ID from scratchDB
```python
import ScraGet #import package
user = ScraGet.get_user() #create object
user.updateScratchDB("griffpatch") #update data
print(user.id) #print required info
```
