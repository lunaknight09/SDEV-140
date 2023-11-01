#Nathan Hopkins
#Date November 1, 2023
#Module 2.2 Lab
# Description: This program calculates the distance between two points (x1, y1) and (x2, y2) entered by the user.

import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 2)

def print_output(distance):
    print(f'The distance between these points is {distance}')

def main():
    x1 = float(input('Enter x1 coordinate: '))
    y1 = float(input('Enter y1 coordinate: '))
    x2 = float(input('Enter x2 coordinate: '))
    y2 = float(input('Enter y2 coordinate: '))

    distance = calculate_distance(x1, y1, x2, y2)
    print_output(distance)

if __name__ == "__main__":
    main()