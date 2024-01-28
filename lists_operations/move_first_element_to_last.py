def move_first_element_to_last(sequence):
    # If the sequence is empty or has only one element, return the sequence unchanged
    if len(sequence) <= 1:
        return sequence

    # Move the first element to the end
    result = sequence[1:] + [sequence[0]]

    return result
