import re
from pprint import pprint


rx_reindeer = re.compile(r"(?P<name>\w*) can fly (?P<speed>\d*) km/s for (?P<time>\d*) seconds, but then must rest for (?P<rest>\d*) seconds.")



def readInput(filename) :
  reindeers = []
  
  with open(filename) as f :
    for l in f :
      l = l.strip()
      m = rx_reindeer.match(l)
      
      name, speed, time, rest = m.group("name"), m.group("speed"), m.group("time"), m.group("rest")
      
      reindeers.append( (name, int(speed), int(time), int(rest)) )
      
  return reindeers


def calcDistance(r, t) :
  name, speed, time, rest = r
  
  dd = time * speed
  dt = time + rest
  
  n = t // dt
  finish = t % dt
  finish = finish if finish < time else time
  
  distance = ( n * dd ) + ( finish * speed )
  
  return (name, distance)

def calcPoints(reindeers, time):
  scores = {}
  for name,_,_,_ in reindeers :
    scores[name] = 0

  for t in range(1, time + 1) :
    distances = [calcDistance(r, t) for r in reindeers]
    _, dwin = max(distances, key = lambda d: d[1])
    for n, d in distances :
      if dwin == d :
        scores[n] = scores[n] + 1
    
  return scores

def ch14(filename, time):
  reindeers = readInput(filename)
  distances = [calcDistance(r, time) for r in reindeers]
  return max(distances, key = lambda d: d[1])
  
def ch14b(filename, time):
  reindeers = readInput(filename)
  return calcPoints(reindeers, time)

print(ch14("ch14input", 2503))
print(ch14b("ch14input", 2503))

