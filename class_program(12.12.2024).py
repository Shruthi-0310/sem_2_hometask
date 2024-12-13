import random

class Customer:
    def __init__(self,customer_id,name,phone_num):
        self.Customer_id=customer_id
        self.name=name
        self.phone_num=phone_num

    def generate_random_id(self):
        random_id=random.randint(1000.9999)
        return f"TICK(random_id)"

    def verify_customer_id(customer_id):
        length=len(customer_id)
        number=0
        uppercase=0
        for i in customer_id:
            if i.isdigit():
                number+=1
            else:
                uppercase+=1
        if length>=8 and number>=4 and customer_id[0:4]=="TICK":
            print("Valid customer id")
        else:
            print("Invalid customer id")

class TicketBooking:
    def __init__(self):
        self.events={
            "Concert" : {"price":500,"seats":1000}
            "Stand up comedy" : {"price":1000,"seats":1500}
            "Theater" : {"price":350,"seats":500},
        }
        self.booked_tickets=[]

    def display_events(self):
        print("\nAvailable Events:")
        for event,details in self.events.items():
            print(f"{event}:${details['price']} per ticket, {details['seats']} seats available.")

    def 
            
            
         

print("Welcome to TICKET Booking application")
customer_id=input("Enter the customer ID:")


if customer.verify_customer_id(customer_id):
    name=input("Enter your name=")
    phone_num=int(input("Enter your phone number="))
    customer=Customer(customer_id,phone_number)
    print("Booking details")
else:
    print("Invalid! Please register.")
    name=input("Enter  your name:")
    phone_num=int(input("Enter your phone number="))
    customer_id=Customer(customer_id,name,phone_num)
    customer=customer(customer_id,phone_number)
    print("Your Customer id is :",customer_id)


while True:
    print("\nTicket Booking Menu:")
    print("1.View Events")
    print("2.Book Ticket")
    print("3.View My Ticket")
    print("4.Exit")
    choice=input("Enter your choice:")

if choice == "1":
    booking_system.display_events()
elif choice == "2":
    event_name =input("Enter the event name:")
    quantity = int(input("Enter the number of ticket:"))
    booking_system.book.ticket(event_name,quality,customer)
elif choice == "3":
    booking_system.view_booked_tickets(customer)
elif choice == "4":
    print("Thank you for using the Ticket Booking system! Have a great day!")
     


    



x`





    
