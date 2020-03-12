# writefile = open("newfile.txt", "w")
# writefile.write("hey\n")
# writefile.write("i" for i in range(10))
# writefile.close()
# a = open("newfile.txt")
# print(a.read())


# with open("output.txt", "w") as output:
#     output.write("Yayyyy!")

with open("hm.txt", "w") as f:
    for i in range(30):
        if i % 2 == 0:
            i = str(i)
            f.write(i+"\n")

with open("hm.txt") as f:
    print(f.read())