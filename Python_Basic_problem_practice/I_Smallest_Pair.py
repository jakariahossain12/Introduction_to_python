t = int(input())

lg = float('inf')
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    
    for i in range(n):
        for j in range(i+1,n):
            c = a[i]+a[j]+ j-i
            if lg > c:
                lg = c
    t-=1

print(lg)