import pytest
from ..sum import *

class TestSum(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_sum_example_with_class(self):
        assert sum(1, 2) == 3

    @classmethod
    def teardown_class(cls):
        pass