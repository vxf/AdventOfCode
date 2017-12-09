import re
from pprint import pprint
import itertools

nodes = set()
relations = {}

rx_relation = re.compile(r"(?P<name1>\w*) would (?P<sign>(?:gain)|(?:lose)) (?P<points>\d*) happiness units by sitting next to (?P<name2>\w*)\.")

with open("ch13input") as f :
  for l in f :
    l = l.strip()
    m = rx_relation.match(l)
    
    name1, name2, sign, points = m.group("name1"), m.group("name2"), m.group("sign"), m.group("points")
    
    points = int(points)
    points = points if sign == "gain" else -points
    
    relations[(name1, name2)] = points
    # relations[(name2, name1)] = points
    
    nodes.add(name1)
    nodes.add(name2)

# part two
for n in nodes :
  relations[("me", n)] = 0
  relations[(n, "me")] = 0
  
nodes.add("me")
    
pprint(relations)
# pprint(nodes)

nodes = list(nodes)
n = len(nodes)
permutations = [p for p in itertools.permutations(nodes)]

# pprint(permutations)

def getScore(p) :
  # print(p)
  s = 0
  p = p + (p[0],)
  for n1, n2 in zip(p, p[1:]) :
    s = s +  relations[(n1, n2)] + relations[(n2, n1)]
    
  return s
  
# scores = [getScore(p) for p in permutations]
# print(scores)
    
best = max([getScore(p) for p in permutations])
print(best)
