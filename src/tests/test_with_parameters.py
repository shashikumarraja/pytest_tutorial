import pytest

@pytest.mark.parametrize('num1, num2, expected', [(3,5,8)])
def test_sum(num1, num2, expected):
        assert sum(num1, num2) == expected