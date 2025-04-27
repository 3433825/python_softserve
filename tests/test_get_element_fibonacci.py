import pytest
from Data import data
from Fibonacci import fibonacci_sequence


@pytest.mark.parametrize(**data.ELEMENT_FIBONACCI)
def test_get_element_fibonacci_sequence(get_logger, index, value):
    get_logger.info('test_get_element_fibonacci_sequence')
    element_fibonacci_sequence = fibonacci_sequence.get_element_fibonacci_sequence(index)
    assert element_fibonacci_sequence == value, (f"ERROR! ({index}) element != {value}")
