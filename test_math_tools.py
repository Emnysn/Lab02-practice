# test_math_tools.py
from math_tools import add, multiply, is_even, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    print("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even: ALL PASSED")

def test_subtract():
    # Easy task: at least 3 assert statements
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(-3, -3) == 0
    print("test_subtract: ALL PASSED")

# Run all tests
test_add()
test_multiply()
test_is_even()
test_subtract()
print("--- All tests passed! ---")