from pprint import pprint

def escape(s):
  return "".join(["\\"+c if c in "\\\"" else c for c in s])

result = 0
result2 = 0
with open("ch8input") as f :
  for l in f :
    l = l.strip()
    result = result + len(l) - len(eval(l))
    result2 = result2 + len(escape(l)) + 2 - len(l)
    
print(result)
print(result2)
