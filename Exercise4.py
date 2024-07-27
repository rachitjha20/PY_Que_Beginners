# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# For example:

# remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.
# Note: n must be less than the length of the string.


def char_remover(s:str, n:int):
    if len(s) <= n:
        print("Length of string is lower than the character remaol request.")
    else:
        v = len(s)-n
        print(s[v::])
    
if __name__ == "__main__":
    s = str(input("Enter the string: "))
    n = int(input("Enter the number of charecter: "))
    char_remover(s, n)