# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.


def reverse_str(s):
    for i in range(0, len(s), 2):
        print(s[i])
    

if __name__ == "__main__" :
    s = str(input("Enter a string: "))
    reverse_str(s)