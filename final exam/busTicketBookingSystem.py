
class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False



class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus



class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self, username, password):
        return username == self.username and password == self.password



class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []


    def add_bus(self, number, route, seats):
        for bus in self.buses:
            if bus.number == number:
                print(" Bus already exists")
                return
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print(" Bus added successfully")


    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        return None


    def book_ticket(self, bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if not bus:
            print(" Bus not found")
            return

        if bus.book_seat():
            passenger = Passenger(name, phone, bus)
            self.passengers.append(passenger)
            print(f" Ticket booked for {name}")
            print(f"Bus: {bus.number} | Route: {bus.route}")
            print("Fare: 500")
        else:
            print(" No seats available")


    def show_buses(self):
        if not self.buses:
            print(" No buses available")
            return

        print("\n Available Buses:")
        for bus in self.buses:
            print(f"Bus No: {bus.number} | Route: {bus.route} | Available Seats: {bus.available_seats()}")



def main():
    system = BusSystem()
    admin = Admin()

    while True:
        print("\n===== Bus System Menu =====")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            if admin.login(username, password):
                print(" Login successful!")

                while True:
                    print("\n--- Admin Menu ---")
                    print("1. Add Bus")
                    print("2. View All Buses")
                    print("3. Logout")

                    admin_choice = input("Enter choice: ")

                    if admin_choice == "1":
                        number = input("Bus Number: ")
                        route = input("Route: ")
                        
                        seats = int(input("Total Seats: "))
                        system.add_bus(number, route, seats)
                        

                    elif admin_choice == "2":
                        system.show_buses()

                    elif admin_choice == "3":
                        print(" Logged out")
                        break

                    else:
                        print(" Invalid choice")

            else:
                print(" Invalid credentials")

        elif choice == "2":
            bus_number = input("Enter Bus Number: ")
            name = input("Enter Your Name: ")
            phone = input("Enter Phone: ")
            system.book_ticket(bus_number, name, phone)

        elif choice == "3":
            system.show_buses()

        elif choice == "4":
            print(" Exiting system...")
            break

        else:
            print(" Invalid choice")


main()