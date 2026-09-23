# Day 19: Finding the Highest-Risk User

## What I Learned

- How to track the highest value while looping through data.
- How to initialize a variable to store the highest value.
- How to compare the current user's value with the highest value found so far.
- How to update the highest value when a larger value is found.
- How to track the username associated with the highest value.
- How to combine value tracking with functions, loops, dictionaries, and conditions.
- How this technique can be used to identify the highest-risk user in security data.

## Security Practice

I created a Python program that reads structured user security data from a file.

The program converts each record into a dictionary and stores the dictionaries inside a list.

I used a `check_attempt()` function to classify each user's login activity as suspicious or normal.

I also created variables to track the highest number of login attempts and the username associated with that value.

The program loops through every user and updates the highest value whenever a user has more login attempts than the current highest value.

At the end, the program displays the user with the highest number of login attempts and their total attempts.

### **Assignment for Day 19**

**Highest-Risk User Analyzer**

The program:

- Reads user security records from a file.
- Converts each record into a dictionary.
- Stores the dictionaries in a list.
- Uses a function to analyze login attempts.
- Loops through every user.
- Identifies suspicious users.
- Tracks the highest number of login attempts.
- Tracks the username associated with the highest number of attempts.
- Displays each user's security status.
- Displays the highest-risk user and their number of attempts.
- Prints a message when security monitoring is complete.

This assignment helped me understand how Python can compare values while processing multiple security records and identify the record with the highest value.
