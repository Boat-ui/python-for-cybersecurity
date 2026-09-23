# Day 12: Error Handling

## What I Learned

- What errors are in Python.
- How errors can cause a program to crash.
- How `try` is used to run code that might produce an error.
- How `except` is used to handle an error.
- How to use `except ValueError` to specifically handle invalid number conversions.
- How error handling can make programs more reliable and user-friendly.

## Security Practice

I created a Python program that asks the user to enter the number of login attempts.

The program uses `try` and `except ValueError` to handle invalid input.

When a valid number is entered, the program records the number of attempts.

When invalid text is entered, the program displays an error message instead of crashing.

### **Assignment for Day 12**

**Safe Number Checker**

The program:

- Asks the user to enter a number of attempts.
- Converts the input into an integer.
- Uses `try` to attempt the conversion.
- Uses `except ValueError` to handle invalid input.
- Displays the recorded number when valid input is provided.
- Displays an error message when invalid input is provided.

This assignment helped me understand how Python programs can handle unexpected input safely instead of crashing.
