#!usr/bin/env python3

import random


def game_numbers():
    keep_going = "y"
    while keep_going == "y":
        print()
        alex_turn = input(
            'Alex, are you in game? Type "y" or "n", please, and then type Enter:'
        )
        # emilia_turn = input('Emilia, are you in game? Type "y" or "n", please, and then type Enter:')

        if alex_turn == "y":  # and emilia_turn == 'y':
            alex_number = random.randint(1, 100)
            emilia_number = random.randint(1, 100)
            # print(f"Alex: {alex_number}, Emilia: {emilia_number}")
            print(f"Alex: {alex_number}, My Number: {emilia_number}")

            if alex_number > emilia_number:
                print("Alex WON")
            else:
                print("I WON")

        keep_going = input(
            'We are still going on? Type "y" or "n", please, and then type Enter:'
        )


if __name__ == "__main__":
    game_numbers()
