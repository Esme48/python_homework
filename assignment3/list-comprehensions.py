import csv

with open('../csv/employees.csv', 'r') as file:
    reader = csv.reader(file)