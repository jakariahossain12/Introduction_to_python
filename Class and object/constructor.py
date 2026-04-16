class phone:
    menufactured = "china"

    def __init__(self , owner,price,brand):
        self.owner = owner
        self.price = price
        self.brand = brand

j = phone("jakaria",3433,"samsung")

print(j.owner,j.brand,j.price)