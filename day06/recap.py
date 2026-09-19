username = input("Please enter your username: ")
age = int(input("Please enter your age: "))
attempts = int(input("Please enter your attempts: "))
trust = input("Is device trusted? yes or no: ")

if attempts >= 10:
    if age >= 18 and trust == "no":
        print("Critical alert,", username)
    else:
        print("Alert: investigate,", username)


elif attempts >= 5:
    if trust == "yes":
        print("Warning: Trusted device, investigate.", username)
    else:
        print("Warning: untrusted device, investigate.", username)

else:
    print("Activity is normal,", username)

print("Security check complete,", username)