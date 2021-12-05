from ScraGet.Exceptions import InvalidValue
import string

chars = list("•" + string.ascii_uppercase + string.digits + ".,!?/\|" + "'" + '"' + "()+-=:;[]^_%{}@#¦" + string.ascii_lowercase + " ~`*&$<>™®©")

class encoder:
  def encode(self,val : list) -> str:
    """
    Input a list to encode. Example: encode(["hello"])
    It can me a list of more than 1 item.
    Returns a number in str format.
    """
    encoded = ""
    x = [str(i) for i in val]
    
    for item in x:
      for letter in item:
        encoded = encoded + str(chars.index(letter)).zfill(2)
      encoded = encoded + "00"
    return encoded

  def decode(self,val : str) -> list:
    """
    Decode any numeric value in str format such as: :"12300300"
    Can decode any encoded value.
    The encoded value must be encoded through ScraGet's encoder only.
    """
    val = str(val)
    I = 0
    decoded = []
    if (len(val) % 2) == 1 or not val.isdigit():
      raise InvalidValue("The value to decode is invalid.")
    if val[-2:] != "00":
      val += "00"
    while I < len(val):
      temp = ""
      while val[I] + val[I+1] != "00":
        id = int(val[I] + val[I+1])
        temp = temp + chars[id]
        I += 2
      decoded.append(temp)
      I += 2
    return decoded