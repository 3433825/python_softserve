def test_comparison_is_even_methods():
    even_numbers = (x for x in range(0, 2000000, 2))
    for number in even_numbers:
        assert number % 2 == int(bin(number)[-1])