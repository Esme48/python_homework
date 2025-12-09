import csv

### Start of code reuse from assignment2 Task 2
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
    except Exception as e:
        print(f"An error occurred reading the file: {e}")

employees = read_employees()
#print(employees)

## End the reuse of Task 2 from assignment2

#Start of Task 3 assignment3
employee_names = [row[1] + " " + row[2] for row in employees["rows"]]
#print(employee_names)

employees_with_e = [name for name in employee_names if 'e' in name]
print(employees_with_e)

