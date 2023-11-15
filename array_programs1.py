#Nathan Hopkins
#Module 4
#November 13, 2023

"""
arrays_program1.py

This Python program allows the user to enter a series of numbers and then calculates and displays the sum and average of those numbers. The user can enter as many numbers as they want and stop entering numbers by typing 'q'.
"""

def calculate_average(numbers: list[float]) -> float:
    # Return the average of the provided list.
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def calculate_sum(numbers: list[float]) -> float:
    # Return the sum of the provided list.
    return sum(numbers)

def get_user_input() -> str:
    # Prompt the user for a number or 'q'.
    return input("Enter a number (or 'q' to quit): ")

def print_average(average: float) -> None:
    # Print the average.
    print(f"Average: {average}")

def print_sum(total_sum: float) -> None:
    # Print the sum.
    print(f"Sum: {total_sum}")

def get_list_of_numbers() -> list[float]:
    numbers: list[float] = []

    while True:
        user_input = get_user_input()

        if user_input.lower() == 'q':
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

    return numbers

def main():
    numbers: list[float] = get_list_of_numbers()
    
    if not numbers:
        print("No numbers entered.")
        return

    total_sum: float = calculate_sum(numbers)
    average: float = calculate_average(numbers)

    print_sum(total_sum)
    print_average(average)

if __name__ == "__main__":
    main()