# CSP-Python-Module-7
Code Refactoring 

This project is a refactored version of a Python script that originally worked but was hard to read. I improved the names, added documentation, and simplified the code without changing what it does.

What the Program Does

The script has two functions:

process_numbers doubles even numbers and triples odd numbers in a list.
format_words turns words longer than 5 letters into uppercase, turns shorter words into lowercase, and joins them into one string.
How to Run It
Make sure Python 3 is installed.
Download undocumented_script.py.
Run this command in your terminal:
python undocumented_script.py
Expected Output
Processed Numbers: [3, 4, 9, 8, 15, 12, 21]
Processed Strings: apple BANANA kiwi GRAPEFRUIT CHERRY
Files in This Repository
File	Description
undocumented_script.py	The refactored and documented Python script
CODE_REVIEW.md	My review of the code before and after refactoring
DECISIONS.md	An explanation of the choices I made while refactoring
Improvements Made
Renamed functions and variables to clear, descriptive names (PEP 8)
Added docstrings to every function (PEP 257)
Replaced loops with a list comprehension and join()
Replaced a hard-coded number with the named constant LONG_WORD_THRESHOLD
Added a comment that explains why, not just what

https://youtu.be/N6c2ogSy7co
