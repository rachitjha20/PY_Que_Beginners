# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

for i in range(6, 1, -1):
    for j in range(i, 1, -1):
        print("*", end=" ")
    print()