from food_item import FoodItem
from menu import Menu
from order import Order
from restaurent import Restaurent
from users import Customer, Admin, Employee

res = Restaurent('mamar res')



def customer_menu():
    name = input("Enter your Name : ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")
    customer = Customer(name,phone,email,address)

    

    while True:
        print(f"Welcom {customer.name}!!!")
        print("1. view Menu")
        print("2. Add item to cart")
        print("3. view cart")
        print("4. payBill")
        print("5. exit")
        
        choice = int(input("enter your choice : "))
        if choice == 1:
            customer.view_menu(res)
        elif choice == 2:
            item_name = input("enter item name : ")
            item_quan = int(input("enter item quantity : "))
            customer.add_to_cart(res,item_name,item_quan)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid input")





def admin_menu():
    name = input("Enter your Name : ")
    email = input("Enter your email : ")
    phone = input("Enter your phone : ")
    address = input("Enter your address : ")
    admin = Admin(name,phone,email,address)

    

    while True:
        print(f"Welcome {admin.name}!!!")
        print("1. add new item")
        print("2. Add new employee")
        print("3. view employee")
        print("4. view item")
        print("5. Delete item")
        print("6. exit")
        
        choice = int(input("enter your choice : "))
        if choice == 1:
            item_name = input("enter item name : ")
            item_price = int(input("enter item price : "))
            item_quan = int(input("enter item quantity : "))
            item = FoodItem(item_name,item_price,item_quan)
            admin.add_new_item(res,item)
        elif choice == 2:
            name = input("Enter employee Name : ")
            email = input("Enter employee email : ")
            phone = input("Enter employee phone : ")
            address = input("Enter employee address : ")
            designation = input("Enter employee Designation : ")
            age = input("Enter employee Age : ")
            salary = input("Enter employee Salary : ")
            emp = Employee(name,phone,email,address,age,designation,salary)
            admin.add_employee(res,emp)
        elif choice == 3:
            admin.view_employee(res)
        elif choice == 4:
            admin.view_menu(res)
        elif choice == 5:
            item = input("enter item name : ")
            admin.remove_item(res,item)
        elif choice == 6:
            break
        else:
            print("Invalid input")


while True:
    print("Welcome !!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("enter your choice : "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input")