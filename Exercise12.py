# Exercise 12: Calculate income tax for the given income by adhering to the rules below
# Taxable          Income	    Rate (in %)
# First            $10,000	       0
# Next             $10,000	       10
# The remaining	                   20
# Expected Output:

# For example, suppose the taxable income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000.


x = int(input("Enter the Annual Income: "))

if x <= 0:
    print("Enter the correct amount")
elif x >= 0 & x <= 10000:
    print("Not a Taxable amount.") 
else:
    taxable_amt = ((10000*0)/100) + ((10000*10)/100) + (((x-20000)*20)/100)
    print(f"Taxable amount is ${taxable_amt} .")