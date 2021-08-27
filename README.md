# ScraGet
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![PyPI Latest Release](https://img.shields.io/pypi/v/ScraGet.svg)](https://pypi.org/project/ScraGet/)
[![Package Status](https://img.shields.io/pypi/status/ScraGet.svg)](https://pypi.org/project/ScraGet/)
[![Downloads](https://static.pepy.tech/personalized-badge/ScraGet?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/ScraGet)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ScraGet.svg)](https://pypi.python.org/pypi/ScraGet/)

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
user = ScraGet.user.get_user() #create object
user.updateScratch("griffpatch") #update data
print(user.id) #print required info
```
### Get user ID from scratchDB
```python
import ScraGet #import package
user = ScraGet.user.get_user() #create object
user.updateScratchDB("griffpatch") #update data
print(user.id) #print required info
```

Docs on the wiki page.
