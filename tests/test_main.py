''' My Calculator Tests'''
import pytest
from app.main import addition, division, multiplication, subtraction

def test_addition():
    '''Addition Function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''Subtraction Function'''
    assert subtraction(1,1) == 0
def test_multiplication():
    '''Multiplication Function'''
    assert multiplication(1,2) == 2
def test_positive_division ():
    '''Positive Division Test'''
    assert division(1,1) == 1
def test_negative_divison():
    '''Negative Division Test'''
    with pytest.raises(ZeroDivisionError):
        division(10,0)
