# Day 18: Counting Suspicious Users

## What I Learned

- How to use counters when analyzing security data.
- How to initialize a counter at `0`.
- How to increase a counter when a specific condition is met.
- How to use a function to analyze each user.
- How to combine functions, loops, conditions, and counters.
- How to count suspicious users while processing structured security data.
- Why the counter is updated inside the loop.
- Why the final count is displayed outside the loop.

## Security Practice

I created a Python program that reads structured user security data from a file.

The program converts each line into a dictionary and stores the dictionaries inside a list.

I used a `check_attempt()` function to determine whether each user's login activity was suspicious or normal.

I then used a counter to keep track of the total number of suspicious users.

The program displays each user's security status and provides a final count of suspicious users.

### **Assignment for Day 18**

**Security Alert Counter**

The program:

- Reads user security records from a file.
- Converts each record into a dictionary.
- Stores the dictionaries in a list.
- Uses a function to analyze login attempts.
- Loops through every user.
- Identifies suspicious users.
- Uses a counter to count suspicious users.
- Displays each user's security status.
- Displays the total number of suspicious users.
- Prints a message when security monitoring is complete.

This assignment helped me understand how Python can process multiple security records and produce useful summary information instead of only analyzing individual records.
