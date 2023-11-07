#Nathan Hopkins
#Date November 6th, 2023
#Module 3  First Lab Pyramid
def get_input() -> int:
    while True:
        try:
            height = int(input("Enter the height of the pyramid: "))
            return height
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def write_pyramid_row(row: int, height: int) -> None:
    # Print spaces before numbers
    for i in range(height - row):
        print(" ", end="")
    # Print increasing numbers
    for i in range(1, row + 1):
        print(i, end="")
    # Print decreasing numbers (if there are any)
    for i in range(row - 1, 0, -1):
        print(i, end="")
    print()

def create_pyramid(height: int) -> None:
    # Invert the pyramid if height is negative
    if height < 0:
        height = abs(height)
        for i in range(height, 0, -1):
            write_pyramid_row(i, height)
    else:
        # Loop through write_pyramid_row to create the full pyramid
        for i in range(1, height + 1):
            write_pyramid_row(i, height)

if __name__ == "__main__":
    height = get_input()
    create_pyramid(height)
