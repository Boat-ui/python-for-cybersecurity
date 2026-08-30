def check_attempts(username, attempt):
    if attempt >= 5:
        return "Suspicious, " + username
    else:
        return "Not suspicious, " + username



result = check_attempts("Boat",7)
print(result)