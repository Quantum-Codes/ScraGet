"""CONVERT TO CLASSES THEN ADD TO SCRAGET FOLDER. DELETE THIS FILE"""

import string
#new
chars = list("•" + string.ascii_uppercase + string.digits + ".,!?/\|" + "'" + '"' + "()+-=:;[]^_%{}@#¦" + string.ascii_lowercase + " ~`*&$<>™®©")

class encoder:
  def encode(self,val): #input list as: encode(["hello"])
    encoded = ""
    x = [str(i) for i in val] #googled ;-;
    
    for item in x:
      for letter in item:
        encoded = encoded + str(chars.index(letter)).zfill(2)
      encoded = encoded + "00"
    return encoded

  def decode(self,val):
    val = str(val)
    I = 0
    decoded = []
    while I < len(val):
      temp = ""
      while val[I] + val[I+1] != "00":
        id = int(val[I] + val[I+1])
        temp = temp + chars[id]
        I += 2
      decoded.append(temp)
      I += 2
    return decoded