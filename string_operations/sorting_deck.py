# deck_tuple = [
#     ("♢", "K"),
#     ("♣", "10"),
#     ("♣", "J"),
#     ("♡", "9"),
#     ("♢", "J"),
#     ("♠", "K"),
#     ("♣", "5"),
#     ("♡", "10"),
#     ("♢", "Q"),
#     ("♢", "3"),
#     ("♡", "Q"),
#     ("♣", "7"),
#     ("♡", "5"),
# ]

deck_tuple = [
    "♢K",
    "♣10",
    "♣J",
    "♡9",
    "♢J",
    "♠K",
    "♣5",
    "♡10",
    "♢Q",
    "♢3",
    "♡Q",
    "♣7",
    "♡5",
]

# deck_sorted = sorted(deck_tuple, key=lambda x: (x[0], x[1]))
deck_sorted = sorted(deck_tuple, key=lambda x: (x[0]))
for item in deck_sorted:
    print(item)
