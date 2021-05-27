#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program plays the number guessing game, but better

import math


def cylinder_volume(radius, height):

    volume = math.pi * (radius * radius) * height

    return volume


def main():

    while True:
        try:
            rad_input = input("Enter the radius (cm): ")
            rad_int = int(rad_input)
            height_input = input("Enter the height (cm): ")
            height_int = int(height_input)
            print("")

            if rad_int > 0 and height_int > 0:
                cylinder = cylinder_volume(rad_int, height_int)

                print("The volume is {0} cm²!!".format(cylinder))

                break
            else:
                print("Input must be a positive number!!!")
        except Exception:
            print("That is not even a number!!")
        finally:
            print("Wanna try again :)?")


if __name__ == "__main__":
    main()
