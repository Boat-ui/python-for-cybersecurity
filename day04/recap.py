username = input("Enter your username: ")
age = int(input("Enter your age: "))
attempt = int(input("Number of failed login attempt: "))

if age >= 18:
    print("You are an adult", username)
else:
    print("You are a minor", username)

if attempt >= 5:
    print("Suspicious attempts", username)
else:
    print("Safe attempts", username)

print("Security Check Complete")
