#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program area rect


def main():
    # funciton calculates area and pereimetn
    
    #input
    side = float(input("What is side dimension:"))
    side2 = float(input("What is other dimension:"))
    
    #process
    area = side * side2
    perimeter = 2 * (side + side2)
    
    #output
    print("\nThe area is " + str(round(area)) + " units squared")
    print("The perimeter is " + str(round(perimeter)) + " units")


if __name__ == "__main__":
    main()
