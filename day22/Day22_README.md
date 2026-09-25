# Day 22: Searching Security Records

## What I Learned

Today I learned how to search through a list of security records and find a specific user.

I learned how to:

- Search through a list of dictionaries using a `for` loop.
- Compare a dictionary value with user input.
- Use a variable to store a matching record.
- Use `None` to represent a value that has not been found.
- Check whether a record was found using `is not None`.
- Access information from the dictionary after finding a matching user.
- Handle the case where a requested user does not exist.

The main search condition was:

`user["username"] == search_user`

This compares the username stored in each dictionary with the username entered by the user.

I also learned that `found_user` contains the entire dictionary when a match is found, while `found_user["username"]` contains only the username.

## Security Practice

I used the `security_users.txt` file containing usernames, roles, and login attempts.

The program:

1. Reads the security records from the file.
2. Converts each line into a dictionary.
3. Stores all users in the `users` list.
4. Asks the user which username they want to search for.
5. Loops through the users.
6. Checks whether each username matches the search value.
7. Stores the matching dictionary in `found_user`.
8. Displays the user's username, role, and login attempts when found.
9. Displays `User not found` when there is no matching record.
10. Prints the security search completion message.

Searching security records is useful when an analyst needs to quickly locate information about a specific account in a larger collection of records.

### **Assignment for Day 22**

**Security User Searcher**

Build a Python program that:

- Reads users from `security_users.txt`.
- Builds a `users` list containing dictionaries.
- Asks the user to enter a username to search for.
- Creates a `found_user` variable starting with `None`.
- Loops through the users.
- Searches for a matching username.
- Stores the matching user dictionary in `found_user`.
- Displays the username, role, and attempts when the user is found.
- Displays `User not found` when the user does not exist.
- Prints `Security search complete`.

## Key Takeaway

Today I learned how to search structured security data and handle both successful and unsuccessful searches.

This is an important step toward building security tools that can locate specific users, events, or records within larger datasets.
