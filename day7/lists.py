users = ["admin","owner", "boat", "him", "guest"]

users.append("root")

for user in users:
    if user == "admin" or user == "owner":
        print("Privileged account:", user)
    else:
        print("Standard account:", user)