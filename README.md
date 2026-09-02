# Python for Cybersecurity

My journey learning Python with a focus on cybersecurity.

## Day 1

I started my Python journey today.

### What I learned

- `print()`

- Strings

- Running Python programs

## Day 2

Today, I learned: Variables, integers, type conversion, inputs.

Variables are containers used to store values. They can be strings or integers.

### Integers are numbers

### Type conversion

Type conversion is changing a value type to another type. For example, you can change text (string) to a number (integer), and it is done using `int()`.

```python

age = "15"

```

To change `age` to a number, we use:

```python

age = int(age)

```

Python then reassigns a number (integer) to the variable `age`.

And to change back to text (string), we do this:

```python

age = str(age)

```

*To be learnt soon.*

### Inputs

Inputs are used to ask questions. For example, if you want a user to input their name rather than putting it directly in the code, you use `input()`, and Python pauses when it gets there to ask for the required information before moving on.

Example:

```python

name = input("What is your name?")

```

Python returns responses from `input()` as strings.

When Python gets there, it pauses to ask for the value to assign to the variable `name` before moving on.

Did all practices and tasks under each day, so refer to the days for the codes.

## Day 3

Today I learned:

- Comparison operators, and they are used to check values against other values.

- Booleans, and they are the results from a comparison.

- `if` statements check whether a condition is true or false, and if it is true, Python executes the indented code.

- `else` statements are used to execute code indented in it when a condition is `False`.

- Indentation tells Python that the code is a part of the code before it and should be executed together.

### Assignment Day3

**Mini Security Login Checker**
Your program should ask the user for:

- Username

- Password

- Number of failed login attempts

Then:

- If failed attempts are 5 or more, print a warning.

- Otherwise, tell them the attempts are within the limit.

- Print the username somewhere in the result.

- Print `"Security check completed"` at the end regardless of the number of attempts.

## Day 4

Today I learned:

- `and` is used to combine two or more conditions, and all conditions must be `True` for the final result to be `True`.
- `or` is used to combine two or more conditions, and at least one condition must be `True` for the final result to be `True`.
- I learned how to use `and` and `or` with comparison operators and `if/else` statements.
- I learned that with `and`, even if one condition is `False`, the whole result becomes `False`.
- I learned that with `or`, the result is only `False` when all the conditions are `False`.
- I also learned that an `else` statement can cover different situations when multiple conditions are being checked, so the message inside `else` should accurately describe what the condition actually means.

### Security Practice

I built security decision programs that used a username, age, and failed login attempts.

I used `and` to check if two conditions were true at the same time, such as checking whether a user was an adult and had multiple failed login attempts.

I also used `or` to create a security alert when either the user's age was below 18 or the number of failed login attempts was 5 or more.

### Assignment for Day4

#### **Security Alert Program**

The program asks the user for:

- Username
- Age
- Number of failed login attempts

The program then checks:

- If the user is below 18 **or** has 5 or more failed login attempts, it displays a `Security Alert`.
- Otherwise, it displays `No immediate Alert`.
- The program prints `Security check complete` at the end.

I tested the program with different combinations of ages and failed login attempts to make sure both the `if` and `else` conditions worked correctly.

## Day 5

Today I learned:

- `elif` statements, which means "else if" and are used when there are multiple possible conditions.
- Python checks `if`, `elif`, and `else` conditions from top to bottom.
- Once Python finds a condition that is `True`, it executes that block and does not continue to the remaining `elif` or `else` blocks.
- The order of conditions matters because Python executes the first condition that is `True`.
- Multiple `elif` statements can be used when there are several possible outcomes.
- Nested `if` statements, which are `if` statements placed inside another `if` statement.
- A nested `if` is only checked when the outer `if` condition is `True`.
- I learned that `else` statements can belong to either an outer `if` or an inner `if`, depending on their indentation.
- I also learned how to compare strings using `==`.

### Security Practice

I built several security decision programs using `if`, `elif`, `else`, and nested `if` statements.

I created a Login Risk Classifier that checks the number of failed login attempts and classifies the activity as critical, suspicious, or normal.

I also used a nested `if` to check whether a login came from a trusted device when there were multiple failed login attempts.

### Assignment for Day 5

#### Account Risk Classifier

The program asks the user for:

- Username
- Age
- Number of failed login attempts
- Whether the login is from a trusted device

The program then:

- Displays a critical warning if there are 10 or more failed attempts.
- For 5–9 failed attempts, uses a nested `if` to check whether the device is trusted.
- Displays a warning for multiple failed attempts from a trusted device.
- Displays a suspicious login warning if the device is untrusted.
- Displays that login activity appears normal if there are fewer than 5 failed attempts.
- Prints `Security check complete` at the end.

I tested the program with different numbers of failed attempts and both trusted and untrusted devices to make sure the different branches worked correctly.

## Day 6

Today I learned:

- `while` loops, which are used to repeat code while a condition is `True`.
- A `while` loop keeps running until its condition becomes `False`.
- Loop counters can be used to control how many times a loop runs.
- Variables inside a loop can be updated so that the loop eventually stops.
- An infinite loop can happen when the condition never becomes `False`.
- I learned how to use `if` statements inside a `while` loop.
- I learned how to use multiple conditions with `and` inside a `while` loop.
- I learned how to use `input()` inside a loop to repeatedly collect information from a user.
- I learned how to limit the number of times a user can perform an action using a counter.
- I also learned how to use an `if/else` after a loop to determine what happened after the loop ended.

### Security Practice

I used a `while` loop to create a password checker that keeps asking for a password while the password is incorrect and the user still has attempts available.

I learned how loops can be useful in cybersecurity for repeatedly checking login attempts and controlling how many times a user can try to authenticate.

**Assignment for Day 6**

**3-Attempt Login Security Checker**

The program asks the user for:

- Username
- Password

The program gives the user a maximum of 3 password attempts.

The program:

- Continues asking for the password while the password is incorrect and attempts are still available.
- Grants access if the correct password is entered.
- Denies access if all 3 attempts are used incorrectly.
- Prints the username in the result.

I tested the program with both a successful login on the third attempt and three incorrect password attempts.


## Day 7:

Today I learned:

- `for` loops, which are used to repeat code while going through a sequence of values.
- `range()` and how it generates a sequence of numbers.
- `range(start, stop)` starts at the given starting number and stops before the ending number.
- Unlike `while` loops, `for` loops can automatically move through a sequence without manually increasing a counter.
- How to use `for` loops to go through each character in a string.
- Lists, which are used to store multiple values in one variable.
- Python list indexes start from `0`.
- How to access individual items in a list using their index.
- `.append()` is used to add a new item to the end of a list.
- How to use a `for` loop to process every item in a list.
- How to combine `for` loops with `if/else` statements to make decisions about each item.
- How to create a counter variable and increase it when an item meets a specific condition.
- How loops can be used to process and count security-related data.

### Security Practice

I practiced using lists of usernames and accounts and used `for` loops to examine each account.

I created a Security Account Scanner that identifies privileged accounts and standard accounts.

I also used a counter to keep track of how many privileged accounts were found while the loop processed the entire list.

### **Assignment for Day 7**

**Security Account Scanner**

The program:

- Stores multiple usernames in a list.
- Adds another username using `.append()`.
- Uses a `for` loop to examine every account.
- Identifies privileged accounts such as `admin`, `root`, and `owner`.
- Prints a message for privileged and standard accounts.
- Uses a counter to keep track of the number of privileged accounts detected.
- Prints the total number of privileged accounts after checking the entire list.

This assignment helped me combine lists, `for` loops, `if/else`, `or`, `.append()`, and counters into one cybersecurity-related program.


## Day 8:

Today I learned:

- Functions, which are reusable blocks of code designed to perform a specific task.
- How to define a function using `def`.
- How to call a function to execute its code.
- Parameters, which allow functions to receive information.
- Arguments, which are the actual values passed into a function.
- How a function can accept multiple parameters.
- `return`, which sends a value back from a function.
- The difference between `print()` and `return`.
- How to store a returned value in a variable.
- How to use a returned value in another `if/else` decision.
- How to combine functions with `if`, `elif`, and `else`.

### Security Practice

I created functions that analyze login attempts and determine whether login activity is suspicious.

I practiced passing usernames and failed login attempts into a function and returning different security risk levels based on the number of attempts.

### **Assignment for Day 8**

**Security Risk Analyzer**

I created a function called `analyze_login(username, attempts)`.

The function classifies login activity into:

- **Low risk** for fewer than 5 attempts.
- **Warning** for 5–9 attempts.
- **Critical risk** for 10 or more attempts.

The function returns the appropriate result instead of printing it directly.

I then stored and printed the returned results and tested all three risk levels successfully.

This helped me understand how functions can process information, return results, and be reused with different inputs.


## Day 9:

Today I learned:

- Dictionaries, which store data as key/value pairs.
- How to create a dictionary using `{}`.
- How to access a value using its key.
- How to update an existing dictionary value.
- How to add a new key/value pair to a dictionary.
- The `.get()` method and how it can safely retrieve a value when a key may not exist.
- How to provide a default value with `.get()`.
- How to use a `for` loop to go through dictionary keys.
- How to use a key to retrieve its corresponding value while looping.
- How to combine dictionaries with `for` loops and `if/else` statements.

### Security Practice

I worked with a login record containing information such as a username, failed login attempts, status, IP address, and device.

I practiced updating information in the record, adding new information, handling missing information with `.get()`, and analyzing the login attempts.

### **Assignment for Day 9**

**Security Login Record Analyzer**

The program:

- Creates a dictionary containing login information.
- Updates the number of failed attempts.
- Adds a device to the login record.
- Uses `.get()` to safely check for missing location information.
- Uses a `for` loop to display the dictionary's keys and values.
- Uses `if/else` to determine whether the login activity is suspicious.

This assignment helped me understand how Python dictionaries can be used to store and analyze structured security information.


## Day 10:

Today I learned:

- File handling in Python.
- How to open a file using `open()`.
- Read mode and how `"r"` is used to read a file.
- How `with open()` safely handles files and automatically closes them.
- How to read the entire contents of a file using `.read()`.
- How to process a file one line at a time using a `for` loop.
- How to use `"text" in line` to search for specific information.
- How to use `.strip()` to remove unwanted whitespace and newline characters.
- How to use a counter to keep track of matching events while processing a file.

### Security Practice

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

This assignment helped me understand how Python can be used to automatically process security logs and identify suspicious activity instead of manually checking every log entry.


## Day 11:

Today I learned:

- How to write information to a file using `file.write()`.
- The difference between `"w"` (write/overwrite) and `"a"` (append) file modes.
- How `"w"` replaces existing file contents.
- How `"a"` keeps existing contents and adds new information.
- How to use `\n` to create a new line when writing to a file.
- How Python can automatically generate and store security reports.

### Security Practice

I created a Python program that opens `security.txt` in append mode and adds security events to the file.

The program records failed login activity, suspicious activity, and the completion of a security scan.

I also tested the program multiple times to confirm that append mode adds new entries without deleting the previous contents.

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