paper = 0
ribon = 0

with open("ch2input") as f :
  for l in f :
    l = [int(n) for n in l.strip().split("x")]
    l.sort()
    a,b,c = l

    paper += 3*a*b + 2*a*c + 2*b*c
    ribon += 2*a + 2*b + a*b*c
    
print(paper)
print(ribon)
