#Nathan Hopkins
#Date October 30, 2023
#Second Lab
#Write a program in Python that accepts three integers from a user and outputs them in order. You may not use arrays or sorting to accomplish this - only decision statements.

# Accept three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Compare the integers and output them in order
if num1 <= num2 and num1 <= num3:
    smallest = num1
    if num2 <= num3:
        middle = num2
        largest = num3
    else:
        middle = num3
        largest = num2
elif num2 <= num1 and num2 <= num3:
    smallest = num2
    if num1 <= num3:
        middle = num1
        largest = num3
    else:
        middle = num3
        largest = num1
else:
    smallest = num3
    if num1 <= num2:
        middle = num1
        largest = num2
    else:
        middle = num2
        largest = num1

# Output the ordered list of integers
print("The ordered list of integers is: {}, {}, {}".format(smallest, middle, largest))