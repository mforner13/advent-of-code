from pprint import pprint

with open('data.py') as f:
    data = f.readlines()

data_as_dicts = []

for item in data:
    data_as_list = item.split()

    obj = {
            "positions": data_as_list[0],
            "letter": data_as_list[1][:1],
            "password": data_as_list[2]
    }
    data_as_dicts.append(obj)


def check_password_correct(password_with_rules: dict):
    positions = password_with_rules['positions'].split('-')
    letter = password_with_rules['letter']
    password = password_with_rules['password']
    p1 = int(positions[0]) - 1
    p2 = int(positions[1]) - 1
    positions = [p1, p2]
    if positions.count(letter) == 1:
        return True
    else:
        return False

total_corrects = 0

for item in data_as_dicts:
    if check_password_correct(item):
        total_corrects += 1


print(total_corrects)
