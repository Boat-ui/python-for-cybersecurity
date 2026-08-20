user = input("Enter your username: ")
age = int(input("Enter your age: "))
attempts = int(input("Enter failed attempts: "))

if age >= 18:
    if attempts >= 5:
        print("Suspicious activity,", user)
    else:
        print("Activity is normal,", user)

elif age < 18:
    print("Access restricted,", user)

print("Check complete")