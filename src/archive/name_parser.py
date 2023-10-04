import csv
import collections
from src.iterator import Iterator
from src.generator_v3 import DIAGRAPHS

CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']


def name_to_template(name):
    letters = ([*name])  # separate name into a list of letters
    template = ""  # blank template

    for letter in letters:
        if letter.lower() in CONSONANTS:
            template += 'c'
        else:
            template += 'v'

    return template


def diagraph_name_template(name):
    name_iter = Iterator(name)
    template = ""

    while True:
        concat_pair = name_iter.curr() + name_iter.get_next()
        if concat_pair.lower() in DIAGRAPHS:
            template += 'c'
            name_iter.next()
            name_iter.next()
            if not name_iter.has_next():
                break
            continue

        if name_iter.curr().lower() in CONSONANTS:
            template += 'c'
        else:
            template += 'v'

        name_iter.next()
        if not name_iter.has_next():
            break

    return template


def common_pairs_template(name):
    template = Iterator(name)
    pair_list = []

    # continue until we break
    while True:
        curr, next = template.curr().lower(), template.get_next().lower()
        if curr in CONSONANTS and next in CONSONANTS or curr in VOWELS and next in VOWELS:
            pair_list.append(curr + next)

        # cycle to the next letter
        template.next()

        # break when we've reached the end of the name
        if not template.has_next():
            break

    return pair_list


def extract_doubles(pair_dict: dict):
    double_dict = {}

    for key, value in pair_dict.items():
        parsed_key = ([*key])
        if parsed_key[0] == parsed_key[1]:
            double_dict[key] = value

    return double_dict


def extract_pairs(pair_dict: dict):
    common_dict = {}

    for key, value in pair_dict.items():
        parsed_key = ([*key])
        if not parsed_key[0] == parsed_key[1]:
            common_dict[key] = value

    return common_dict


def extract_consonant_pairs(pair_dict: dict):
    consonant_dict = {}

    for key, value in pair_dict.items():
        parsed_key = ([*key])
        if parsed_key[0] in CONSONANTS and parsed_key[1] in CONSONANTS:
            consonant_dict[key] = value

    return consonant_dict


def extract_vowel_pairs(pair_dict: dict):
    consonant_dict = {}

    for key, value in pair_dict.items():
        parsed_key = ([*key])
        if parsed_key[0] in VOWELS and parsed_key[1] in VOWELS:
            consonant_dict[key] = value

    return consonant_dict


def flatten_and_sort(_2d_list, parsing_func):
    flat_list = []

    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)

    processed_names = []

    for el in flat_list:
        retval = parsing_func(el)
        if type(retval) == list:
            processed_names.extend(retval)
        else:
            processed_names.append(retval)

    frequency_of_names = collections.Counter(processed_names)
    frequency_of_names = dict(frequency_of_names)

    return dict(reversed(sorted(frequency_of_names.items(), key=lambda item: item[1])))


if __name__ == '__main__':
    file = open("../../data/all_names.csv", "r")
    data = list(csv.reader(file))
    file.close()

    template_frequency = flatten_and_sort(data, name_to_template)
    diagraph_frequency = flatten_and_sort(data, diagraph_name_template)
    double_frequency = extract_doubles(flatten_and_sort(data, common_pairs_template))
    consonant_pair_frequency = extract_consonant_pairs(extract_pairs(flatten_and_sort(data, common_pairs_template)))
    vowel_pair_frequency = extract_vowel_pairs(extract_pairs(flatten_and_sort(data, common_pairs_template)))

    print(f"Template Frequency: {template_frequency}")
    print(f"Diagraph Frequency: {diagraph_frequency}")
    print(f"Double Frequency: {double_frequency}")
    print(f"Consonant Pair Frequency: {consonant_pair_frequency}")
    print(f"Vowel Pair Frequency: {vowel_pair_frequency}")
