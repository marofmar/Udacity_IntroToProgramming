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
            "gigantic notorious octopus",
            ]

weapons = [
            "magical Sword of Ogoroth",
            "gigantic Christmas candy cane",
            "Torr's hammer",
            "golden chopstick",
            "needle",
            "big wood stick",
            "Japanese sword",
]

dice = [1,2,3,4,5,6,7,8,9,10,11]

def pick_random(choices):
    return random.choice(choices)

monster = pick_random(attackers)
new_weapon = pick_random(weapons)
dice_value = pick_random(dice)

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

win = f"""You walk back to the field, thinking that you having a pretty lucky day.
You decided to buy yourself a strawberry cake to celebrate this event! Yeyyy!!! """

roll_dice = f"""The humongous {monster} looks down on you saying 'hey, kido, listen, as you are real tiny to me, I feel bad hurting you.
How about we roll a dice, and if the dice shows even number I will let you go, harmless. 
However, in opposite case, if the dice shows odd number, then, I am not sure you will be able to walk away from here. 
Oh, for your information, my dice is {len(dice)} values. Unlike that of your world."""

def win_restart(win):
    show_txt(win)
    while True:
        end_choice = input("\nWould you like to play again? (y/n)\n")

        if 'n' in end_choice:
            print_pause("Ok, goodbye!")
            break
            return end_choice

        elif 'y' in end_choice:
            print_pause("Excellent choice! Now restarting the game....")
            #restart
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
            break

        elif 'y' in end_choice:
            print_pause("Excellent choice! Now restarting the game....")
            #restart
            play_game(monster, new_weapon, defeated, win)
        
        else:
            print_pause("\nPlease in yes or no only.\n")

def choice_dice_or_fight():
    show_txt(roll_dice)
    while True:
        choice = input("\n\tSo, what is your choice? Yes for rolling the dice, and no for just starting to fight.\n")
        if 'y' in choice: # roll the dice
            if dice_value%2 == 0: # no fight, lucky kido
                print_pause(f"Oh, you are a lucky kiddo. You got {dice_value}. Go back to your field. Happy that I don't have to hurt you.\n")
                print_pause("When you go back, you can say to others that you defeated me, and you won me over!\n")
                end_choice = win_restart(win)
      
            else:
                print_pause(f"Oh, you got odd value, {dice_value}. Today is not a good day for you, I guess.\n")
                end_choice = defeat_restart(defeated)


        elif 'n' in choice: # let's fight, I dont need your pathetic emphacy! I am a fighter!!!
            print_pause(f"Let's fight, {monster}, I am a fighter and I don't need your pathetic empathy!")
            end_choice = defeat_restart(defeated)

        else:
            print_pause("Kido. Answer me in yes or no only I am damn serious.")
        
        if 'n' in end_choice:
            break
    

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


def play_game(monster, new_weapon, defeated, win):
    show_txt(intro)
    choice = choice_house_cave()

    if choice == 1: #knock knock house
        show_txt(knock_house)
        print_pause("\nYou feel a bit under-prepared for this, what with only having a tiny dagger.")
        choice = choice_fight_run()
        
        if choice ==1: # fight!!!!!
            choice_dice_or_fight()

        elif choice ==2: #run!!!!!
            print_pause("While running, you think, 'Sometimes, running away is the wisest decision.'")
            print_pause("You came back to the field.")
            # restart
            play_game(monster, new_weapon, defeated, win)
    else: #into the cave! 
        show_txt(into_cave)
        choice = choice_old_new_weapon()
        if 'y' in choice: # take new weapon
            print_pause(f"You discard your silly old dagger and take the ${new_weapon}$ with you.")
            print_pause(f"You walk back out to the field holding ${new_weapon}$, silently saying to yourself, 'yes, getting a better tool is always right.'")
            # restart
            play_game(monster, new_weapon, defeated, win)
        else: # keep the cute old littel dagger
            print_pause("You turn around, firmly holding your dagger in you hand.")
            print_pause("You silently tell your dagger, 'hey, I cannot throw you away. You have been my good company!'")
            print_pause("You walk back out to the field, with your dagger.")
            #restart 
            play_game(monster, new_weapon, defeated, win)

play_game(monster, new_weapon, defeated, win)