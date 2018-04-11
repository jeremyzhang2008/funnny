import pytest
import davehello as dh

def test_greet():
    assert dh.greet() == 'hello, world!'