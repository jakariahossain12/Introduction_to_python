person = {'name':'jakria','address':'kuwait','age':23,'job':'bekar'}

print(person)
print(person['job'])
print(person.keys())
print(person.values())
del person['age']
print(person)

for key,value in person.items():
    print(key,value)