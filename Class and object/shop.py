class shop:

    cart = [] # class attribute

    def __init__(self,byer):
        self.byer = byer
    
    def add_cart(self,item):
        self.cart.append(item)


j = shop("jakria")

j.add_cart("show")
j.add_cart("belt")

s = shop("sumon")
s.add_cart("watch")
s.add_cart("malboro")

print(j.cart)