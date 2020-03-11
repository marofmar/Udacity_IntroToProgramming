count = 0 
files = []
while True:
    count += 1
    print(f"Opening file #{count}")
    files.append(open("sometext.txt"))