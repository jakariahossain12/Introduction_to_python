number = [32,3,2,53,32,53,23,5,3]

setnumber = set(number)

print(setnumber)

setnumber.add(44)

print(setnumber)

if 3 in setnumber:
    print("yes")


for i in setnumber:
    print(i)

a = {1,2,3}
b = {1,2,3,4,5,6,}
print(a & b)
print(a | b)