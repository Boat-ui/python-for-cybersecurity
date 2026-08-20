us_name = input("What is your name? ")
age = int(input("How old are you? "))
failed_attempts = int(input("Number of failed attempts? "))

if age >= 18 and failed_attempts < 5:
    print("Access granted,", us_name)

else:
    print("Access denied,", us_name)

print("Check Complete!")

