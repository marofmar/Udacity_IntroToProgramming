import time
import random
from params import attackers, weapons, dice 
from adventure_story import intro, knock_house, into_cave, defeated, win, roll_dice
from make_decision_functions import choice_dice_or_fight, choice_fight_run, choice_house_cave, choice_old_new_weapon
from win_lose_functions import win_restart, defeat_restart
from utils import show_txt, print_pause, pick_random



def win_restart(win):
    show_txt(win)
    while True:
        end_choice = input("\nWould you like to play again? (y/n)\n")

        if 'n' in end_choice:
            print_pause("Ok, goodbye!")
            return end_choice

        elif 'y' in end_choice:
            print_pause("Excellent choice! Now restarting the game....")
            # restart
            play_game(monster, new_weapon, defeated, win)
            
        else:
            print_pause("\nPlease in yes or no only.\n")


def defeat_restart(defeated):
    show_txt(defeated)
    while True:
        end_choice = input("\nWould you like to play again? (y/n)\n")

        if 'n' in end_choice:
            print_pause("Ok, goodbye!")
            return end_choice

        elif 'y' in end_choice:
            print_pause("Excellent choice! Now restarting the game....")
            # restart
            play_game(monster, new_weapon, defeated, win)

        else:
            print_pause("\nPlease in yes or no only.\n")
