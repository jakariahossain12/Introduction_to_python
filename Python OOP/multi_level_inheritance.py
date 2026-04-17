class Vehicle:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def move(self):
        pass


class Bus(Vehicle):
    def __init__(self, name, price,seat):
        self.seat = seat
        super().__init__(name, price)

class Truck(Vehicle):
    def __init__(self, name, price,weight):
        self.weight = weight
        super().__init__(name, price)


class PickupTruck(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)


class ACBus(Bus):
    def __init__(self, name, price, seat,temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)