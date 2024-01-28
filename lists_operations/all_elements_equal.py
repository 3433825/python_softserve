def are_all_elements_equal(sequence):
    # Check if all elements are equal using the 'all' function
    return all(element == sequence[0] for element in sequence)


sequence_same_elements = [1, 1, 1, 1]
sequence_diff_elements = [1, 1, 1, 2]
result_same = are_all_elements_equal(sequence_same_elements)
print(result_same)
result_diff = are_all_elements_equal(sequence_diff_elements)
print(result_diff)
