def double_decker():
    print("starting the double decker")

    def inner_fun():
        print("inside the inner")
    
    return inner_fun


print(double_decker()())