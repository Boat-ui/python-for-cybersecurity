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

for user in users:
    print(user["username"])
    print(user["attempts"])
    print(user["role"])

    if user["attempts"] >= 3:
            print("Suspicious login activity")
    else:
            print("Login activity normal")



print("Security monitoring complete")
