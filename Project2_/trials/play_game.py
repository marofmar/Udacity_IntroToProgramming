from adv_game import print_pause, choose, game_begin, house, cave, beef, pop_corn, re_begin, face_monster
import time
import random
from params import *

while True:
    answer = game_begin()


    if answer == "house":
        house_decision = house()
        if house_decision == "1":  # new_weapon
            print_pause(f"Good. It is {prob}!")
            re_begin()


        elif house_decision == "2":  # direction 
            print_pause("Okay, you know where that monster is now! ")
            print_pause("Just came back to the starting point. ")
            print_pause("And heading to North, following the beef smell")
            beef()
            

        elif house_decision == "3":  # no question 
            print_pause("You decide to go back to the starting point.")
            re_begin()
        
    elif answer == "q":
        break
    elif answer == "cave":
        cave_decision = cave()
        if cave_decision == "1":  # weapon 
            print_pause(f"Oh, this is the {new_weapon}!")
            re_begin()

        elif cave_decision == "2":  # animal
            if animal == "tiger":
                print_pause("Great, I can fight with the tiger!")
                print_pause("Let's go tiger, we can beat the monster together!")
                print_pause("Tiger says, 'no thank you. Just go to North.'")
                re_begin()

            else:
                print_pause("Oh, that is a rabbit. "\
                        "I should go back to the starting point.")
                re_begin()


    elif answer == "beef":
        beef_decision = beef()
        if beef_decision == "1":  # join dinner
            print_pause("You approach to the monster.")
            print_pause("Asking, 'hello, can I join you?")
            print_pause(f"The {monster} stops cooking. He looks upset!!!")
            face_monster()
                
        elif beef_decision == "2":  # attack!
            print_pause("Yes, I am BRAVE!")
            face_monster()  

    elif answer == "pop corn":
        pop_corn_decision = pop_corn()
        if pop_corn_decision == "1":  # restart
            re_begin()
        elif pop_corn_decision == "2":  # watch movie
            print_pause(f"The {monster} unexpectedly welcomes you!")

