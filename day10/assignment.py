failed_count = 0

with open("security.txt") as file:
    for line in file:
        if "failed" in line:
            failed_count = failed_count + 1
            print("Failed login detected:", line.strip())

print("Total failed logins: ", failed_count)
print("Log analysis complete")