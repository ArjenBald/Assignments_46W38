#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mini syntax tour: comments, docstrings, PEP 8, identifiers, indentation, line continuation,
functions, and a simple 'main' entry point.
"""

# ======================================================================
# 1. COMMENTS & DOCUMENTATION
# ======================================================================

"""
Multi-line strings are used for module/function docstrings or long comments.
"""

'''
Triple single quotes work the same way.
'''

# ======================================================================
# 2. IDENTIFIERS & PEP 8 NAMING CONVENTIONS
# ======================================================================
# Variables: snake_case
user_name = "Alice"

# Constants: UPPER_CASE
MAX_CONNECTIONS = 5

length = 10
width = 5
area = length * width
print(f'Area is {area}')

# Functions: snake_case
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle using double quotes."""
    return length * width

def calculate_perimeter(length: float, width: float) -> float:
    '''Calculate the perimeter of a rectangle using single quotes.'''
    return 2 * (length + width)

# ======================================================================
# 3. IDENTIFIER RULES
# ======================================================================
second_value = 5  # cannot start with a number (so not "2nd_value")

first_name = "Alice"
First_name = "Bob"      # different from first_name (case-sensitive)
FIRST_NAME = "Charlie"  # another different variable

print(f"first_name: {first_name}")
print(f"First_name: {First_name}")
print(f"FIRST_NAME: {FIRST_NAME}")

# only letters, numbers, underscores:
user_id = "12345"
# user-id = "12345"  # bad
# class = "Math"     # bad: 'class' is a keyword
class_name = "Math"

# ======================================================================
# 4. INDENTATION (CRITICAL SYNTAX)
# ======================================================================
if second_value > 3:
    print("The value is greater than 3")
    if second_value > 10:
        print("The value is also greater than 10")
else:
    print("The value is 3 or less")

# ======================================================================
# 5. LINE CONTINUATION
# ======================================================================
total_sum = (second_value +
             len(user_name) +
             MAX_CONNECTIONS)

year = 2025; month = 9; day = 1
hour = 22; minute = 30; second = 30

if 1900 < year < 2100 and 1 <= month <= 12 \
     and 1 <= day <= 31 and 0 <= hour < 24 \
     and 0 <= minute < 60 and 0 <= second < 60:
    print("It is a valid date.")

favorite_colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple"
]

# ======================================================================
# 6. PUTTING IT ALL TOGETHER
# ======================================================================
from typing import Sequence, Any, List

def process_data(input_data: Sequence[Any], max_items: int = 10) -> List[Any]:
    '''
    Process data with a docstring using single quotes.

    Args:
        input_data: Data to process (sequence)
        max_items: Maximum items to process

    Returns:
        A new list with the first max_items elements.
    '''
    # example: list comprehension to clone slice as list
    return [item for item in input_data[:max_items]]

# ======================================================================
# 7. EXAMPLE USAGE
# ======================================================================
def main() -> None:
    # show geometry helpers from one place
    rect_area = calculate_area(5, 3)
    rect_perimeter = calculate_perimeter(5, 3)
    print(f"Perimeter: {rect_perimeter}")
    print(f"Area (via function): {rect_area}")

    # demonstrate docstrings
    print("\nDocstrings:")
    print("calculate_area docstring:", calculate_area.__doc__)
    print("calculate_perimeter docstring:", calculate_perimeter.__doc__)

    # use process_data on favorite_colors
    top3 = process_data(favorite_colors, max_items=3)
    print(f"\nFirst 3 favorite colors (processed): {top3}")

if __name__ == "__main__":
    main()