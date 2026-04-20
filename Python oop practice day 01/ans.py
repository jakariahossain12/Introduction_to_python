class Product:
    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity


class Shop:
    def __init__(self):
        self.products = []
    

    def add_product(self,product):
        self.products.append(product)
        print(f'{product.name} added successfully')
    
    def buy_product(self,product_name,quantity):
        for prod in self.products:
            if prod.name == product_name :
                if prod.quantity >= quantity:
                    prod.quantity-=quantity
                    print(f" congrats you successfully bought {quantity} {prod.name}")
                    return
                else:
                    print(" Not enough stock available")
                    return
            print("product not found")


shop = Shop()

p1 = Product('laptop',1000,23)

shop.add_product(p1)

shop.buy_product('jfijsof',23)
