import json

def trav(j) :
  if type(j) is dict :
    values = [v for _, v in j.items()]

    if "red" in values :
      return 0
      
    return sum([trav(v) for v in values])

  elif type(j) is list :
    return sum([trav(v) for v in j])
    
  elif type(j) is str :
    return 0
    
  else :
    return j

with open("ch12input") as f :
  j = json.load(f)
  
  print(trav(j))
  
