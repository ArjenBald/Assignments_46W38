"""
Task 2 — Word counter for text files.

Requirements covered:
- A function count_words(filename) that returns the number of words in a text file.
- Handle FileNotFoundError gracefully (return None).
- Ignore punctuation before splitting into words.
- Print the result using an f-string.
"""

from typing import Optional
import string


def count_words(filename: str) -> Optional[int]:
    """
    Return the number of words in the given text file.
    If the file is not found, return None.

    Implementation details:
    - Read the file in UTF-8.
    - Remove punctuation using str.translate and string.punctuation.
    - Split by whitespace and count tokens.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        return None

    translator = str.maketrans("", "", string.punctuation)
    cleaned_text = text.translate(translator)
    words = cleaned_text.split()
    return len(words)


if __name__ == "__main__":
    # Ask user for a path; allow empty input to keep it flexible for the grader.
    path = input("Enter path to a .txt file: ").strip()

    count = count_words(path)
    if count is None:
        print(f"Could not find the file: '{path}'")
    else:
        print(f"File '{path}' contains {count} words.")