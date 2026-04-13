number =  [32,13,33,24,23,53,23]
print(number[3], number[-4])

print(number[2:6])

# list (start : end : step)

print(number[1: 6:2])

print(number[6:1:-1])

print(number[2:])
print(number[:3])
print(number[:])
number.append(400)
number.sort()
if 38 in number:
    number.remove(33)
if 33 in number:
    number.pop()
print(number[::-1])



