import csv

def read_employees():
    employee_csv = {"fields": None, "rows": []}

    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            employee_csv["fields"] = next(reader)

            for row in reader:
                 employee_csv["rows"].append(row)

        return employee_csv
    except FileNotFoundError:
        print("The file was not found.")

read_employees()
