import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest


@pytest.fixture
def add(a, b):
    return a + b

def test_add_integration_positive():
    result = add(10, 5)
    assert result == 15

def test_add_integration_negative():
    result = add(-10, -5)
    assert result == -15

def test_add_integration_mixed():
    result = add(10, -5)
    assert result == 5
