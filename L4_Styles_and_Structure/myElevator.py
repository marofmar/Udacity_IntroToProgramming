import time

def print_pause(strings):
    print(strings)
    time.sleep(2)
def print_greeting1(number):
    print("You push the button for the "+number+" floor.")
    time.sleep(1)
def print_greeting2(place):
    print_pause("After a few moments, you find yourself in the "+place+".")
    #print_pause("Where would you like to go next?")
def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.") 

def first_floor(items):
        print_greeting1("first")
        print_greeting2("lobby")
        if "ID card" in items:
            print_pause("The clerk greets you, but he has already given you the ID card, "\
                "so there is nothing more to do here now.")
        else:
            print_pause("The clerk greets you and gives you your ID card.")
            items.append("ID card")
        print_pause("You head back to the elevator.")
        ride_elevator(items)
          
def second_floor(items):
        print_greeting1("second")
        print_greeting2("human resources department")
        if "handbook" in items:
            print_pause("The HR folks are busy at their desks."\
                "There doesnt' seem to be much to do here.")
        else:
            print_pause("The head of HR greets you.")
            if "ID card" in items:
                print_pause("He looks at your ID card and then gives you a copy "\
                    "of the employee handbook.")
                items.append("handbook")
            else:
                print_pause("He has something for you, but says he can't give it to you"\
                    " until you go get your ID card.")
            print_pause("You head back to the elevator.")
            ride_elevator(items)

def third_floor(items):
        print_greeting1("third")
        print_greeting2("engineering department")
        if 'ID card' in items:
            print_pause("You use your ID card to open the door.")
            print_pause("Your program manager greets you and tells you"\
                " that you need to have a copy of the employee handgboook"\
                "in order to start work.")
            if 'handbook' in items:
                print_pause("Fortunately, you got that from HR!")
                print_pause("Congratulations! You are ready to start your new job "\
                    "as vice president of engineering!")

            else:
                print_pause("They scowl  when they see that you don't have it, "\
                    "and send you back to the elevator.")
                ride_elevator(items)
        else:
            print_pause("Unfortunately, the door is locked and you can't get in.")
            print_pause("It looks like you need some kind of key card to open the door.")
            print_pause("You head back to the elevator.")
            ride_elevator(items)
def ride_elevator(items):
    print_pause("Please enter the number for the floor you would like to visit:")
    floor = int(float(input("1. Lobby\n"
                     "2. Human resources\n"
                     "3. Engineering department\n")))
    if floor == 1:
        first_floor(items)

    elif floor ==2:
        second_floor(items)
            
    elif floor ==3:
        third_floor(items)
    
    print_pause("Where would you like to go next?")


# start! 
def play_game():
    items = []
    intro()
    ride_elevator(items)

play_game()