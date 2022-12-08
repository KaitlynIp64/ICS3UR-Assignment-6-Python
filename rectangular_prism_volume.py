#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program calculates volume of a rectangular prism


import random


def volume_of_rectangular_prism(int_base, int_height, int_width):
    # calculate area

    # process
    volume = int_base * int_height * int_width

    # output
    print("The volume of the rectangular prism is: {0}cm³.".format(volume))


def main():
    # input
    while True:
        string_base = input("Enter the base (cm): ")
        string_height = input("Enter the height (cm): ")
        string_width = input("Enter the width (cm): ")

        try:
            int_base = int(string_base)
            int_height = int(string_height)
            int_width = int(string_width)

        except ValueError:
            print("That is not a valid input. Please try again.")

        else:
            volume_of_rectangular_prism(int_base, int_height, int_width)
            break

    print("\nDone.")


if __name__ == "__main__":
    main()
