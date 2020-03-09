import time
import random


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


def intro_pic():
    print(r"""
            />____________________________________________
    [########[]__________GAME START_______________________>
            \>
          """)
    print_pause("===============================================\n"
                "\tEnter 1 to start Roll thd dice game.\n"
                "\tEnter 2 to start Random draw game.\n"
                "\tEnter 3 to quit the game.\n"
                "================================================")
    choice = choose(["1", "2", "3"])
    return choice


def dice_intro_rule():
    print("\t<<Rule of this game: Dice Game>>")
    print_pause("It is widely known that this monster is a dice collector.")
    print_pause("Rule is simple. Odd number, you lose.")
    print_pause("Even number, you win.")
    print_pause("Good? Ok, let's start dice game.")


def draw_intro_rule():
    print("\t<<Rule of this game: Random Draw Game.>>")
    print_pause("There will be a monster in the woods.")
    print_pause("And you will be assigned a weapon.")
    print_pause("If the weapons's power outweights that of monster, "
                "you win this game.")
    print_pause("Otherwise, you lose.")
    print_pause("Good? Ok, let's start random draw game.")


def play():
    choice = intro_pic()
    if choice == "1":
        dice_intro_rule()
        dice_round(choose_dice())

    elif choice == "2":
        draw_intro_rule()
        draw_round()

    elif choice == "3":
        print_pause("Okay, goodbye!")


def play_again():
    print("\tSo, would you like to play again?")
    print_pause("===============================================\n"
                "\tEnter 1 to restart.\n"
                "\tEnter 2 to quit.\n"
                "================================================")
    choice = choose(["1", "2"])
    if choice == "1":
        play()
    else:
        print_pause("Ok, you must be tired, take a good rest. Goodbye! ")


def draw_weapon():

    print_pause("........drawing your weapon........")
    weapons = ['scissor',
               'knife',
               'candy cane',
               'dagger',
               'pepper spray',
               ]
    weapon = random.choice(weapons)
    prob2 = random.randint(1, 100)
    print_pause(f"Your weapon: {weapon}, power score: {prob2}")
    print_pause("Satisfied with this result?")
    print_pause("===============================================\n"
                "\tEnter 1 to draw again.\n"
                "\tEnter 2 to move on.\n"
                "================================================")
    choice = choose(["1", "2"])
    if choice == "1":
        draw_weapon()
    elif choice == "2":
        print_pause(f"You keep this power score {prob2}, nice.")
    return prob2


def draw_monster():
    print_pause("........your opponent monster is.......")
    monsters = ['hulk',
                'jelly fish',
                'gorgon',
                'dragon',
                'Santa',
                'Furious Rudolf',
                ]
    monster = random.choice(monsters)
    prob2 = random.randint(1, 100)
    print_pause(f"Your monster: {monster}, power score: {prob2}")
    return prob2


def draw_round():
    prob_win = draw_weapon()
    prob_lose = draw_monster()
    if prob_win > prob_lose:
        print_pause("Ok, you won the monster!")
        print_pause("Congratulations!\n\n")
        play_again()
    elif prob_win < prob_lose:
        print_pause("You tried your best, but defeated...\n\n")
        play_again()
    else:
        print_pause("Hmmm.. even power score. Let's draw again.")
        draw_weapon()
        draw_monster()


def choose_dice():
    dice_val = random.randrange(1, 100)
    print_pause(f"This time, the monster picks {dice_val}-dim dice. ")
    print_pause("You okay with this dice? ")
    print_pause("===============================================\n"
                "\tEnter 1 to ask the monster to pick another.\n"
                "\tEnter 2 to move on.\n"
                "================================================")
    choice = choose(["1", "2"])
    if choice == "1":
        choose_dice()
    elif choice == "2":
        print_pause(f"Okay, now throwing {dice_val}-dim dice up high!")
        dice_val = int(dice_val)
    return dice_val


def dice_round(dice_val):

    lst = []
    for i in range(dice_val):
        lst.append(i+1)

    print_pause(",,,,,,,,,,,what would be the number?,,,,,")

    val = random.choice(lst)

    print_pause("You and monster came to see the value of the dice.")
    if val % 2 == 0:
        print_pause(f"Yes!!! {val}!!!!!! Even number!")
        print_pause("Monster says, 'okay. I am a cool monster. You win.'\n\n")
        play_again()
    else:
        print_pause(f"..............{val}.......Oh... my.. goddenss..")
        print_pause("Monster says, 'hey don't be so sad. Life happens. '")
        print_pause("But seems clear I just won you over. HAHAHAHA'\n\n")
        play_again()
