login = {
    "username": "boat",
    "attempts": 7,
    "status": "Suspicious",
    "ip": "127.0.0.1",
}

login["attempts"] = 9
login["device"] = "laptop"
print("key:", login.get("location", "not available"))


for key in login:
    print(key, login[key])
if login["attempts"] >= 5:
    print("Suspicious activity")
else:
    print("Normal activity")
