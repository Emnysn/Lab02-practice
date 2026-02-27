# math_tools.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

# 1. Easy Task: Subtraction
def subtract(a, b):
    return a - b

# 3. Medium Task: Max of Three
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# 4. Medium Task: Is Palindrome
def is_palindrome(s):
    # Ignoring spaces, case-sensitive
    clean_s = s.replace(" ", "")
    return clean_s == clean_s[::-1]

# 5. Hard Task: Find Min
def find_min(numbers):
    if not numbers:
        return None
    # Initialize with first element to avoid the "min_val = 0" bug
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

# 6. Hard Task: Remove Duplicates
def remove_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen