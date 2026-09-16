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

def check_attempt(user):
    if user["attempts"] >= 3:
        return "Suspicious"
    else:
        return "Normal"
for user in users:
    result = check_attempt(user)
    print(user["username"],result)

print("Security monitoring complete")