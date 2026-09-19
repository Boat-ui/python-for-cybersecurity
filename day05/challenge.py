username = input("Enter username: ")
age = int(input("Enter age: "))
attempts = int(input("Enter failed logins: "))

if attempts >= 10:
    print("Critical: Possible brute-force attack")

elif attempts >= 5:
    if age >= 18:
        print("Adult account: investigate")
    else:
        print("Minor account: investigate")

else:
    print("Login activity is normal")

print("Security check complete")