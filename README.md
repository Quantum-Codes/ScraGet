# ScraGet
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) <br>
[![Downloads](https://static.pepy.tech/personalized-badge/scraget?period=total&units=none&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/scraget)
[![PyPI Latest Release](https://img.shields.io/pypi/v/ScraGet.svg)](https://pypi.org/project/ScraGet/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ScraGet.svg)](https://pypi.python.org/pypi/ScraGet/)

**No longer maintained.**

ScraGet - A Scratch API package for Python<br>
This is a package that makes it easy to get data form:<br>
1. Scratch -- Made by [Scratch developers](https://github.com/LLK/scratch-rest-api)<br>
2. ScratchDB -- Made by [@DatOneLefty](https://Scratch.mit.edu/users/DatOneLefty)<br>

<br>Code at: https://github.com/Quantum-Codes/ScraGet
<br>Pypi: https://pypi.python.org/pypi/ScraGet/

This package is used **without any passwords!**<br>
You don't need to Memorize any links!<br><br>
**Bonus features:**<br>
1. Cloud encoding/decoding with pre-made scratch script too!<br>
2. Cloud variable change event!

## To install:<br>
`pip install ScraGet`<br>

## Docs: https://github.com/Quantum-Codes/ScraGet/wiki
### Some example usages given in the docs!

# Basic usage:
### Get user ID from scratch
```python
from ScraGet import ScraGet #import package
user = ScraGet.get_user() #create object
user.updateScratch("griffpatch") #update data
print(user.id) #print required info
```
### Get user ID from scratchDB
```python
from ScraGet import ScraGet #import package
user = ScraGet.get_user() #create object
user.updateScratchDB("griffpatch") #update data
print(user.id) #print required info
```

# Advanced
### Scan cloud for any changes
```python
from ScraGet import ScraGet

Cloud = ScraGet.cloud()
@Cloud.scan(ID="612229554",delay=1,NewThread=False) #params explained in wiki
def hello(change): #change parameter is automatically passed.
  print(change.var)
  Cloud.stop = True #this stops the scanning. Don't put if u want to keep scanning
```

# Useful links
Code not working as intended or have any questions? [Ask here](.)!<br>
Any problems with the package or want to suggest a feature? Make an [issue](.)!
