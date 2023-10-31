import pytest
from Data import data
from Fibonacci import fibonacci_sequence


@pytest.mark.parametrize(**data.ELEMENT_FIBONACCI)
def test_get_element_fibonacci_sequence(index, value):
    assert fibonacci_sequence.get_element_fibonacci_sequence(index) == value, (
        f"ERROR! ({index}) element != {value}")