fd = 0
p = 1
basement = 0
with open("ch1input") as f :
    for c in f.read() :
        if c == "(" :
            fd += 1
        elif c == ")" :
            fd -= 1
        if fd < 0  and basement == 0:
          basement = p
        p += 1

print(fd)
print(basement)
