## Task 1

import pandas as pd
import json

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
#print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()

salary = [70000, 80000, 90000]
task1_with_salary['Salary'] = salary
#print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
#print(task1_older)

task1_older.to_csv("employees.csv", index=False)


#Task 2
task2_employees = pd.read_csv('employees.csv')
#print(task2_employees)

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
#print(json_employees)

more_employees = pd.concat([task1_older, json_employees], ignore_index=True)
#print(more_employees)


#Task 3:

first_three = more_employees.head(3)
#print(first_three)

last_two = more_employees.tail(2)
#print(last_two)

employee_shape = more_employees.shape
#print(employee_shape)

more_employees.info()

#Task 4

dirty_data = pd.read_csv('dirty_data.csv')
#print(dirty_data)
clean_data = dirty_data.copy()
#print(clean_data)
clean_data.drop_duplicates(inplace=True)
#print(clean_data)
clean_data["Age"] = clean_data["Age"].replace("unknown", pd.NA)
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors = "coerce")
#print(clean_data)
clean_data["Salary"] = clean_data["Salary"].replace("unknown", pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors = "coerce")

age_mean = clean_data["Age"].mean()
salary_median = clean_data["Salary"].median()

clean_data["Age"] = clean_data["Age"].fillna(age_mean)
clean_data["Salary"] = clean_data["Salary"].fillna(salary_median)
#print(clean_data)

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors ="coerce")
print(clean_data)



#Notes: 
#- https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
#-https://www.geeksforgeeks.org/pandas/python-pandas-dataframe-drop_duplicates/