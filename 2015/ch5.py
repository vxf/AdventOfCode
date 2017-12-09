forbid = [(w, v) for w, v in ["ab", "cd", "pq", "xy"]]

def isnice(s):
  vowels = len([c for c in s if c in 'aeiou'])
  if vowels < 3 :
    return False
    
  nice = False
  for w, v in zip(s, s[1:]) :
    if (w, v) in forbid :
      return False
      
    if w == v : 
      nice = True
      
  return nice
  
def isnice2(s):
  nice1 = False
  nice2 = False
  pairs = []
  for w, v in zip(s, s[1:]) :
    p = w + v
    if p in pairs :
      nice1 = True
      break
    else :
      pairs.append(p)
      
  for a, b, c in zip(s, s[1:], s[2:]) :
    if a == c :
      if a != b :
        nice2 = True
      else :
        nice1 = False
        break
      
  return nice1 and nice2
    
nicewords = 0
nicewords2 = 0
with open("ch5input") as f :
  for l in f :
    l = l.strip()
    if isnice(l) :
      nicewords += 1
    if isnice2(l) :
      nicewords2 += 1
    
    
print(nicewords)    
print(nicewords2)
