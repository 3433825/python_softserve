# x = int(input("Введите x: "))
# y = int(input("Введите y: "))


def get_result_ternary_operator(x: int, y: int) -> str:
    """
    Function outputs a value depending on the values of x and y
    """
    result_string = str(
        "game over"
        if (x == 0 and y == 0)
        else x + y
        if x < y
        else 0
        if x == y
        else x - y
    )

    return result_string


if __name__ == "__main__":
    cases = ((1, 2, "3"), (2, 2, "0"), (3, 2, "1"), (0, 0, "game over"))
    for x, y, result in cases:
        assert get_result_ternary_operator(x, y) == result, f"ERROR"
