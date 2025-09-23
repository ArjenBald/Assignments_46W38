"""MyModule: reusable utilities for Module 04 — Task 1 and Task 2.


Functions:
- get_a_list_of_numbers(): Prompt the user for numbers until 'end'.
- find_min(list_of_numbers): Return minimal number or None.
- find_max(list_of_numbers): Return maximal number or None.
- find_average(list_of_numbers): Return arithmetic mean or None for empty list.
- find_median(list_of_numbers): Return median or None for empty list.
"""


from typing import List, Optional




def get_a_list_of_numbers(prompt: str = "Enter a number (or 'end' to stop): ") -> List[float]:
"""
Interactively collect numbers from the user using input().


The user is asked to type one number per prompt; typing 'end' (any case) finishes the input.
If the user provides something that is not a valid number string and not 'end',
the function raises a ValueError.
"""
numbers: List[float] = []


while True:
raw = input(prompt).strip()
if raw.lower() == "end":
break
try:
number = float(raw)
except ValueError as exc:
raise ValueError(f"Invalid input: {raw!r}. Please enter a number or 'end'.") from exc
numbers.append(number)


return numbers




def find_min(list_of_numbers: List[float]) -> Optional[float]:
"""Return the minimal number in the list, or None for an empty list."""
if not list_of_numbers:
return None
return min(list_of_numbers)




def find_max(list_of_numbers: List[float]) -> Optional[float]:
"""Return the maximal number in the list, or None for an empty list."""
if not list_of_numbers:
return None
return max(list_of_numbers)




def find_average(list_of_numbers: List[float]) -> Optional[float]:
"""Return the arithmetic mean of the list, or None for an empty list."""
if not list_of_numbers:
return None
return sum(list_of_numbers) / len(list_of_numbers)


return sorted_list[mid]