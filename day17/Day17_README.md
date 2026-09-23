# Day 17: Reading Structured Data from Files

## What I Learned

- How to read structured information from a text file.
- How to process a file one line at a time.
- How to use `.strip()` to clean each line.
- How to use `.split(",")` to separate values in a line.
- How to access separated values using list indexes.
- How file data is initially read as strings.
- How to convert numerical data from a string to an integer using `int()`.
- How to build dictionaries from data read from a file.
- How to store multiple dictionaries inside a list.
- How file handling, lists, and dictionaries can work together.

## Security Practice

I created a `security_users.txt` file containing structured user security records.

I wrote a Python program that reads each record, separates the values, converts the login attempts into an integer, and creates a dictionary for each user.

The dictionaries are stored in a list so they can be analyzed using the security functions learned previously.

### **Assignment for Day 17**

**Security User File Analyzer**

The program:

- Opens a structured security file.
- Reads the file line by line.
- Uses `.strip()` and `.split(",")`.
- Creates a dictionary for each user.
- Converts login attempts into integers.
- Stores the dictionaries in a `users` list.
- Uses the Day 16 security analysis function.
- Displays each user's security result.
- Prints a message when security monitoring is complete.

This assignment helped me connect file handling with the structured data and functions I learned earlier.
