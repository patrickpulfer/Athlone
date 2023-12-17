import re, sys

file_name = 'employees.txt'


def FileToDictionary(file_name):
    employee_information = {}
    pps_regex = "[0-9]{7}[A-Z]{2}"
    salary_regex = "\\d+(?=\\s)"

    try:
        file = open(file_name, "r")

    except FileNotFoundError:
        print("Sorry file not found")
        sys.exit()

    for line in file.readlines():
        line = line.rstrip()
        pps = re.search(pps_regex, line).group(0)
        salary = re.search(salary_regex, line).group(0)
        employee_information[pps] = int(salary)

    return employee_information


def GetPPSWithHighestSalary(employee_dict):
    highest_salary = max(employee_dict.values())
    for key, value in employee_dict.items():
        if value == highest_salary:
            highest_salary_pps = key

    return highest_salary_pps
    

employee_information = FileToDictionary(file_name)

highest_salary_pps = GetPPSWithHighestSalary(employee_information)

print('PPSN of employee with the highest salary: ' + highest_salary_pps)