suspicious = 0
users = []
suspicious_user = []

with open("security_users.txt") as file:
    for line in file:
        parts = line.strip().split(",")

        user = {
            "username": parts[0],
            "role": parts[1],
            "attempts": int(parts[2])
        }

        users.append(user)

for user in users:
    if user["attempts"] >= 3:
        print("User ", user["username"], " has suspicious activity")
        suspicious_user.append(user)
        suspicious = suspicious + 1

print("There are",suspicious, "suspicious users")
print("Security monitoring complete")