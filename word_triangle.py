a = "abc"
"""
a
ab
abc
"""
# for i in range(len(a)):
#     print(a[0:(i+1)])

"""
abc
ab 
a
"""
for i in range(len(a),0,-1):
    print(i)
    print(a[0:(i)])

