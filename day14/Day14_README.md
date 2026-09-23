# Day 14: Multiple Conditions and Boolean Input

## What I Learned

- How to use multiple conditions in Python.
- The difference between `and` and `or`.
- How `and` requires both conditions to be true.
- How `or` requires at least one condition to be true.
- How to use `if`, `elif`, and `else` together.
- The difference between a Boolean value and a string.
- How `input()` returns user input as a string.
- How to convert a `"True"` or `"False"` response into a Boolean through a comparison.

## Security Practice

I created a Python program that analyzes login activity using the number of login attempts and whether an IP address is suspicious.

The program uses multiple conditions to classify the activity as high risk, suspicious, or normal.

High risk activity is detected when there are at least 3 attempts and the IP address is suspicious.

Suspicious activity is detected when either there are at least 3 attempts or the IP address is suspicious.

### **Assignment for Day 14**

**Suspicious Login Detector**

The program:

- Asks the user for the number of login attempts.
- Asks whether the IP address is suspicious.
- Uses `and` to identify high-risk activity.
- Uses `or` to identify suspicious activity.
- Uses `if`, `elif`, and `else` to classify the login activity.
- Handles the difference between string input and Boolean values.
- Displays a message when the login detection is complete.

This assignment helped me understand how multiple security indicators can be combined to make more meaningful decisions in a security program.
