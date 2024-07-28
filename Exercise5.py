# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Given:

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

def similar(x):
    if x[0] == x[-1]:
        print("True")
    else:
        print("False")
        
if __name__ == "__main__":
    num_x = [10, 20, 30, 20, 40, 50]
    similar(num_x)
    
    