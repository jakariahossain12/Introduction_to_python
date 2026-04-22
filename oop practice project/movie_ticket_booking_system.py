
class Hall:

    def __init__(self,hall_no,row,col):
        self.hall_no = hall_no
        self.row = row
        self.col = col
        self.seats = {}
        self.show_list = []
    
    def enter_show(self,show_id,movie_name,time):
        self.tuple = (show_id,movie_name,time)
        self.show_list.append(self.tuple)
        self.seat_list = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append('free')
            self.seat_list.append(row)
        
        self.seats[show_id] = self.seat_list
    
    def view_show_list(self):
        for x in self.show_list:
            print(f' show id : {x[0]}  Movie : {x[1]}  Time: {x[2]}\n')
    
    def view_available_seats(self,id):
        if id not in self.seats:
            print("wrong show id")
        else:
            for i in self.show_list:
                if i[0] == id:
                    print(f'Movie : {i[1]} \t\t time: today at {i[2]}\n')
                
            for x in range(self.row):
                for y in range(self.col):
                    if(self.seats[id][x][y] == 'free'):
                        print(f'{chr(x+65)}{y+1}  \t', end="")
                    else:
                        print('x  \t', end="")
                print("\n")

    def book_tickets(self,id,name,phone,booking_seats):
        if id not in self.seats:
            print("Wrong show id")
        else:
            for x in booking_seats:
                r = ord(x[0]) - 65
                c = ord(x[1]) - 49
                if r >= self.row or c >= self.col or r<0 or c <0:
                    print("Seat doesn't exists.")
                elif self.seats[id][r][c] != 'free':
                    print(x , "is already booked")
                else:
                    self.seats[id][r][c] = 'x'
            
            print("\n\t #### ticket Booked Successfully ###")
            print("\n------------------------------------------")
            print("Name: ",name)
            print("Phone: ", phone)
            for i in self.show_list:
                if i[0] == id:
                    print("Movie: ",i[1], " time: today at: ", i[2])



my_hall = Hall(2,6,8)
my_hall.enter_show(444,'Domm','10:00 pm')
my_hall.enter_show(333,'ABCD','11:00 pm')
my_hall.enter_show(222,'Asiki2','8:00 pm')

while True:
    print("\n -----------------------------------------------------------")
    print("1. view all show today")
    print("2. view available seats")
    print("3. Book tickets")
    option = int(input("Enter your option "))
    print("\n")

    if option == 1:
        print("\n -----------------------------------------------------------\n")
        my_hall.view_show_list()
    elif option == 2:
        id = int(input("Enter show id: "))
        print("\n -----------------------------------------------------------")
        my_hall.view_available_seats(id)
    elif option == 3:
        id = int(input("Enter show id: "))
        name = input("Enter your name: ")
        phone = input("Enter your phone no: ")
        tickets = int(input("Enter number of tickets: "))
        booking_seats = []
        for i in range(tickets):
            booking_seats.append(input("Enter your seat no. "))
        
        my_hall.book_tickets(id,name,phone,booking_seats)
    else:
        print("wrong option, choose again\n")
