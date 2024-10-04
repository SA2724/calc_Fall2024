from typing import Literal
import pytest
from app.Calculation import Addition, Subtraction, Multiplication, Division  # Assuming your classes are in 'calculation' module

# Parameterized test for Addition with __str__ and __repr__ checks
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2), (2, 3, 5), (-1, -1, -2), (0, 0, 0)
])
def test_addition(a: Literal[1] | Literal[2] | Literal[-1] | Literal[0], b: Literal[1] | Literal[3] | Literal[-1] | Literal[0], expected: Literal[2] | Literal[5] | Literal[-2] | Literal[0]):
    '''Test for addition operation'''
    operation = Addition.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Addition: {a} + {b} = {expected}"
    assert repr(operation) == f"Addition(a={a}, b={b}, result={expected})"

# Parameterized test for Subtraction with __str__ and __repr__ checks
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0), (5, 3, 2), (-1, -1, 0), (0, 5, -5)
])
def test_subtraction(a: Literal[1] | Literal[5] | Literal[-1] | Literal[0], b: Literal[1] | Literal[3] | Literal[-1] | Literal[5], expected: Literal[0] | Literal[2] | Literal[-5]):
    '''Test for subtraction operation'''
    operation = Subtraction.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Subtraction: {a} - {b} = {expected}"
    assert repr(operation) == f"Subtraction(a={a}, b={b}, result={expected})"

# Parameterized test for Multiplication with __str__ and __repr__ checks
@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4), (3, 5, 15), (0, 5, 0), (-1, 1, -1)
])
def test_multiplication(a: Literal[2] | Literal[3] | Literal[0] | Literal[-1], b: Literal[2] | Literal[5] | Literal[1], expected: Literal[4] | Literal[15] | Literal[0] | Literal[-1]):
    '''Test for multiplication operation'''
    operation = Multiplication.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Multiplication: {a} * {b} = {expected}"
    assert repr(operation) == f"Multiplication(a={a}, b={b}, result={expected})"

# Parameterized test for Division with __str__ and __repr__ checks
@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 1), (10, 5, 2), (9, 3, 3), (7, 2, 3.5)
])
def test_division(a: Literal[2] | Literal[10] | Literal[9] | Literal[7], b: Literal[2] | Literal[5] | Literal[3], expected: float | Literal[1] | Literal[2] | Literal[3]):
    '''Test for division operation'''
    operation = Division.create(a, b)
    assert operation.compute() == expected
    assert str(operation) == f"Division: {a} / {b} = {expected}"
    assert repr(operation) == f"Division(a={a}, b={b}, result={expected})"

# Test for division by zero exception
def test_division_by_zero_exception():
    '''Test for division by zero exception'''
    operation = Division.create(10, 0)
    with pytest.raises(ZeroDivisionError):
        operation.compute()