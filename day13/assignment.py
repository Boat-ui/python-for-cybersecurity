while True:
    try:
        attempts = int(input("Enter number of attempts: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

if attempts >= 3:
    print("Account may be under attack")
else:
    print("Login activity appears normal")

print("Logs analysis complete")