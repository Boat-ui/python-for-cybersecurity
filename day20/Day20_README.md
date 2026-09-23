# Day 20: Filtering Security Records

## What I Learned

Today I learned how to filter records in Python.

Filtering means going through a collection of records and selecting only the records that meet a specific condition.

I learned how to:

- Loop through a list of dictionaries.
- Check a condition for each record.
- Use `if` to identify records that meet the condition.
- Create a separate empty list to store matching records.
- Use `.append()` to add matching dictionaries to the new list.
- Count matching records using a counter.
- Understand the difference between **counting** records and **collecting** records.

The main condition used today was:

`user["attempts"] >= 3`

This allowed me to identify users with suspicious login activity.

## Security Practice

I worked with a security user file containing usernames, roles, and login attempts.

The program:

1. Reads the security records from `security_users.txt`.
2. Converts each line into a dictionary.
3. Stores all users in a `users` list.
4. Loops through all users.
5. Checks whether each user has 3 or more login attempts.
6. Prints users with suspicious activity.
7. Stores suspicious users in a separate list.
8. Counts the number of suspicious users.
9. Displays the final security monitoring message.

This is useful in cybersecurity because security analysts often need to filter large amounts of data and focus only on records that meet certain conditions.

### **Assignment for Day 20**

**Security User Filter**

Build a Python program that:

- Reads users from `security_users.txt`.
- Builds a `users` list containing dictionaries.
- Creates an empty `suspicious_user` list.
- Loops through every user.
- Checks whether the user's login attempts are greater than or equal to 3.
- Prints users with suspicious activity.
- Adds suspicious users to the `suspicious_user` list.
- Counts the total number of suspicious users.
- Displays the total number of suspicious users.
- Prints `Security monitoring complete`.

## Key Takeaway

Today I learned that filtering allows me to select specific records from a larger collection based on a condition.

I also learned that I can both **collect** matching records in a new list and **count** how many matching records there are.

This is an important concept for future cybersecurity tasks such as filtering logs, alerts, users, network events, and other security data.
