import pytest
from ..sum import *

@pytest.fixture
def get_sum_test_data():
        return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]
def test_sum_with_fixture(get_sum_test_data):
        for data in get_sum_test_data:
                num1 = data[0]
                num2 = data[1]
                expected = data[2]
                assert sum(num1, num2) == expected