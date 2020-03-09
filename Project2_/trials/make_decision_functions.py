import time
import random
from params import attackers, weapons, dice 
from adventure_story import intro, knock_house, into_cave, defeated, win, roll_dice
from make_decision_functions import choice_dice_or_fight, choice_fight_run, choice_house_cave, choice_old_new_weapon
from win_lose_functions import win_restart, defeat_restart
from utils import show_txt, print_pause, pick_random



def choice_house_cave():
    while True:
        print_pause(
            "\n\tEnter 1 to knock on the door of the house.\n\tEnter 2 to peer into the cave.")
        choice = input(
            "\nWhat would you like to do?\n(Please enter 1 or 2.)\n")
        if "1" in choice:
            return choice
        elif "2" in choice:
            return choice
        else:
            print_pause("Invalid choice. Please enter 1 or 2.")


def choice_fight_run():
    while True:
        choice = input("\n\tWould you like to (1) fight or (2) run away?\n")
        if "1" in choice:
            return choice
        elif "2" in choice:
            return choice
        else:
            print_pause("Invalid choice. Please enter 1 or 2.")


def choice_old_new_weapon():
    while True:
        print_pause(
            "Now, you have to choose out of the two; your old dagger, and the new weapon in front of you")
        print_pause("The thing is, that new one might be haunted or cursed.")
        choice = input(
            "\n\tSo, would you like to take this new weapon with you? (y/n)\n")
        return choice

def choice_dice_or_fight():
    show_txt(roll_dice)
    while True:
        choice = input(
            "\n\tSo, what is your choice? Yes for rolling the dice, and no for just starting to fight.\n")
        if 'y' in choice:  # roll the dice
            if dice_value % 2 == 0:  # no fight, lucky kido
                print_pause(f"Oh, you are lucky. You got {dice_value}. Go back to your field."
                            "Happy that I don't have to hurt you.\n")
                print_pause(
                    "When you go back, you can say to others that you defeated me! Tell them you won me over!\n")
                end_choice = win_restart(win)

            else:
                print_pause(
                    f"Oh, you got odd value, {dice_value}. Today is not a good day for you, I guess.\n")
                end_choice = defeat_restart(defeated)

        elif 'n' in choice:  # let's fight, I dont need your pathetic emphacy! I am a fighter!!!
            print_pause(
                f"Let's fight, {monster}, I am a fighter and I don't need your pathetic empathy!")
            end_choice = defeat_restart(defeated)

        else:
            print_pause("Kido. Answer me in yes or no only, I am serious.")

        if 'n' in end_choice:
            break
