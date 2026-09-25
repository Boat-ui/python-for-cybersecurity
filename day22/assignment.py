found_user = None
users = []

with open ("security_users.txt") as file:
    for line in file:
        parts = line.strip().split(",")


        user = {
            "username": parts[0],
            "role": parts[1],
            "attempts": int(parts[2]),
        }

        users.append(user)

search_user = input("Enter username to search for: ")
for user in users:
    if user["username"] == search_user:
        found_user = user

if found_user is not None:
    print("Username:", found_user["username"])
    print("Role:", found_user["role"])
    print("Attempts:", found_user["attempts"])
else:
    print("User not found")

print("Security search complete")