username = input("Enter your username: ")
password = input("Enter your password: ")

attempts = int(input("Enter how many attempts: "))

if attempts >= 5:
    print("Warning: possible brute-force attacks")
    print("Report Immediately,", username)

else:
    print("Attempts are within limits")
    print("System is safe,", username)

print("Security check complete")