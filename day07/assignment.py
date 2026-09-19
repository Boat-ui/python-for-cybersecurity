accounts = ["admin", "root", "guest", "student", "owner"]

accounts.append("boat")
privileged = 0

for account in accounts:
    if account == "admin" or account == "root" or account == "guest" or account == "owner":
        privileged = privileged + 1
        print("Privileged account detected: ", account)
    else:
        print("Standard account: ", account)

print("Privileged account detected: ", privileged)