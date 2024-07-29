# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

def palindrome_num(x):
   
    if x == x[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")
                
if __name__ == "__main__":
    x = input("Enter the number: ")
    palindrome_num(x)