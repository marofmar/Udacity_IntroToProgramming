import time

def print_pause(msg):
    '''
    msg: messages to be displayed to users
    '''
    print(msg)
    time.sleep(2)

def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def valid_response(prompt, options):
    '''
    prompt: message to show to users
    options: food menu options, a list containig string menu names
    '''
    response = input(prompt).lower()
    for i in options:
        if i in response:
            print(i.title()+" it is!")
            return response
    return 0

def take_order():
    response = valid_response("\tPlease place your order. Would you like waffles or pancakes?\n", ['waffle', 'pancake'])
    if response:
        print_pause("Good choice, your order will be ready shortly.")
    else:
        print_pause("Hm.. Sorry, but I should tell you that we do not have that for now.")
        take_order()

def add_order():
    order_again = input("\tWould you like to order another? Please answer me either 'yes' or 'no.\n").lower()
    if 'y' in order_again:
        print_pause("\t\tWe are happy to take your order.")
        take_order()
        add_order()
    elif 'n' in order_again:
        print_pause("Okay, see you later!")
    else: 
        print_pause("Sorry, I don't understand.")
        add_order()
    
intro()    
take_order()
add_order()