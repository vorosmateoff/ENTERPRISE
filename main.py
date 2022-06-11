import csv

class Employee:
  def __init__(self, emp_id, emp_name, working, wage, skills):
    self.emp_id = emp_id
    self.emp_name = emp_name
    self.working = working
    self.wage = wage
    self.skills = skills


employees = []

with open('Employees.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) != 0:
            employees.append(Employee(row[0], row[1],row[2],row[3],row[4]))

for e in employees:
    print(e.emp_id,e.emp_name,e.working,e.wage,e.skills)