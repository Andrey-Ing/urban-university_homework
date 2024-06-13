import json


def employees_rewrite(sort_type):
    key = None
    reverse = False
    if sort_type.lower() == 'firstname':
        key = 'firstName'
    elif sort_type.lower() == 'lastname':
        key = 'lastName'
    elif sort_type.lower() == 'department':
        key = 'department'
    elif sort_type.lower() == 'salary':
        key = 'salary'
        reverse = True
    else:
        raise ValueError('Bad key for sorting')

    with open("employees.json", "r") as read_file:
        loaded_json_file = json.load(read_file)
        employees_lst = loaded_json_file['employees']

        employees_lst.sort(key=lambda people: people[key], reverse=reverse)

        employees = {'employees': employees_lst}

        with open(f"employees_{sort_type.lower()}_sorted.json", "w") as write_file:
            json.dump(employees, write_file, indent=4)


employees_rewrite('firstName')
employees_rewrite('LastName')
employees_rewrite('DEPARTMENT')
employees_rewrite('Salary')
