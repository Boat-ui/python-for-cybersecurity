login = {
    "username": "boat",
    "attempts": 6,
    "status": "Suspicious"
}

login["attempts"] = 8
login["status"] = "Critical"
login["ip"] = "127.0.0.1"
login["device"] = "Desktop"

for key in login:
    print(key, login[key])
print(login.get("location", "not available"))