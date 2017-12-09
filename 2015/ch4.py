import hashlib

key = b"yzbqklnj"
# key = b"abcdef"

ans = 0

for n in range(70000000) :
  h = hashlib.md5(key + str.encode(str(n))).hexdigest()
  if h[:6] == "000000" :
    ans = n
    break
    
print(str(ans))
