#Safe Number Checker

try:
    attempts = int(input("Enter number of attempts: "))
    print("Attempts:", attempts)
except ValueError:
    print("Invalid input. Please enter a number.")