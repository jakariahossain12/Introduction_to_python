n = int(input())

a = list(map(int,input().split()))

b = {}


for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i] = 1


c = 0

for i in b:

    if b[i] < i :
        c+=b[i]
    else:
        c+=(b[i] - i)

print(c)