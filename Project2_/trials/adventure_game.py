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


def play_game(monster, new_weapon, defeated, win):
    show_txt(intro)
    choice = choice_house_cave()

    if '1' in choice:  # knock knock house
        show_txt(knock_house)
        print_pause(
            "\nYou feel a bit under-prepared for this, what with only having a tiny dagger.")
        choice = choice_fight_run()

        if '1' in choice:  # fight!!!!!
            choice_dice_or_fight()

        elif '2' in choice:  # run!!!!!
            print_pause(
                "While running, you think, 'Sometimes, running away is the wisest decision.'")
            print_pause("You came back to the field.")
            play_game(monster, new_weapon, defeated, win)

    else:  # into the cave!
        show_txt(into_cave)
        choice = choice_old_new_weapon()
        if 'y' in choice:  # take new weapon
            print_pause(
                f"You discard your silly old dagger and take the ${new_weapon}$ with you.")
            print_pause(f"You walk back out to the field holding ${new_weapon}$, silently saying to yourself, "
                        "'yes, getting a better tool is always right.'")
            play_game(monster, new_weapon, defeated, win)

        else:  # keep the cute old littel dagger
            print_pause(
                "You turn around, firmly holding your dagger in you hand.")
            print_pause(
                "You silently tell your dagger, 'hey, I cannot throw you away. You have been my good company!'")
            print_pause("You walk back out to the field, with your dagger.")
            play_game(monster, new_weapon, defeated, win)


play_game(monster, new_weapon, defeated, win)
