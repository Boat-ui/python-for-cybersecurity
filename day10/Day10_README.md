# Day 10: File Handling and Log Analysis

## What I Learned

- How to open a file using `open()`.
- How to use read mode.
- How `with open()` safely handles files and automatically closes them.
- How to read the contents of a file using `.read()`.
- How to process a file one line at a time using a `for` loop.
- How to search for specific information using `"text" in line`.
- How to use `.strip()` to remove unwanted whitespace and newline characters.
- How to use a counter to keep track of matching events while processing a file.
- How Python can be used to automate basic security log analysis.

## Security Practice

I created a `security.txt` file containing simulated security log entries.

I wrote a Python program that reads the log file line by line and searches for failed login attempts.

Whenever a failed login is detected, the program reports it and increases a counter.

After the entire file has been analyzed, the program displays the total number of failed login attempts.

### **Assignment for Day 10**

**Security Log Analyzer**

The program:

- Opens a security log using `with open()`.
- Reads the file line by line.
- Searches for lines containing `"failed"`.
- Reports every failed login detected.
- Uses a counter to track the total number of failed logins.
- Displays the final number of failed login attempts.
- Prints a message when the log analysis is complete.

This assignment helped me understand how Python can automatically process security logs and identify suspicious activity.
