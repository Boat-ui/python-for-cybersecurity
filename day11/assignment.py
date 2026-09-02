with open ("security.txt","a") as file:
    file.write("\nFailed login detected\n")
    file.write("Suspicious activity detected\n")
    file.write("Security scan complete\n")

print("Security report updated")