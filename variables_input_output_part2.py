#Nathan Hopkins
#Date October 25, 2023
#First Lab
# Description: This program asks the user to enter a score out of 15 and displays their grade as a percent.

# Get user input for the score out of 15
score_out_of_15 = int(input("Enter your score out of 15: "))

# Calculate the grade as a percent
grade_percent = (score_out_of_15 / 15) * 100

# Display the grade as a percent
print(f"Your final score was {grade_percent}%")
