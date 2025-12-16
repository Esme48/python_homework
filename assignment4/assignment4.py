## Task 1

import pandas as pd

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
