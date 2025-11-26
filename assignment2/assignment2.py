import os
import csv
import custom_module

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

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

#Task 7
def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[2])
    return employees["rows"]
                                  
results_seven = sort_by_last_name()

#Task 8                                                                                                                                                                             

def employee_dict(row):
    employee_dict = dict(zip(employees["fields"][1:], row[1:]))
    return employee_dict

result_eight = print(employee_dict(employees["rows"][5]))

# Task 9

def all_employees_dict():
    employees_dict = {}
    for rows in employees["rows"]:
        employee_id = rows[0]
        employees_dict[employee_id] = employee_dict(rows)
    return employees_dict


result_nine = all_employees_dict()
print(result_nine)

#Task 10

def get_this_value():
    env_variable = os.getenv('THISVALUE')
    return env_variable

#Task 11

def set_that_secret(new_secret_to_set):
    secret = custom_module.set_secret(new_secret_to_set)

result = set_that_secret("welcome")
print(custom_module.secret)

# Task 12
def read_minutes():
    minutes1 = {}
    rows1 = []
    minutes2 = {}
    rows2 = []
    with open('../csv/minutes1.csv', 'r') as file:
            reader = csv.reader(file)
            minutes1["fields"] = next(reader)

            for row in reader:
                rows1.append(tuple(row))
        
    minutes1["rows"] = rows1
    
    with open('../csv/minutes2.csv', 'r') as file:
            reader = csv.reader(file)
            minutes2["fields"] = next(reader)

            for row in reader:
                rows2.append(tuple(row))
        
    minutes2["rows"] = rows2
    
    return minutes1, minutes2

#result_twelve = read_minutes()
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

