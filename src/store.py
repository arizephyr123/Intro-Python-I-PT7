"""
python3 store.py

output should be:
The Dugout #name
    1. Running
    2. Baseball
    3. Basketball
    4. Exit
Select the number of a department

*****
Attributes:
- name
- departments

Optional extra attributes:
- Store Hours
- Store capacity

*****
Notes:
self = like this in JS, this instance of this class, makes a copy of the class as an object instance, saves it in memory

__str__ = goal for readability, to print specific instance of object

__repr__ = representation, for debugging, if no string, should be able to id this instance of the

str type casting polymorhic => means can convert object or int string
"""

from departments import Department


class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = []

        for dep in departments:
            department = Department(dep)
            # creating instance of class Department
            self.departments.append(department)
            # adding it to list of departments in class Store

    def __str__(self):
        # return f'Store name is {self.name}'
        output = ''

        output += self.name + "\n"

        for index, department in enumerate(self.departments):
            output += str(index + 1) + '. ' + str(department) + "\n"

        output += str(len(self.departments) + 1) + ". Exit"
        return output


store = Store("The Dugout", ["Running", "Baseball", "Basketball"])

print(store)

selection = 0
while selection != len(store.departments) + 1:
    selection = input("Select the number of a department.")
    selection = int(selection)

    try:
        if selection >= 1 and selection < (len(store.departments) + 1)
        print(f"the user selected {selection}")
        else:
            print("Choose selection)
