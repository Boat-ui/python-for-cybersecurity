users = [
    {"username": "admin", "role": "administrator", "attempts": 5},
    {"username": "boat", "role": "standard", "attempts": 1},
    {"username": "guest", "role": "standard", "attempts": 4},
    {"username": "root", "role": "administrator", "attempts": 2}
]

for user in users:
    if user["attempts"] >= 3:
        print(user["username"], "has suspicious activity")