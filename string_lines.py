story = "When you need to change lines \
    make sure to type backward slash\
        uless you will face EOL(End of Lines) errors"

#print(story) # but unnecessary extra spaces btw them

story2 = "When you need to change lines \
make sure to type backward slash\
unless you will face EOL(End of Lines) errors"

#print(story2) # this works, but not easy too read.

# story3 = """When you need to change lines 
#             make sure to type backward slash
#             unless you will face EOL(End of Lines) errors"""

# print(story3) # again bunch of unnecessary spaces btw lines

# story =  "Once upon a time there was a very long string that was " +
#          "over 100 characters long and could not all fit on the " +
#          "screen at once."
# print(story)

# story =  "Once upon a time there was a very long string that was " +\
#          "over 100 characters long and could not all fit on the " +\
#          "screen at once."
# print(story)

story =  ("Once upon a time there was a very long string that was "
          "over 100 characters long and could not all fit on the "
          "screen at once.")
print(story)
print("Implicit line-joining and automatic string-literal concatenation?!")