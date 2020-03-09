import time
import random
from params import attackers, weapons, dice 
from adventure_story import intro, knock_house, into_cave, defeated, win, roll_dice
from make_decision_functions import choice_dice_or_fight, choice_fight_run, choice_house_cave, choice_old_new_weapon
from win_lose_functions import win_restart, defeat_restart
from utils import show_txt, print_pause, pick_random


def print_pause(strings):
    print(strings)
    time.sleep(1)


def show_txt(txt):
    for i in txt.splitlines():
        print_pause(i)

def pick_random(choices):
    return random.choice(choices)
