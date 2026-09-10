number = int(input("Enter a number: "))

#If someone enters:

#hello

#Python crashes with a ValueError.

#That's a problem for security tools because users can enter unexpected data, and log files can contain malformed information.

#try and except

#try:
    # code that might cause an error
#except:
    # what to do if an error happens

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except:
    print("Invalid input")