import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from app import app, items


@pytest.fixture
def client():
    with app.test_client() as client:
        items.clear()  
        yield client

def test_add_item_logic():
    items.clear()
    items.append('Item1')
    assert len(items) == 1
    assert items[0] == 'Item1'
