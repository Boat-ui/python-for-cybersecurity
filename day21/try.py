users = [
    {"username": "admin", "attempts": 5},
    {"username": "boat", "attempts": 1},
    {"username": "guest", "attempts": 4},
    {"username": "root", "attempts": 2}
]

sorted_users = sorted(users, key=lambda user: user["attempts"], reverse=True)

for user in sorted_users:
    print(user["username"], user["attempts"])