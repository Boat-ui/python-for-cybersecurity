# Day 21: Sorting Security Records

## What I Learned

Today I learned how to sort security records in Python.

I learned how to:

- Use Python's `sorted()` function.
- Sort numbers from smallest to largest.
- Use `reverse=True` to sort from largest to smallest.
- Sort a list of dictionaries based on a specific dictionary value.
- Use the `key` parameter to tell `sorted()` what value to use for sorting.
- Use a `lambda` expression with `sorted()` to access a dictionary value.
- Store the sorted records in a new list.

The main sorting pattern I learned was:

`sorted(users, key=lambda user: user["attempts"], reverse=True)`

This allowed me to arrange users according to their number of login attempts, with the highest number appearing first.

## Security Practice

I used the `security_users.txt` file containing usernames, roles, and login attempts.

The program:

1. Reads the security records from the file.
2. Converts each line into a dictionary.
3. Stores all users in the `users` list.
4. Sorts the users based on their login attempts.
5. Places the sorted records into a new `sorted_users` list.
6. Loops through the sorted users.
7. Displays each username and their number of attempts.
8. Prints the security monitoring completion message.

Sorting security records can help analysts quickly identify users or events with the highest activity and prioritize what needs further investigation.

### **Assignment for Day 21**

**Security Risk Sorter**

Build a Python program that:

- Reads users from `security_users.txt`.
- Builds a `users` list containing dictionaries.
- Sorts the users by login attempts.
- Sorts them from highest to lowest.
- Stores the sorted records in `sorted_users`.
- Loops through `sorted_users`.
- Displays each username and their number of attempts.
- Prints `Security monitoring complete`.

## Key Takeaway

Today I learned how sorting can make security data easier to analyze.

Instead of checking users in their original order, I can arrange them based on a security-related value such as login attempts. This makes records with higher activity easier to identify and review.
