username = input("Enter your username: ")
password = ""
attempt = 1

while password != "admin123" and attempt <=3:
    password = input("Enter your password: ")
    attempt = attempt + 1

if password == "admin123":
    print("Access granted,", username)
else:
    print("Access denied,", username)