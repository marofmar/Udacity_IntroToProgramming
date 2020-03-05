import time

def print_pause(strings):
    print(strings)
    time.sleep(2)
def print_greeting1(number):
    print("You push the button for the "+number+" floor.")
    time.sleep(1)
def print_greeting2(place):
    print_pause("After a few moments, you find yourself in the "+place+".")
    print_pause("Where would you like to go next?")
    
print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.") 

while True:
    print_pause("Please enter the number for the floor you would like to visit:")
    floor = int(input("1. Lobby\n"
                     "2. Human resources\n"
                     "3. Engineering department\n"))
    if floor == 1:
        print_greeting1("first")
        print_greeting2("lobby")
    elif floor ==2:
        print_greeting1("second")
        print_greeting2("human resources department")
    else:
        print_greeting1("third")
        print_greeting2("engineering department")
         