s = input()

a = []

s2 = ""

c = 0

for ch in s:
    s2+=ch
    if ch == "L":
        c+=1
    else:
        c-=1
    
    if c == 0:
        a.append(s2)
        s2 = ""


print(len(a))

for c in a:
    print(c)

