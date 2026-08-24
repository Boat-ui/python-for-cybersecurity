password = ""
attempt = 1

while password != "cyber" and attempt <= 3:
    password = input("Please enter your password: ")
    attempt = attempt + 1

if password == "cyber":
        print("Access granted")
else:
        print("Access denied")