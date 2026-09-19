username = input("Enter your username: ")
password = ""
attempts = 1

while password != "cyber" and attempts <= 3:
    password = input("Enter your password: ")
    attempts = attempts + 1

if password == "cyber":
    print("Access granted,", username)
else:
    print("Access denied,", username)

print("Security check complete")