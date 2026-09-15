users =[
    {
        "username":"admin",
        "role":"administrator",
        "attempts": 5
    },

    {
        "username":"boat",
        "role":"standard",
        "attempts":1
    },

    {
        "username":"guest",
        "role":"standard",
        "attempts":4
    },

    {
        "username":"root",
        "role":"administrator",
        "attempts":2
    }

]

def check_attempts(user):
    if user["attempts"] >= 3:
        return "Suspicious"
    else:
        return "Normal"


for user in users:
    result=check_attempts(user)
    print(user["username"],result)

print("Security monitoring complete")