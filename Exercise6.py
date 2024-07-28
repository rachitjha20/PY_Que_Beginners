# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which
# are divisible by 5


def div_five(x):
    for i in x:
        if i%5 == 0:
            print(i)
            
if __name__ == "__main__":
    y = [12, 10, 15, 9, 25, 20]
    div_five(y)
    
    