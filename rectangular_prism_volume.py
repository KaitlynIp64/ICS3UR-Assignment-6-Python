#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program calculates volume of a rectangular prism


import random


def volume_of_rectangular_prism(int_length, int_width, int_height):
    # calculate area

    # process
    volume = int_length * int_width * int_height

    # output
    print("The volume of the rectangular prism is: {0}cm³.".format(volume))


def main():
    # input
    while True:
        string_length = input("Enter the length (cm): ")
        string_width = input("Enter the width (cm): ")
        string_height = input("Enter the height (cm): ")

        try:
            int_length = int(string_length)
            int_width = int(string_width)
            int_height = int(string_height)

        except ValueError:
            print("That is not a valid input. Please try again.")

        else:
            volume_of_rectangular_prism(int_length, int_width, int_height)
            break

    print("\nDone.")


if __name__ == "__main__":
    main()
