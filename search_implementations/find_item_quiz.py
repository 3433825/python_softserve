def find_item(sequence: list, item):
    # Returns True if the item is in the list, False if not.
    if len(sequence) == 0:
        return False

#     sequence.sort()
    left = 0
    right = len(sequence) - 1
    while left <= right:
        # Is the item in the center of the list?
        middle = (left + right) // 2
        if sequence[middle] == item:
            return True
        # Is the item in the first half of the list?
        elif item < sequence[middle]:
            # Call the function with the first half of the list
            right = middle - 1
        elif item > sequence[middle]:
            # Call the function with the second half of the list
            left = middle + 1

    return False


# Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]
list_of_names.sort()

print(find_item(list_of_names, "Alex"))  # True
print(find_item(list_of_names, "Andrew"))  # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False