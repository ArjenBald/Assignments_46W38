"""Script for Module 04 — Task 1."""

import sys
import MyModule  # Make sure MyModule.py is in the same folder as this script.

def main() -> int:
    try:
        numbers = MyModule.get_a_list_of_numbers()
    except ValueError as err:
        print(f"Error: {err}")
        return 1

    min_value = MyModule.find_min(numbers)
    max_value = MyModule.find_max(numbers)

    print(f"The list of numbers is: {numbers}")
    print(f"The minimal number is: {min_value}")
    print(f"The maximal number is: {max_value}")

    return 0

if __name__ == "__main__":
    sys.exit(main())