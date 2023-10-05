import os
file = open("ved.txt", "w")

file.write("hi\n")

file.close()


file = open("ved.txt", "a")

file.write("hi.2")

file.close()


file = open("ved.txt", "r")

r = file.read()

file.close()

print(r)

