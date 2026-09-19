username = input("Enter your username: ")
age = int(input("Enter your age: "))
attempt = int(input("Number of failed login attempt: "))

if age >= 18 and attempt >= 5:
    print("Adult with suspicious login activity,", username)


print("Security Check Complete")
