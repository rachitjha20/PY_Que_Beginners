# Exercise 10: Create a new list from two list using the following condition
# Create a new list from two list using the following condition

# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# Given:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

def new_list(x, y):
    c_new_list = []
    if len(x) == len(y):
        for i in range(len(x)):
            if x[i]%2 == 1:
                c_new_list.append(x[i])
        
        for i in range(len(y)):
                if y[i]%2 == 0:
                    c_new_list.append(y[i])
    print(c_new_list)
        
    
if __name__ =="__main__":
    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]
    new_list(list1, list2)