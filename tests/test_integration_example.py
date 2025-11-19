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

def test_index_page_contains_items_title(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Items' in response.data

def test_add_item_endpoint(client):
    response = client.post(
        '/add', 
        data={'item': 'Test Item'}, 
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'Test Item' in response.data
    assert 'Test Item' in items

def test_delete_item_endpoint(client):
    items.append('Delete Me')
    response = client.get('/delete/0', follow_redirects=True)
    assert response.status_code == 200
    assert b'Delete Me' not in response.data
    assert 'Delete Me' not in items

def test_update_item_endpoint(client):
    items.append('Old Item')
    response = client.post(
        '/update/0', 
        data={'new_item': 'Updated Item'}, 
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'Updated Item' in response.data
    assert items[0] == 'Updated Item'
