import csv

# Task 2
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

#Task 3

def column_index(string):
    employees["fields"].index("first_name")

result = column_index("employee_id")
print(result)