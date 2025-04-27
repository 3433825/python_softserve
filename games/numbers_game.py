#!usr/bin/env python3

import random


def game_numbers():
    keep_going = "y"
    print()
    print("Ich schlage vor, Zahlen zu spielen")
    print()
    while keep_going == "y":
        alex_turn = input(
            # 'Alex, are you in game? Type "y" or "n", please, and then type Enter:'
            'Alex, Willst du spielen? Drücken Sie bitte "y" oder "n" und dann "Enter"'
        )
        print()
        emilia_turn = input(
            'Emilia, Willst du spielen? Drücken Sie bitte "y" oder "n" und dann "Enter":'
        )

        if alex_turn == "y" and emilia_turn == "y":
            alex_number = random.randint(1, 100)
            emilia_number = random.randint(1, 100)
            print()
            print(f"Alex: {alex_number}\n \nEmilia: {emilia_number}")
            print()

            if alex_number > emilia_number:
                print("Alex WON")
                print()
            else:
                print("Emiliya WON")
                print()

        keep_going = input(
            'Sollen wir noch einmal spielen? Drücken Sie bitte "y" oder "n" und dann "Enter"'
        )


if __name__ == "__main__":
    game_numbers()
