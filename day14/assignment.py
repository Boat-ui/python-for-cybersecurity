attempts = int(input("Enter number of attempts: "))
suspicious_ip = input("Is the IP suspicious? True/False: ") == "True"

if attempts >= 3 and suspicious_ip == True:
    print("High risk activity detected")
elif attempts >= 3 or suspicious_ip == True:
    print("Suspicious activity detected")
else:
    print("Login activity appears normal")

print("Login Detection complete")
