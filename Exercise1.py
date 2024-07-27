# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

x = int(input("X= "))
y = int(input("Y= "))
def main(x, y):
    
    if x*y <= 1000:
        return (x*y)
    else:
        return (x + y)

if __name__ == "__main__":
    result = main(x, y)
    print(result)