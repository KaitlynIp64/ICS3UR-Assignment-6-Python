#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Dec 2022
# This program calculates volume of a rectangular prism


import random


def volume_of_rectangular_prism(int_length, int_width, int_height):
    # calculate area

    # process
    volume = int_length * int_width * int_height

    return volume_of_rectangular_prism


def main():
    # input
    string_length = input("Enter the length of the rectangular prism (cm): ")
    string_width = input("Enter the width of the rectangular prism (cm): ")
    string_height = input("Enter the height of the rectangular prism (cm): ")

    try:
        int_length = int(string_length)
        int_width = int(string_width)
        int_height = int(string_height)

        volume = volume_of_rectangular_prism(int_length, int_width, int_height)
        print("The volume of the rectangular prism is: {0}cm³.".format(volume))

    except ValueError:
        print("That is not a valid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
