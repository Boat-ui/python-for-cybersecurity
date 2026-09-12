while True:
    try:
        attempts = int(input("Enter number of attempts: "))
        break
    except ValueError:
        print("Invalid input. Try again.")