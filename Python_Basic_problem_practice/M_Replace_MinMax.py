num = int(input())

numbers = list(map(int,input().split()))

ma = max(numbers)
mn = min(numbers)

in_ma = numbers.index(ma)
in_mn = numbers.index(mn)

numbers[in_ma],numbers[in_mn] = numbers[in_mn],numbers[in_ma]

print(*(numbers))