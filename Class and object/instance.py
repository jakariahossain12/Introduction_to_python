class shop:

    

    def __init__(self,byer):
        self.byer = byer
        self.cart = [] # cart is an instance attribute
    
    def add_cart(self,item):
        self.cart.append(item)


j = shop("jakria")

j.add_cart("show")
j.add_cart("belt")

print(j.cart)
s = shop("sumon")
s.add_cart("watch")
s.add_cart("malboro")

print(s.cart)