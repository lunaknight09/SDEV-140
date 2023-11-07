def print_pyramid(height):
    if height > 0:
        for i in range(1, height + 1):
            # Print spaces
            for j in range(height - i):
                print(" ", end="")
            # Print increasing numbers
            for j in range(1, i + 1):
                print(j, end="")
            # Print decreasing numbers
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()
    elif height < 0:
        height = abs(height)
        for i in range(height, 0, -1):
            # Print spaces
            for j in range(height - i):
                print(" ", end="")
            # Print increasing numbers
            for j in range(1, i + 1):
                print(j, end="")
            # Print decreasing numbers
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()
    else:
        print("Invalid input. Height must be a non-zero integer.")

# Main function
if __name__ == "__main__":
    try:
        height = int(input("Enter the height of the pyramid: "))
        print_pyramid(height)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")