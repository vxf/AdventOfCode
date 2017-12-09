lights = [[False for n in range(1000)] for n in range(1000)]
dimlights = [[0 for n in range(1000)] for n in range(1000)]

def parseCoord(s): return [int(n) for n in s.split(",")]

with open("ch6input") as f :
  for l in f :
    l = l.strip().split(" ")
    if l[0] == "toggle" :
      sX, sY = parseCoord(l[1])
      eX, eY = parseCoord(l[3])
      for y in range(sY, eY + 1) :
        for x in range(sX, eX + 1) :
          # print("%d,%d %d" % (x, y, not lights[y][x]))
          lights[y][x] = not lights[y][x]
          
          dimlights[y][x] = dimlights[y][x] + 2

    elif l[0] == "turn" :
      t = False if l[1] == "off" else True
      sX, sY = parseCoord(l[2])
      eX, eY = parseCoord(l[4])
      for y in range(sY, eY + 1) :
        for x in range(sX, eX + 1) :
          # print("%d,%d" % (x, y))
          lights[y][x] = t
          
          d = dimlights[y][x]
          dimlights[y][x] = d + 1 if t else d - 1 if d > 1 else 0

print(sum(sum(lights, [])))
print(sum(sum(dimlights, [])))
