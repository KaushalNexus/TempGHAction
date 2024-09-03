from src.app import add, mul
import pytest


def test_add():
    assert add(2,3)==5
    assert add(-1, 1)==0
    assert add(9, 8)==17

def test_mul():
    assert mul(1, 1)==1
    assert mul(3, 4)==12
    assert mul(-1, 1)==-1
    
