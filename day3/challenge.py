#Challenge: Security Decision program

SOC_name = input("Who is logging?")
attempts = int(input("Enter number of failed login attempts: "))

if attempts >= 10:
    print("Critical: Possible brute-force attack")
    print("Investigate Immediately,", SOC_name)

else:
    print("Attempts are below the critical threshold")
    print("Data logged Successfully,", SOC_name)

print("Security Check Completed")