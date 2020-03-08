import time 
import random 

def print_pause(strings):
    print(strings)
    time.sleep(1) 

def show_txt(txt):
    for i in txt.splitlines():
        print_pause(i)

attackers = [
            "wicked fairie", 
            "pirate", 
            "dragon",
            "troll",
            "gigantic notorious octopus"
            ]
weapons = [
            "magical Sword of Ogoroth",
            "gigantic Christmas cany cane",
            "Torr's hammer"
]

def pick_random(choices):
    return random.choice(choices)

monster = pick_random(attackers)
new_weapon = pick_random(weapons)

intro_first = f"""You find yourself standing in an open field, filled with grass and yellow wildflowers.
Rumor has it that a *{monster}* is somewhere around here, and has been terrifying the nearby village.
In front of you is a house.
To your right is a dark cave.
In your hand you hold your trusty (but not very effective) dagger."""

intro = f"""You find yourself standing in an open field, filled with grass and yellow wildflowers.
Rumor has it that a *{monster}* is somewhere around here, and has been terrifying the nearby village.
In front of you is a house.
To your right is a dark cave."""


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


def choice_house_cave():
    while True:
        print_pause("\n\tEnter 1 to knock on the door of the house.\n\tEnter 2 to peer into the cave.")
        choice = input("\nWhat would you like to do?\n(Please enter 1 or 2.)\n")
        if "1" in choice:
            return int(float(choice))
        elif "2" in choice:
            return int(float(choice))
        else:
            print_pause("Invalid choice. Please enter 1 or 2.")
    
def choice_fight_run():
    while True:
        choice = input("\n\tWould you like to (1) fight or (2) run away?\n")
        if "1" in choice:
            return int(float(choice))
        elif "2" in choice:
            return int(float(choice))
        else:
            print_pause("Invalid choice. Please enter 1 or 2.")

def choice_old_new_weapon():
    while True:
        print_pause("Now, you have to choose out of the two; your old dagger, and the new weapon in front of you")
        print_pause("The thing is, that new one might be haunted or cursed.")
        choice = input("\n\tSo, would you like to take this new weapon with you? (y/n)\n")
        return choice 


def play_game(monster, new_weapon):
    show_txt(intro)
    choice = choice_house_cave()

    if choice == 1: #knock knock house
        show_txt(knock_house)
        print_pause("\nYou feel a bit under-prepared for this, what with only having a tiny dagger.")
        choice = choice_fight_run()
        
        if choice ==1: # fight!!!!!
            show_txt(defeated)
            choice = input("\nWould you like to play again? (y/n)\n")

            if 'n' in choice:
                print_pause("Ok, goodbye!")

            elif 'y' in choice:
                print_pause("Excellent choice! Now restarting the game....")
                #restart
                play_game(monster, new_weapon)

        elif choice ==2: #run!!!!!
            print_pause("While running, you think, 'Sometimes, running away is the wisest decision.'")
            print_pause("You came back to the field.")
            # restart
            play_game(monster, new_weapon)     
    else: #into the cave! 
        show_txt(into_cave)
        choice = choice_old_new_weapon()
        if 'y' in choice: # take new weapon
            print_pause(f"You discard your silly old dagger and take the ${new_weapon}$ with you.")
            print_pause(f"You walk back out to the field holding ${new_weapon}$, silently saying to yourself, 'yes, getting a better tool is always right.'")
            # restart
            play_game(monster, new_weapon)
        else: # keep the cute old littel dagger
            print_pause("You turn around, firmly holding your dagger in you hand.")
            print_pause("You silently tell your dagger, 'hey, I cannot throw you away. You have been my good company!'")
            print_pause("You walk back out to the field, with your dagger.")
            #restart 
            play_game(monster, new_weapon)


play_game(monster, new_weapon)