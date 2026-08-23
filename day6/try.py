attempt = int(input("Enter your attempt number: "))
limit = int(input("Enter your limit: "))

while attempt <= limit:
    print("attempt #", attempt)
    if attempt == 3:
        print("Review this attempt")

    attempt = attempt + 1

print("Monitoring complete")