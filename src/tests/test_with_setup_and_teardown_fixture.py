import pytest
from ..sum import *

@pytest.fixture(scope='session')
def get_sum_test_data():
        return [(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]

@pytest.fixture(autouse=True)
def setup_and_teardown():
        #setup part 
        print '\nFetching data from db'
        yield
        #teardown part
        print '\nSaving test run data in db'

def test_sum_with_setup_and_teardown_fixture(get_sum_test_data):
        for data in get_sum_test_data:
                num1 = data[0]
                num2 = data[1]
                expected = data[2]
                assert sum(num1, num2) == expected