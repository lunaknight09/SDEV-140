#Nathan Hopkins
#Date October 25, 2023
#First Lab

# Get user input for name and birth year
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

# Calculate the age of the user as of January of the current year
current_year = 2023
age = current_year - birth_year

# Display the summary text
print(f"{name} was born in {birth_year}. On January 1st of this year, he was {age} years old.")