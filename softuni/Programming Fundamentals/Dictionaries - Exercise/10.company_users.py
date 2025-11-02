command = input()
data = {}

while command != "End":
    company_name, employee_id = command.split(" -> ")

    if company_name not in data:
        data[company_name] = []

    if employee_id not in data[company_name]:
        data[company_name].append(employee_id)

    command = input()

for company, employees in data.items():
    print(company)
    for empl_id in employees:
        print(f"-- {empl_id}")
