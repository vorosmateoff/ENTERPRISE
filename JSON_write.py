import json 
  
employee_info = ['emp_id','emp_name', 'working','wage', 'skills']

new_dict = [
{'emp_id': 456, 'emp_name': 'George', 'skills': 'Python', 'working': True, 'wage': 323220},
{'emp_id': 892, 'emp_name': 'Adam', 'skills': 'Java', 'working': True, 'wage': 300030},
{'emp_id': 178, 'emp_name': 'Gilchrist', 'skills': 'Mongo db', 'working': True, 'wage': 20000},
{'emp_id': 155, 'emp_name': 'Elon', 'skills': 'Sql', 'working': True, 'wage': 20000},
{'emp_id': 299, 'emp_name': 'Mask', 'skills': 'Ruby', 'working': True, 'wage': 12000},
]
  
with open("Employees.json", "w") as outfile:
    json.dump(new_dict, outfile)