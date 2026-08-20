name = input("Enter username : ")
age = int(input("Enter age : "))
attempts = int(input("Enter number of attempts : "))
trusted_device = input("Is is trusted device? Yes or No : ")


if attempts >= 10:
    print("Critical")

elif attempts >= 5:
    if trusted_device == "yes":
        print("Warning: Multiple failed attempts from trusted device")
    else:
        print("Warning: Suspicious login from untrusted device")

else:
    print("Login activity appears normal")

print("Security check complete")