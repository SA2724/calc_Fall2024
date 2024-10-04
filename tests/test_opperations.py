"""
This module contains unit tests for basic arithmetic operations
(addition, subtraction, multiplication, and division) defined in
app.Operations.
"""

import pytest
from app.Opperations import addition, division, multiplication, subtraction

# Fixture for test data
@pytest.fixture
def test_data():
    '''Provides test data for addition, subtraction, and multiplication.'''
    return {
        "addition": (1, 1, 2),
        "subtraction": (1, 1, 0),
        "multiplication": (1, 2, 2)
    }

# Parameterized test for addition, subtraction, and multiplication
@pytest.mark.parametrize("operation, a, b, expected", [
    (addition, 1, 1, 2),
    (subtraction, 1, 1, 0),
    (multiplication, 1, 2, 2)
])
def test_operations(operation, a, b, expected):
    '''Tests addition, subtraction, and multiplication operations.'''
    assert operation(a, b) == expected

# Parameterized test for division
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),   # Normal case
])
def test_positive_division(a, b, expected):
    '''Tests positive division cases where b != 0.'''
    assert division(a, b) == expected

# Test for division by zero
def test_negative_division():
    '''Tests division by zero, expecting a ZeroDivisionError.'''
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
