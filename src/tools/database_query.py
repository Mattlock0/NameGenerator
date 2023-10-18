import csv
import json
import urllib
import requests

PULL_LIMIT = '258000'  # max: 258000


def pull_data():
    limit = '?limit=' + PULL_LIMIT if not PULL_LIMIT == '' else ''

    url = f'https://parseapi.back4app.com/classes/Complete_List_Names{limit}'
    headers = {
        'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I',  # This is the fake app's application id
        'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK'  # This is the fake app's readonly master key
    }
    return json.loads(requests.get(url, headers=headers).content.decode('utf-8'))['results']


def csv_write(data):
    with open('../../data/name_database.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for element in data:
            writer.writerow([element[0], element[1].lower()])


def pull_and_write():
    data = pull_data()

    # strip that data list for only the info we need
    name_list = []
    for element in data:
        name_list.append((element['Name'].title(), element['Gender'].lower()))

    print(f'Length of List (before set): {len(name_list)}')
    name_list = sorted(list(set(name_list)))
    print(f'Length of List (after set): {len(name_list)}')

    # json_dump = json.dumps(data, indent=2)
    # with open("../../data/pulled_names.json", "w") as outfile:
    #     outfile.write(json_dump)

    csv_write(name_list)


if __name__ == '__main__':
    pull_and_write()
