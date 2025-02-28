#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: Feb 28, 2025
# This programs calculates the circumference of a circle

import constants


def main():
    # This give the user input for the radius
    radius = int(input("What is the radius of the circle? (cm) "))
    # This part of the code calculates the Circumference.
    print("Area is {}cm^2".format(constants.TAU * radius))


if __name__ == "__main__":
    main()
