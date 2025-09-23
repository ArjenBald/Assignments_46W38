"""MyModule: reusable utilities for Module 04 — Task 1.

Functions:
- get_a_list_of_numbers(): Prompt the user for numbers until 'end', return a list of floats.
- find_min(list_of_numbers): Return minimal number or None for empty list.
- find_max(list_of_numbers): Return maximal number or None for empty list.
"""

from typing import List, Optional

def get_a_list_of_numbers(prompt: str = "Enter a number (or 'end' to stop): ") -> List[float]:
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
    if not list_of_numbers:
        return None
    return min(list_of_numbers)


def find_max(list_of_numbers: List[float]) -> Optional[float]:
    if not list_of_numbers:
        return None
    return max(list_of_numbers)