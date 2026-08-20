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
