users = []

with open("security_users.txt") as file:
    for line in file:
        parts = line.strip().split(",")

        user = {
            "username": parts[0],
            "role": parts[1],
            "attempts": int(parts[2])
        }

        users.append(user)

sorted_users = sorted(users, key=lambda user: user["attempts"], reverse=True)
for user in sorted_users:
    print(user["username"], user["attempts"])

print("Security monitoring complete")