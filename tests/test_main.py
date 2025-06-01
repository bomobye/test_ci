# tests/test_main.py

from app.main import add, subtract

def test_add():
    assert add(3, 5) == 8

def test_subtract():
    assert subtract(10, 5) == 5
