# Day 16: Functions with Structured Data

## What I Learned

- How to pass a dictionary into a function as a parameter.
- How a function can work with structured data.
- How to access dictionary values inside a function using keys.
- How a function can return a result based on information in a dictionary.
- How to loop through a list of dictionaries.
- How to pass each dictionary from a list into a function.
- How to separate the responsibilities of a loop and a function.
- How functions can make security analysis logic reusable.

## Security Practice

I created a Python program that analyzes the login attempts of multiple users.

The users are stored as dictionaries inside a list.

I created a `check_attempts()` function that receives one user dictionary and checks the user's number of login attempts.

The function returns either `Suspicious` or `Normal`.

A `for` loop then passes each user dictionary to the function and displays the username together with the returned result.

### **Assignment for Day 16**

**User Risk Analyzer**

The program:

- Stores multiple user records in a list of dictionaries.
- Creates a function that accepts one user dictionary.
- Uses the `"attempts"` key to access the user's login attempts.
- Returns `Suspicious` when the user has 3 or more attempts.
- Returns `Normal` when the user has fewer than 3 attempts.
- Loops through every user in the list.
- Passes each user to the analysis function.
- Displays each username and its security result.
- Displays a message when security monitoring is complete.

This assignment helped me understand how functions, dictionaries, and loops can work together to analyze structured security data in a reusable way.
