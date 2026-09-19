users = [
    {"username": "admin", "attempts": 5},
    {"username": "boat", "attempts": 1},
    {"username": "guest", "attempts": 4},
    {"username": "root", "attempts": 2},
    {"username": "student", "attempts": 6}
]

highest_attempts = 0
highest_user = ""

for user in users:
    if user["attempts"] > highest_attempts:
        highest_attempts = user["attempts"]
        highest_user = user["username"]

print("Highest-risk user:", highest_user)
print("Login attempts:", highest_attempts)