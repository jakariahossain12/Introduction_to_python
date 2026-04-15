n = int(input())

a =list(map(int,input().split()))

b = a[::-1]    

if a==b:
    print("YES")
else:
    print("NO")