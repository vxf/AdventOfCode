from pprint import pprint

nodes = {}

with open("ch7input") as f :
  for l in f :
    l = l.strip()
    l, out = l.split(" -> ")
    
    l = l.split(" ")
    n = len(l)
    if n == 1 : # input
      if l[0].isdigit() :
        nodes[out] = ("IN",  int(l[0]) ,)
      else :
        nodes[out] = ("WIRE", l[0] ,)
        
    elif n == 2 and l[0] == "NOT": # not
      nodes[out] = ("NOT", l[1])
    elif n == 3 :
      a, gate, b = l[0], l[1], l[2]
      if a.isdigit(): a = int(a)
      if b.isdigit(): b = int(b)
      nodes[out] = (gate, a, b)
      
solved = {}
      
def solve(nid) :
  if not nid in nodes :
    return nid
    
  # print(nid)
  n = nodes[nid]
  if nid in solved :
    return solved[nid]
  
  # pprint(n)
  n0 = n[0]
  r = 0
  if n0 == "NOT" :
    r = ~ solve(n[1])
  elif n0 == "AND" :
    r = solve(n[1]) & solve(n[2])
  elif n0 == "OR" :
    r = solve(n[1]) | solve(n[2])
  elif n0 == "RSHIFT" :
    r = solve(n[1]) >> n[2]
  elif n0 == "LSHIFT" :
    r = solve(n[1]) << n[2]
  elif n0 == "IN" :
    r = n[1]
  elif n0 == "WIRE" :
    r = solve(n[1])
    
  solved[nid] = r
  return r

#pprint(nodes)

a = solve("a")
print(a)

nodes["b"] = ("IN",  a ,)
solved = {}
a = solve("a")
print(a)

#for key, value in nodes.items(): 
#  print("%s: %d", (key, solve(key)))
 

