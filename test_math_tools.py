# test_math_tools.py
from math_tools import *

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("test_add: ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    print("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    print("test_is_even: ALL PASSED")

def test_subtract():
    # 1. Easy Task
    assert subtract(10, 5) == 5
    assert subtract(0, 7) == -7
    assert subtract(-3, -3) == 0
    print("test_subtract: ALL PASSED")

def test_max_of_three():
    # 3. Medium Task
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(10, 5, 2) == 10
    assert max_of_three(4, 9, 1) == 9
    assert max_of_three(5, 5, 2) == 5  # Two equal
    assert max_of_three(7, 7, 7) == 7  # All equal
    print("test_max_of_three: ALL PASSED")

def test_is_palindrome():
    # 4. Medium Task
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("a plan a canal panama") == True # Strings with spaces
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome("z") == True  # Single character
    assert is_palindrome("Racecar") == False # Case-sensitive
    print("test_is_palindrome: ALL PASSED")

def test_find_min():
    # 5. Hard Task
    assert find_min([5, 2, 9, 1]) == 1
    assert find_min([10, 20, 30]) == 10 # Catch min_val = 0 bug
    assert find_min([-5, -1, -10]) == -10
    print("test_find_min: ALL PASSED")

def test_remove_duplicates():
    # 6. Hard Task
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates([]) == [] # Empty list
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3] # No duplicates
    assert remove_duplicates([5, 5, 5]) == [5] # All duplicates
    assert remove_duplicates([1, "1"]) == [1, "1"] # Mixed types
    assert remove_duplicates(["apple", "banana", "apple"]) == ["apple", "banana"]
    print("test_remove_duplicates: ALL PASSED")

# Run all tests
if __name__ == "__main__":
    test_add()
    test_multiply()
    test_is_even()
    test_subtract()
    test_max_of_three()
    test_is_palindrome()
    test_find_min()
    test_remove_duplicates()
    print("--- All tests passed! ---")