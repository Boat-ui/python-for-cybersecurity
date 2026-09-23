# Day 6: While Loops and Login Attempts

## What I Learned

- What a `while` loop is and how it repeatedly executes code while a condition is true.
- How to use a counter with a `while` loop.
- How to control how many times a loop runs.
- How to combine `while` loops with conditional statements.
- How to use `and` inside a loop condition.
- How loops can be used to repeatedly check login information.
- How to limit the number of password attempts.
- How Python can use loops to automate repeated security checks.

## Security Practice

I created a Python login checker that gives a user a limited number of password attempts.

The program repeatedly asks for a password while the password is incorrect and the maximum number of attempts has not been reached.

After the user enters the correct password, access is granted. If the maximum number of attempts is reached without the correct password, access is denied.

### **Assignment for Day 6**

**Security Login Attempt Checker**

The program:

- Asks the user for a username.
- Repeatedly asks for a password.
- Uses a `while` loop to control the login attempts.
- Limits the user to three password attempts.
- Uses a condition to determine whether the password is correct.
- Grants access when the correct password is provided.
- Denies access after the maximum number of failed attempts.
- Displays the username in the final security message.

This assignment helped me understand how loops can be used to automate repeated security checks and enforce limits on login attempts.
