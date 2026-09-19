username = input("Enter your username: ")
password = input("Enter your password: ")
age = int(input("Enter your age: "))

attempts = int(input("Enter how many attempts: "))

if attempts >= 5 or age < 18:
    print("Warning: Security alert")

else:
    print("No immediate alerts")

print("Security check complete")