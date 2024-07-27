# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
sum = 0

for i in range(10):
    pre = i-1 #
    sum = i + pre
    if pre == -1:
        pre = 0
    print(f"Current Number {i} Previous Number {pre}  Sum: {sum}" )
    i+=i