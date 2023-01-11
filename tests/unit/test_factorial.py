import pytest
from factorial_example.core import calculate_factorial

pytestmark = pytest.mark.timeout(1)

@pytest.mark.timeout(5)
def test_calculate_factorial_valid():
    factorial = calculate_factorial(num=5, delay=10)
    assert factorial == 120


@pytest.mark.timeout(1)
def test_calculate_factorial_invalid():
    with pytest.raises(ValueError):
        factorial = calculate_factorial(num=-1, delay=10)
