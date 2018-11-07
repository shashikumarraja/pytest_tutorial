import pytest
from hypothesis import given, settings, Verbosity, example
import hypothesis.strategies as st
from ..sum import *

@given(st.integers(), st.integers())
def test_sum_basic(num1, num2):
    assert sum(num1, num2) == num1 + num2

@given(st.integers(), st.integers())
@example(1, 2)
def test_sum_basic_with_example(num1, num2):
    assert sum(num1, num2) == num1 + num2

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_sum_with_property(num1, num2):
    assert sum(num1, num2) == num1 + num2
    # Test Identity property
    assert sum(num1, 0) == num1
    # Test Commutative property
    assert sum(num1, num2) == sum(num2, num1)

@given(st.integers(), st.integers())
def test_sum_with_shrinking_example(num1, num2):
    assert sum(num1, num2) == num1 + num2
    # Test Identity property
    assert sum(num1, 0) == num1
    # Test Commutative property
    assert sum(num1, num2) == sum(num2, num1)
    assert num1 <= 30