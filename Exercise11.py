# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def rev_order(x):
    print(" ".join(x[::-1]))
        
if __name__ == "__main__":
    y = input("enter the number")
    rev_order(y)