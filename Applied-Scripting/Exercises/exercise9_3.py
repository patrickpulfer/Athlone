import re, sys

file_name = 'employees.txt'


def FileToDictionary(file_name):
    employee_information = {}
    department_regex = "\\w+$"

    try:
        file = open(file_name, "r")

    except FileNotFoundError:
        print("Sorry file not found")
        sys.exit()

    for line in file.readlines():
        line = line.rstrip()
        department = re.search(department_regex, line).group(0)

        if department in employee_information.keys():
            current_count = employee_information[department]
            employee_information.update({department: current_count + 1})
        else:
            employee_information[department] = 0

    return employee_information


def DepartmentWithMostEmployees(employee_dict):
    highest_department = max(employee_dict.values())
    for key, value in employee_dict.items():
        if value == highest_department:
            highest_department_key = key
    
    print('Department with most employees: ' + highest_department_key)


employee_information = FileToDictionary(file_name)
DepartmentWithMostEmployees(employee_information)