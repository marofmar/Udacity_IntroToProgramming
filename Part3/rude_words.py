# rude words detector v0.2

rude_words = ['idiot', 'butt', 'devil', 'heck', 'jerk', 'crap', 'darn']

def check_line(line):
    rude_count = 0 
    words = line.split(" ")  # list of words 
    for word in words:
        if word in rude_words:
            rude_count += 1
            print(f"Foudn rude word: {word}")
    return rude_count

def check_file(filename):
        with open(filename) as my_story:
            rude_count = 0
            for line in my_story:
                rude_count += check_line(line)
        if rude_count == 0:
            print("Congrats, no rude word!")
        else:
            print("You should take another look to your writing! ")    
        
if __name__ == "__main__":
    check_file("sometext.txt")

    
