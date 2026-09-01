with open("security.txt.txt") as file:
    content = file.read()
    print(content)

  #another codes
with open("security.txt") as file:
    for line in file:
        print(line)