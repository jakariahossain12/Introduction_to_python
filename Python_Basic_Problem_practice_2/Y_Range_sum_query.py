a,b = map(int ,input().split())

arr = list(map(int,input().split()))

arr2 = [0] *(a+1)



for i in range(a):
    arr2[i+1] = arr2[i] + arr[i]


for _ in range(b):
    l,r = map(int,input().split())
    print(arr2[r] - arr2[l-1])