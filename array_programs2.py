#Nathan Hopkins
#Module 4
#November 13, 2023
"""
arrays_program2.py

This Python program is a simple game where the player has to guess the position of a ship on a board. 
The board size is determined at the start of the game. 
The player takes turns guessing the ship's position. 
After each guess, the board is displayed with the positions the player has guessed so far. 
The game continues until the player guesses the ship's position correctly.
"""
import random

def display_board(board_size: int, guessed_positions: list[int],
                  ship_position: int) -> None:
    for i in range(1, board_size + 1):
        if i in guessed_positions:
            if i == ship_position:
                print(" X |", end="")
            else:
                print(" O |", end="")
        else:
            print(" . |", end="")
    print()

    for i in range(1, board_size + 1):
        print(f" {i} |", end="")

    print()

def get_board_size() -> int:
    return int(input("Enter the board size: "))

def get_guess() -> int:
    return int(input("Enter your guess: "))
  
def is_hit(guess: int, ship_position: int) -> bool:
    return guess == ship_position

def initialize_ship_position(board_size: int) -> int:
    return random.randint(1, board_size)

def print_hit_message(is_hit: bool) -> None:
    if is_hit:
        print("Hit!")
    else:
        print("Miss!")

def take_turn(board_size: int, guessed_positions: list[int],
              ship_position: int) -> bool:
    guess = get_guess()
    guessed_positions.append(guess)
    display_board(board_size, guessed_positions, ship_position)
    hit = is_hit(guess, ship_position)
    print_hit_message(hit)
    return hit

def main():
    print("Welcome to Battleship!")

    board_size: int = get_board_size()
    ship_position: int = initialize_ship_position(board_size)
    guessed_positions: list[int] = []

    while not take_turn(board_size, guessed_positions, ship_position):
        pass

    print("Congratulations! You sunk the battleship!")

if __name__ == "__main__":
    main()