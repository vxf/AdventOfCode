from pprint import pprint

nodes = []
distances = {}

with open("ch9input") as f :
  for l in f :
    l = l.strip()
    a, _, b, _, d  = l.split(" ")
    d = int(d)
    
    distances[(a, b)] = d
    distances[(b, a)] = d
    if not a in nodes : nodes.append(a)
    if not b in nodes : nodes.append(b)
    
def tsp(n1, visited, distance) :
  next = [n for n in nodes if not n in visited]
  
  if not next :
    return distance
  
  dnext = []
  for n2 in next :
    p = (n1, n2)
    d = tsp(n2, visited + [n2], distances[p] + distance)
    dnext.append(d)
    
  # pprint(dnext)
  return max(dnext)
  # return min(dnext)
  
n = nodes[0]
v = [n]
maxroute = max([tsp(n, [n], 0) for n in nodes])
print(maxroute)
