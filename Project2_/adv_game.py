import time
import random
from params import *

def print_pause(strings):
    print(strings)
    time.sleep(1)


def pick_random(choices):
    return random.choice(choices)


def choose(li):
    while True:
        choose = input(">>>> ")        
        for i in range(len(li)):
            if choose == li[i]:
                choice = choose
                print_pause(f"So, you chose {choice}. Good.")
                return choice
        print(f"Please enter one value out of {li}")



def game_begin():
    print(r"""
            />____________________________________________
    [########[]__________GAME START_______________________>
            \>
          """)
    print_pause("You find yourself in a dark dungeon. ")
    print_pause(f"You came here to kill the notorious monster, *{monster}*")
    print_pause("Looking around, you find that you are" \
                "in the middle of an intersection.")
    print_pause("Luckly, you have a compass in your pocket. "\
                "You pull out the compass.")
    print_pause("East road leads to a house. ")
    print_pause("West road leads to a cave. ")
    print_pause("North road, you cannot see anything, too dark. "\
                "But, you can smell grilled beef.")
    print_pause('South road, you can smell pop corn.')
    print_pause("===============================================\n"
                "\tEnter 1 to go east.\n"
                "\tEnter 2 to go west.\n"
                "\tEnter 3 to go North.\n"
                "\tEnter 4 to go South.\n"
                "\tEnter q to quit this game.\n"
                "================================================")
    choice = choose(["1", "2", "3", "4", "q"])

    if choice == "1":
        print_pause("You chose to knock the door of the house.")
        return "house"
    elif choice == "2":
        print_pause("You chose to peep inside the cave.")
        return "cave"
    elif choice == "3":
        print_pause("So, let's find where that delicious smell come from!")
        return "beef"
    elif choice == "4":
        print_pause("Pop corn? Really? In this dark dungeon? "\
                    "Anyhow, let's go to the South!")
        return "pop corn"
    else choice == "q":
        print_pause("Goodbyebyebye")
        return "q"


def re_begin():
    print_pause(f"Now, you know the winning probabilty, {prob}")
    print_pause("You now came back to the starting point.")
    print_pause("East road leads to a house. ")
    print_pause("West road leads to a cave. ")
    print_pause("North road, you cannot see anything, too dark. "\
                "But, you can smell grilled beef.")
    print_pause('South road, you can smell pop corn.')
    print_pause("===============================================\n"
                "\tEnter 1 to go east(house).\n"
                "\tEnter 2 to go west(cave).\n"
                "\tEnter 3 to go North(grilling beef).\n"
                "\tEnter 4 to go South(pop corn).\n"
                "\tEnter q to quit this game.\n"
                "================================================")
    choice = choose(["1", "2", "3", "4", "q"])

    if choice == "1":
        house()
    elif choice == "2":
        cave() 
    elif choice == "3":
        beef()
    elif choice == "4":
        pop_corn()
    elif choice == "q":

    

def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock"
                " when the door opens and out steps an old man.")
    print_pause("Oh! This is the famous fortuneteller's house!")
    print_pause("The old man asks you a question.")
    print_pause("'I was waiting for you. Choose one out of them'")
    print_pause("================================================\n"
                "\tEnter 1 the winning probabiliy of yours.\n"
                "\tEnter 2 the direction you should go to find the monster.\n"
                "\tEnter 3 if you have nothing to know.\n"
                "================================================")
    choice = choose(["1", "2", "3"])
    return choice 

def face_monster():
    print_pause("Before starting this journey, you set a rule.")
    print_pause("You only engage in physical fight "\
                "only if the probabily to win the monster exceeds 50%.")
    print_pause(f"This time, the probabily value is {prob}.")

    if probability > 0.5:
        raw_fight()
    else:
        smart_fight()

def raw_fight():
    print_pause(f"You believe you can beat this monster {prob}.")
    print_pause("but this monster is stronger than expected!")
    print_pause("(scary sounds,,,,)")
    print_pause("(even scarier sounds,,,,!)")
    print_pause("(suddenly, tranquilo!)")
    print_pause("Wow, you just killed the monster!!!!!!!!")
    print_pause("Congratulations! You made it! ")

    start_over()
    


def smart_fight():
    print_pause("You know that it is unlikely to beat the monster.")
    print_pause(f"As your probability to win the monster is only {prob}!")
    print_pause("So, you make a suggestion, "\
                "to roll a dice to decide who wins.")
    print_pause(f"The {monster} agrees with your idea, "\
                "but with one condition.")
    print_pause(f"The {monster} says, "\
                "then we should use my dice."\
                "As I do not trust human's dice.")
    print_pause(f"Monster says, 'my dice has {len(dice)} values.'")
    print_pause("'If even number comes up, you win. You can go home.'")
    print_pause(f"Otherwise, this great {monster}, I win.")
    print_pause("...............Rolling dice!..................")
    dice_value = random.choice(dice)
    print_pause(f"The number? {dice_value}.")

    if dice_value % 2 == 0:
        print_pause("You WIN!")
    else:
        print_pause("You LOSE.....!")

    start_over()


def run_away():
    print_pause("RUN RUN RUN!!!!")
    print_pause("Now, you are safe, came back to the starting point. ")
    
    re_begin()
    
    
def encourage():
    print_pause("Hey, you can do better!")
    print_pause("Your family and friends believe in you!")
    print_pause("Do not underestimate your pontential! ")
    print_pause("You can do this!")

    start_over()


def start_over():
    print_pause("Would you like to play this game again?")
    print_pause("================================================\n"
                "\tEnter 1 if you want to restart this game.\n"
                "\tEnter 2 if you want to quit this game.\n"
                "\tEnter 3 if you want to hear encouragements and restart.\n"
                "================================================")
    choice = choose(["1", "2", "3"])
    if choice == "1":
        print_pause("Excellent! Restarting your game,,,,,,")
        game_begin()
    elif choice == "2":
        print_pause("Goodbye!")
    elif choice == "3":
        encourage()

def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("Your eye catches a glint of something behind a rock.")
    print_pause("'What is that?' You approach to that silently.")
    print_pause("================================================\n"
                "\tEnter 1 if that is a weapon.\n"
                "\tEnter 2 if that is an animal.\n"
                "================================================")
    choice = choose(["1", "2"])
    return choice 


def beef():
    print_pause("You walk in the dark.")
    print_pause("Oh, there is something at the end of this road!")
    print_pause(f"Gosh, the {monster} is cooking for his dinner!")
    print_pause("It seems like the monster not yet notices you.")
    print_pause("What do you want to do now?")
    print_pause("================================================\n"
                "\tEnter 1 if you want to join dinner with the monster.\n"
                "\tEnter 2 if you want to attack the monster.\n"
                "================================================")
    choice = choose(["1", "2"])
    return choice 

    
def pop_corn():
    print_pause("You follow rich smell of pop corn.")
    print_pause("On your way, you hear some sound.")
    print_pause("Getting more and more curious,,,,")
    print_pause("WHAT??? Cinema??? Really???? ")
    print_pause(f"You see a sign, '{monster}'s Theater'.")
    print_pause("What do you want to do now?")
    print_pause("================================================\n"
                "\tEnter 1 if you want to restart this game.\n"
                "\tEnter 2 if you want to watch a movie with the monster."\
                "Maybe you can have a chance to attack him durin the movie.\n"
                "================================================")
    choice = choose(["1", "2"])
    return choice 





