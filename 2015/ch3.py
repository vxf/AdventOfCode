x, y = 0, 0

visited = set([(0,0)])

sx, sy = 0, 0
rx, ry = 0, 0

visitedsr = set([(0,0)])
vinc = {
  "<" : (-1,  0),
  ">" : ( 1,  0),
  "^" : ( 0, -1),
  "v" : ( 0,  1)
  }

with open("ch3input") as f :
  i = 0
  for c in f.read() :
    if not c in vinc : continue
    ix, iy = vinc[c]
    x, y = x + ix, y + iy
    visited.add((x, y))
    
    if i % 2 == 0 :
      sx, sy = sx + ix, sy + iy
      visitedsr.add((sx, sy))
    else :
      rx, ry = rx + ix, ry + iy
      visitedsr.add((rx, ry))

    i += 1

print(len(visited))
print(len(visitedsr))
