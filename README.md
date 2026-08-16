\# Python for Cybersecurity



My journey learning Python with a focus on cybersecurity.



\## Day 1:



I started my Python journey today.



\### What I learned



\- `print()`

\- Strings

\- Running Python programs



\## Day 2:



Today, I learned: Variables, integers, type conversion, inputs.



Variables are containers used to store values. They can be strings or integers.



\### Integers are numbers



\### Type conversion



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



\*To be learnt soon.\*



\### Inputs



Inputs are used to ask questions. For example, if you want a user to input their name rather than putting it directly in the code, you use `input()`, and Python pauses when it gets there to ask for the required information before moving on.



Example:



```python

name = input("What is your name?")

```



Python returns responses from `input()` as strings.



When Python gets there, it pauses to ask for the value to assign to the variable `name` before moving on.



Did all practices and tasks under each day, so refer to the days for the codes.



\## Day 3:



Today I learned:



\- Comparison operators, and they are used to check values against other values.

\- Booleans, and they are the results from a comparison.

\- `if` statements check whether a condition is true or false, and if it is true, Python executes the indented code.

\- `else` statements are used to execute code indented in it when a condition is `False`.

\- Indentation tells Python that the code is a part of the code before it and should be executed together.



\### Assignment for the Day:



\*\*Mini Security Login Checker\*\*



Your program should ask the user for:



\- Username

\- Password

\- Number of failed login attempts



Then:



\- If failed attempts are 5 or more, print a warning.

\- Otherwise, tell them the attempts are within the limit.

\- Print the username somewhere in the result.

\- Print `"Security check completed"` at the end regardless of the number of attempts.

