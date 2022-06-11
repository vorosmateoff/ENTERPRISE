# Converting Python Dictionary to XML
from dict2xml import dict2xml
children1=["Peter","Steve"]
employees = {
    "employees":{  'employee1': 
    {
        'Firstname': 'Matthew',
        'Lastname': 'Andrew',
        'Working': True,
        'Wage': 120000,
        'Childrens':children1
        },
    'employee2': 
    {
        'Firstname': 'Matthew',
        'Lastname': 'Andrew',
        'Working': True,
        'Wage': 120000,
        'Childrens':children1
        },
    'employee3': 
    {
        'Firstname': 'Matthew',
        'Lastname': 'Andrew',
        'Working': True,
        'Wage': 120000,
        'Childrens':children1
        }}
}

xml = dict2xml(employees)
print(xml)
 
xmlfile = open("Employees.xml", "w")
xmlfile.write(xml)
xmlfile.close()