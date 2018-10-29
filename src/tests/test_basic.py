import pytest
from .. import sum

#make sure to start function name with test
def test_sum():
    assert sum(1, 2) == 3