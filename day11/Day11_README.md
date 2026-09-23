# Day 11: Writing and Appending Files

## What I Learned

- How to write information to a file using `file.write()`.
- The difference between `"w"` (write/overwrite) and `"a"` (append) file modes.
- How `"w"` replaces existing file contents.
- How `"a"` keeps existing contents and adds new information.
- How to use `\n` to create a new line when writing to a file.
- How Python can automatically generate and store security reports.

## Security Practice

I created a Python program that opens `security.txt` in append mode and adds security events to the file.

The program records failed login activity, suspicious activity, and the completion of a security scan.

I also tested the program multiple times to confirm that append mode adds new entries without deleting previous contents.

### **Assignment for Day 11**

**Security Report Generator**

The program:

- Opens `security.txt` using append mode.
- Writes multiple security events to the file.
- Uses `\n` to place each event on its own line.
- Preserves existing information in the file.
- Adds new security events whenever the program runs.
- Displays a message confirming that the security report was updated.

This assignment helped me understand how Python can not only read security logs but also create and update security reports automatically.
