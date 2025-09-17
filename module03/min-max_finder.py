"""
min-max_finder.py

This script reads a list of numbers from user input,
then finds the minimal and maximal numbers manually,
without using the built-in min() or max() functions.
"""

numbers = []
print("Enter numbers. You can:")
print("- type them one by one (type 'end' to finish), OR")
print("- type several numbers separated by spaces in one line.")

while True:
    user_input = input("Enter a number (or 'end' to stop): ")

    if user_input.lower() == "end":
        break

    # Case 1: several numbers in one line
    if " " in user_input:
        parts = user_input.split()
        for part in parts:
            numbers.append(float(part))
        continue

    # Case 2: single number
    numbers.append(float(user_input))

# Handle empty list
if not numbers:
    min_val = None
    max_val = None
else:
    # Find minimum
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num

    # Find maximum
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num

# Print results
print(f"\nThe list of numbers is: {numbers}")
print(f"The minimal number is: {min_val}")
print(f"The maximal number is: {max_val}")