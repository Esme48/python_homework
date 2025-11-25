import csv

def read_employees():
    employee_csv = {}
    rows = []

    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            employee_csv["fields"] = next(reader)

            for row in reader:
                 rows.append(row)
        
        employee_csv["rows"] = rows

        return employee_csv
    except FileNotFoundError:
        print("The file was not found.")

employees = read_employees()
print(employees)
