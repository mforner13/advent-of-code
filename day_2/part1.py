from pprint import pprint

with open('data.py') as f:
    data = f.readlines()

data_as_dicts = []

for item in data:
    data_as_list = item.split()

    obj = {
            "range": data_as_list[0],
            "letter": data_as_list[1][:1],
            "password": data_as_list[2]
    }
    data_as_dicts.append(obj)


def check_password_correct(password_with_rules: dict):
    limits = password_with_rules['range'].split('-')
    lower_limit = int(limits[0])
    upper_limit = int(limits[1])
    letter = password_with_rules['letter']
    password = password_with_rules['password']

    if password.count(letter) in range(lower_limit, upper_limit+1):
        return True


total_corrects = 0

for item in data_as_dicts:
    if check_password_correct(item):
        total_corrects += 1


print(total_corrects)
