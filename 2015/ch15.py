from pprint import pprint


def readInput(filename) :
  ingredients = []
  
  with open(filename) as f :
    for l in f :
      l = l.strip()
      
      ingredient, properties = l.split(": ")
      
      properties = [p.split(" ") for p in properties.split(", ")]
      properties = [(p, int(s)) for p, s in properties]
      
      ingredients.append( (ingredient, properties) )
      
  pprint(ingredients)
  
  
readInput("ch15input2")
