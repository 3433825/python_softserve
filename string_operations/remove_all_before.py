def remove_elements_before(sequence, cutting_element):
    # If the sequence is empty, return an empty sequence
    if not sequence:
        return sequence

    # Find the index of the cutting element in the sequence
    try:
        index = sequence.index(cutting_element)
    except ValueError:
        # If the cutting element is not found, return the original sequence
        return sequence

    # Remove elements before the cutting element
    result_sequence = sequence[index:]

    return result_sequence
