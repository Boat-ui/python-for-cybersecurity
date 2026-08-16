uname = input("What is your username?:")
attempt = input("How many failed login attempts happened?:")
attempt = int(attempt)
print("User is:", uname)
print("Failed login attempt(s) is/are:", attempt)
print("And three more attempts would have made it", attempt+3)

