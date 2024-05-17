import random
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

r1 = random.randrange(1, 8)
r2 = random.randrange(1,8)
r3 = random.randrange(1,8)

l1 = letters[random.randrange(len(letters)-1)]
l2 = letters[random.randrange(len(letters)-1)]
l3 = letters[random.randrange(len(letters)-1)]

for i in range(len(letters)):
    s = random.randrange(len(letters)-1)
    temp = letters[i]
    letters[i] = letters[s]
    letters[s] = temp
strstr = ""
for i in letters:
    strstr+=i
print(str(r1)+str(r2)+str(r3)+" "+l1+l2+l3+" "+strstr)
    