def analyze_login(username, attempts):
    if attempts >= 10:
        return "Critical risk, " + username
    elif attempts >= 5:
        return "Warning, " + username
    else:
        return "Low risk, " + username

result = analyze_login("boat", 7)
print(result)