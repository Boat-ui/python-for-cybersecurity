with open("security.txt") as file:
    for line in file:
        if "failed" in line:
            print("Failed login detected:", line.rstrip())

print("Log analysis complete")