import pytest
from hello import greet

def test_greeing():
    assert greet("mangesh") == "Hello, Mangesh"