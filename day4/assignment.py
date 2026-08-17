username = input("Enter your username: ")
age = int(input("Enter your age: "))
attempts = int(input("Failed login attempts: "))

if age < 18 or attempts >= 5:
    print("Security Alert")

else:
    print("No immediate Alert")

print("Security check complete")