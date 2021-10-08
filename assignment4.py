#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Oct 2021
# This program is assignment 4


def main():
    # This is the assignment 4 function

    price = 100
    total = 0

    # Input
    items = input("How many units would you like: ")
    print("")

    # Process and Output
    try:
        units = int(items)
        if units >= 1000:
            final_price = price - (price * 0.1)
        else:
            final_price = price
        sub_total = units * final_price
        total = sub_total * 1.13
        print("The total is ${0:,.2f}".format(total))
    except Exception:
        print("Invalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
