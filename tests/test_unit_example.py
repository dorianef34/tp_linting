import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from app import add_numbers


@pytest.fixture

def test_add_positive_numbers():
    assert add_numbers(2, 3) == 5

def test_add_negative_numbers():
    assert add_numbers(-2, -3) == -5

def test_add_mixed_numbers():
    assert add_numbers(-2, 3) == 1

def test_add_zeros():
    assert add_numbers(0, 0) == 0
