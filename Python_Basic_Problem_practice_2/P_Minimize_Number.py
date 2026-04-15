n = int(input())

a = list(map(int,input().split()))

c = 0

while True:
    isT = False
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = a[i]/2
        else:
            isT = True
            break
            
    if isT == True:
        break
    c+=1


print(c)
