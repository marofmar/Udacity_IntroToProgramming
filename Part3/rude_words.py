# rude words detector v0.1

rude_words = ['idiot', 'butt', 'devil', 'heck', 'jerk', 'crap', 'darn']

with open("sometext.txt") as my_story:
    contents = my_story.read()
    rude_count = 0
    for rude in rude_words:
        if rude in contents:
            rude_count += 1
            print(f"Found rude word: {rude}")
if rude_count == 0:
    print("Congrats, no rude word!")
    