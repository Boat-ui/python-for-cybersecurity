employees = []

with open("employees.txt") as file:
    for line in file:
        parts = line.strip().split(",")

        employee={
            "name":parts[0],
            "role":parts[1],
            "attempta":int(parts[2])
        }

        employees.append(employee)

print(employees)