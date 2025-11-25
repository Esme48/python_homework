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
    return employees["fields"].index(string)

employee_id_column = column_index("employee_id")
#print(employee_id_column)

#Task   4

def first_name(num): #Defining the first_name function and it has parameter num
    call_column = column_index("first_name") #Calls the previous function and in the 'fields" looks up the 'first_name'
    row = employees["rows"][num] #Inside employees from two previous functions, it looks through the rows and looks for the specific number
    return row[call_column] #Returns the 'first-name' of the row
    #When there are two brackets "something[a][b]" the operation acceses [a] first and then it retrieves [b] in [a]
result = first_name(2)
#print(result)

#Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

results_two = employee_find(2)

