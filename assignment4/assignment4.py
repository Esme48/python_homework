## Task 1

import pandas as pd
import json

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()

salary = [70000, 80000, 90000]
task1_with_salary['Salary'] = salary
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

task1_older.to_csv("employees.csv", index=False)


#Task 2
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

data_two = {
    'Name': ['Eve', 'Frank'],
    'Age': [28, 40],
    'City': ['Miami', 'Seattle'],
    'Salary' : [60000, 95000]
}

json_str = json.dumps(data_two, indent = 4)

with open("additional_employees.json", "w") as f:
    f.write(json_str)

json_employees = pd.read_json('additional_employees.json')
print(json_employees)

more_employees = pd.merge(task1_older, json_employees)
print(more_employees)

#Notes: 
#- https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
# Create a JSON file (additional_employees.json). The file adds two new employees. Eve, who is 28, lives in Miami, and has a salary of 60000, and Frank, who is 40, lives in Seattle, and has a salary of 95000.
# Load this JSON file into a new DataFrame and assign it to the variable json_employees.
# Print the DataFrame to verify it loaded correctly and run the tests.