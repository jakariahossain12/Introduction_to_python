# def sum(num,num2):
#     print(num+num2)

# sum(4,4)


# def all_sum(*number):
#     print(number)
#     for num in number:
#         print(num)

# all_sum(34,34,234,234,45,)



def names(n,m,**adi):
    fun = f'{n} {m} {adi['title']}'
    print(fun)
    print(adi['title'])


names(n="jakaria",m="khan",title="hoooo")
