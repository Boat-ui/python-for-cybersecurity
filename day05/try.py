name = input("Enter your username: ")
age = int(input("Enter your age: "))
attempts = int(input("failed login attempts: "))

if age >= 18:
    if attempts >= 5:
        print("Suspicious activity")
    else:
        print("Activity is normal")

else :
        print("Access denied")