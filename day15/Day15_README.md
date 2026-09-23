# Day 15: Lists of Dictionaries

## What I Learned

- How lists and dictionaries can be used together.
- How a list can contain multiple dictionaries.
- How each dictionary can represent one user or record.
- How a `for` loop can go through a list of dictionaries one dictionary at a time.
- How to use dictionary keys to access information from each record.
- How to access values such as usernames, roles, and login attempts.
- How integers and strings are different when working with numerical comparisons.
- How to combine lists, dictionaries, loops, and conditional statements.

## Security Practice

I created a Python program that stores information about multiple users using a list of dictionaries.

Each user has a username, role, and number of login attempts.

The program loops through each user and checks their login attempts.

If a user has 3 or more login attempts, the program reports suspicious login activity.

Otherwise, it reports that the login activity is normal.

### **Assignment for Day 15**

**User Security Monitor**

The program:

- Stores multiple user records inside a list.
- Uses dictionaries to store information about each user.
- Loops through each user using a `for` loop.
- Displays information from each user's dictionary.
- Checks the number of login attempts.
- Identifies users with 3 or more attempts as suspicious.
- Reports normal activity for users with fewer than 3 attempts.
- Displays a message when security monitoring is complete.

This assignment helped me understand how Python can work with structured data containing multiple records, which is important when analyzing security events and user activity.
