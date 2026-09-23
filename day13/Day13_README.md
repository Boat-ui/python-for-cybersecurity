# Day 13: Error Handling with Loops

## What I Learned

- How to combine `while` loops with `try` and `except`.
- How `while True` can keep a program running until a condition is met.
- How `break` stops a loop immediately.
- How `ValueError` can be handled when converting invalid input to an integer.
- How to repeatedly ask for valid input instead of allowing the program to crash.
- How to combine error handling, loops, and conditional statements.

## Security Practice

I created a Python program that checks the number of failed login attempts.

The program keeps asking for the number of attempts until valid numerical input is provided.

Invalid input is handled using `try` and `except ValueError`.

After receiving a valid number, the program checks whether the number of failed attempts is 3 or more.

If it is 3 or more, the program reports that the account may be under attack.

Otherwise, it reports that the login activity appears normal.

### **Assignment for Day 13**

**Safe Login Attempt Counter**

The program:

- Uses a `while` loop to repeatedly request input.
- Uses `try` to attempt integer conversion.
- Uses `except ValueError` to handle invalid input.
- Uses `break` to exit the loop after valid input is received.
- Checks the number of failed login attempts.
- Identifies potentially suspicious login activity.
- Displays a message when the log analysis is complete.

This assignment helped me understand how error handling can be combined with loops to make security programs more reliable when dealing with unexpected input.
