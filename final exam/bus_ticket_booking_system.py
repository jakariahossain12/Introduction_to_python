class Bus:
    def __init__(self,number,route,total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.seats = {}
        self.create_seats()

    def create_seats(self):
        rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        seat_count = 0 
        for row in rows:
            for col in range(1,5):
                if seat_count >= self.total_seats:
                    return
                
                seat_no = f"{row}{col}"
                self.seats[seat_no] = None
                seat_count +=1
    
    def show_seats(self):
        print(f"\n ========= seat  ============")

        count = 0

        for seat , passenger in self.seats.items():
            if passenger is None:
                print(f"{seat}(Empty)", end="\t")
            else:
                print(f"{seat}(Booked)", end="\t")
            
            count +=1

            if count % 4 == 0:
                print("\n")
    
    def available_seats(self):
        empty = 0

        for passenger in self.seats.values():
            if passenger is None:
                empty +=1
        
        return empty
    
    def book_seat(self,seat_no , passenger_name):
        if seat_no not in self.seats:
            print("Invalid seat number")
            return False
        
        if self.seats[seat_no] is not None:
            print("seat already booked")
            return False
        
        self.seats[seat_no] = passenger_name
        return True

class Passenger:
    def __init__(self,name,phone,bus,seat_no):
        self.name = name
        self.phone = phone
        self.bus = bus
        self.seat_no = seat_no
    

class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"
    
    def login(self , username ,password):

        return self.username == username and self.password == password
    

class BusSystem:

    def __init__(self):
        self.buses = []
        self.passengers = []
    
    def add_bus(self,number,route,seats):
        for bus in self.buses:
            if bus.number == number:
                print("Bus already exists")
                return
        
        new_bus = Bus(number,route,seats)
        self.buses.append(new_bus)
        print("bus added successfully")
    
    def find_bus(self,number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        
        return None

    def book_ticket(self,bus_number,name,phone):
        bus = self.find_bus(bus_number)
        if not bus:
            print("bus not found")
            return
        
        if bus.available_seats() == 0:
            print("No seats available")
            return
        
        bus.show_seats()

        sets_no = input("\n chose seat number : ").upper()

        book = bus.book_seat(sets_no,name)

        
        if book:
            passenger = Passenger(name,phone,bus,sets_no)
            self.passengers.append(passenger)
            print("ticket booked for ",name)
            print(f"bus : {bus.number} | route : {bus.route}")
            print("seat number : ",sets_no)
            print("fare : 500 taka")
        else:
            print("No seats available")
        
    def show_buses(self):
        if not self.buses:
            print("no buses available")
            return
        
        print("\n available busses")
        for bus in self.buses:
            print(f" bus no : {bus.number} | route : {bus.route} | available seats : {bus.available_seats()}")
    
    def show_passenger(self):
        if not self.passengers:
            print("no passenger available")
            return
        
        print("\n  ============= available passenger =============")
        for passen in self.passengers:
            print(f" passenger name : {passen.name} | bus number : {passen.bus.number} | seat no : {passen.seat_no} phone : {passen.phone}")

    
    def find_your_set(self, name , phone):
        if not self.passengers:
            print(" no passenger available")
            return
        f = False
        for psng in self.passengers:
            if psng.name.upper() == name:
                if psng.phone == phone:
                    print(f" Name : {name} | Bus no : {psng.bus.number} | seat no : {psng.seat_no} | phone : {phone}")
                    f = True
        
        
        if f == False:
            print("Not found the passenger")




def main():
    system = BusSystem()
    admin = Admin()

    while True:
        print("\n===== Bus System Menu =====")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Find the bus and seat number")
        print("5. Exit")

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
                    print("3. View All passenger")
                    print("4. Logout")
                    

                    admin_choice = input("Enter choice: ")

                    if admin_choice == "1":
                        number = input("Bus Number: ")
                        route = input("Route: ")
                        
                        seats = int(input("Total Seats: "))
                        system.add_bus(number, route, seats)
                        

                    elif admin_choice == "2":
                        system.show_buses()
                    
                    elif admin_choice == "3":
                        system.show_passenger()

                    elif admin_choice == "4":
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
            name = input("enter your name : ").upper()
            phone = input("enter your phone number : ")
            system.find_your_set(name,phone)

        elif choice == "5":
            print(" Exiting system...")
            break

        else:
            print(" Invalid choice")


main()




        