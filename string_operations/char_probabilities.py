from collections import Counter


def get_char_probabilities(input_string: str) -> dict:
    """
    Calculate probabilities of each character in the given string.

    Args:
    - input_string (str): The input string for which probabilities are calculated.

    Returns:
    - dict: A dictionary where keys are characters and values are their probabilities in the input string.
    """
    char_count = len(input_string)
    char_probabilities = {
        char: round(input_string.count(char) / char_count, 2)
        for char in set(input_string)
    }

    return char_probabilities


def get_char_probabilities_with_counter(text) -> dict:
    """
        Calculate probabilities of each character in the given string with
        Counter.

    Args:
    - input_string (str): The input string for which probabilities are calculated.

    Returns:
    - dict: A dictionary where keys are characters and values are their probabilities in the input string.
    """
    text_len = len(text)
    return {key: round(value / text_len, 2) for key, value in Counter(text).items()}


# if __name__ == "__main__":
#     input_str = "демонстрація виконання домашнього завдання до першої лекції"
#     probabilities = get_char_probabilities(input_str)
#     for item in probabilities.items():
#         print(item)
