import time
import random
from params import attackers, weapons, dice 
from adventure_story import intro, knock_house, into_cave, defeated, win, roll_dice
from make_decision_functions import choice_dice_or_fight, choice_fight_run, choice_house_cave, choice_old_new_weapon
from win_lose_functions import win_restart, defeat_restart
from utils import show_txt, print_pause, pick_random


monster = pick_random(attackers)
new_weapon = pick_random(weapons)
dice_value = pick_random(dice)

intro = "You find yourself standing in an open field, \nfilled with grass and yellow wildflowers."\
        f"Rumor has it that a *{monster}* is somewhere around here, \nand has been terrifying the nearby village.\n"\
        "In front of you is a house."\
        "To your right is a dark cave."


knock_house = f"""You approach the door of the house.
You are about to knock when the door opens and out steps a *{monster}*.
Eep! This is the *{monster}*'s house!
The *{monster}* attacks you!"""

into_cave = f"""You peer cautiously into the cave.
It turns out to be only a very small cave.
Your eye catches a glint of metal behind a rock.
You have found the ${new_weapon}$!"""

defeated = f"""You do your best...
but your dagger is no match for the *{monster}*.
You have been defeated!"""

win = f"""You walk back to the field, thinking that you having a pretty lucky day.
You decided to buy yourself a strawberry cake to celebrate this event! Yeyyy!!! """

roll_dice = f"The humongous {monster} looks down on you saying, "\
            "'hey, kido, listen, as you are real tiny to me, I feel bad hurting you."\
            "How about we roll a dice, and if the dice shows even number I will let you go, harmless. "\
            "However, in opposite case, if the dice shows odd number, "\
            "I am not sure you will be able to walk away from here. "\
            "Oh, for your information, my dice is {len(dice)} values. Unlike that of your world."
