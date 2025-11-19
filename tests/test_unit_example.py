import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app, items
import pytest

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
