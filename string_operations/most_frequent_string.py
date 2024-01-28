from collections import Counter


def most_frequent_string(sequence, place):
    # Use Counter to count occurrences of each string in the sequence
    string_counter = Counter(sequence)

    # Use most_common(1) to get the most frequently occurring string
    most_common_string = string_counter.most_common(place)

    # Extract the string from the result
    if most_common_string:
        result = most_common_string[place - 1][0]
        return result
    else:
        # Handle the case when the sequence is empty
        return None


example_string = ["a", "b", "c", "a", "b", "a"]
print(most_frequent_string(example_string, 1))
