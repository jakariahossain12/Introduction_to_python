n = int(input())

m = [-1]*(n+2)




def febb(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    global m
    if m[num] != -1:
        return m[num]
    m[num] = febb(num-1) + febb(num-2)
    return m[num]

print(febb(n))