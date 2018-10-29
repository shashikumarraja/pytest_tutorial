import pytest
from ..sum import *

#make sure to start function name with test
def test_1():
    assert sum(1, 2) == 3

def test_2():
    assert type(sum(1, 2)) is int