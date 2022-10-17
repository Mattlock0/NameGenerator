import csv
import collections

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
diagraphs = ['sh', 'ch', 'wh', 'ck', 'th', 'ph']  # potentially create an if statement to catch these


def name_to_template(name):
    letters = ([*name])  # separate name into a list of letters
    template = ""  # blank template

    for letter in letters:
        if letter.lower() in consonants:
            template += 'c'
        else:
            template += 'v'

    return template


def diagraph_name_template(name):
    letters = ([*name])  # separate name into a list of letters
    template = ""  # blank template
    flag = False

    for index, letter in enumerate(letters):
        if flag:  # we just read in a diagraph, so skip this letter
            flag = False
            continue

        if index + 1 < len(letters):  # there is the potential for a diagraph
            if letter + letters[index+1] in diagraphs:  # this pair of letters makes a diagraph
                template += 'c'  # it's just a consonant
                flag = True  # set the flag true so we don't doubly read in the letters
                continue

        if letter.lower() in consonants:
            template += 'c'
        else:
            template += 'v'

    return template


def flatten_and_sort(_2d_list, parsing):
    flat_list = []

    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)

    processed_names = []

    for el in flat_list:
        processed_names.append(parsing(el))

    frequency_of_names = collections.Counter(processed_names)
    frequency_of_names = dict(frequency_of_names)

    return dict(reversed(sorted(frequency_of_names.items(), key=lambda item: item[1])))


if __name__ == '__main__':
    file = open("../data/all_names.csv", "r")
    data = list(csv.reader(file))
    file.close()

    data1 = flatten_and_sort(data, name_to_template)
    data2 = flatten_and_sort(data, diagraph_name_template)

    print(data1)
    print(data2)
