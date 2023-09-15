from src.iterator import Iterator
from enum import IntEnum
import random


LITERAL_SYMBOLS = ['\\', '/', '|', '$', '@']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'r', 's', 't', 'v', 'w']
RARE_CONSONANTS = {'p': 252, 'z': 191, 'x': 71, 'q': 61, 'y': 35}
DIAGRAPHS = {'sh': 275, 'th': 219, 'ch': 185, 'ck': 77, 'ph': 71, 'qu': 58, 'ng': 58}
DOUBLE_CONSONANTS = {'ll': 398, 'nn': 310, 'tt': 199, 'rr': 157, 'ss': 126, 'mm': 44, 'dd': 31, 'ff': 29, 'bb': 27}
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
DOUBLE_VOWELS = {'ee': 152, 'oo': 28, 'aa': 15}
ALL_SYMBOLS = [CONSONANTS, RARE_CONSONANTS, DIAGRAPHS, DOUBLE_CONSONANTS, VOWELS, DOUBLE_VOWELS]

rare_chance = 5
double_chance = 9
diagraph_chance = 12
pair_chance = 5


class Symbols(IntEnum):
    CONSONANT = 0
    RARE_CONSONANT = 1
    DIAGRAPH = 2
    DOUBLE_CONSONANT = 3
    VOWEL = 4
    DOUBLE_VOWEL = 5


def cut_tuple(tuple_list, index):
    return list(map(lambda x: x[index], tuple_list))


def random_choice(choices):
    if type(choices) == list:
        return random.choice(choices)
    return random.choices(list(choices.keys()), weights=list(choices.values()), k=1)[0]


def generate_consonant() -> str:
    # set up basic consonant chance based on other chances
    consonant_chance = 100 - rare_chance - double_chance - diagraph_chance

    # choose one generation type based on weights
    type_to_generate = random_choice({Symbols.CONSONANT: consonant_chance, Symbols.RARE_CONSONANT: rare_chance,
                                      Symbols.DIAGRAPH: diagraph_chance, Symbols.DOUBLE_CONSONANT: double_chance})

    # generate a consonant of that type
    return random_choice(ALL_SYMBOLS[type_to_generate])


def generate_vowel() -> str:
    # set up basic vowel chance based on double chance
    vowel_chance = 100 - double_chance

    # choose one generation type based on weights
    type_to_generate = random_choice({Symbols.VOWEL: vowel_chance, Symbols.DOUBLE_VOWEL: double_chance})

    # generate a vowel of that type
    return random_choice(ALL_SYMBOLS[type_to_generate])


def generate_letter(template: Iterator) -> str:
    if template.curr() in LITERAL_SYMBOLS:
        if template.has_next():
            template.next()
            return template.next()
        else:
            return template.curr()

    template_letter = template.next()
    if template_letter.lower() == 'c':
        generated_symbol = generate_consonant()
    elif template_letter.lower() == 'v':
        generated_symbol = generate_vowel()
    elif template_letter == '*':
        generated_symbol = random.choice([generate_vowel(), generate_consonant()])
    else:  # no template letter was passed in; generate nothing
        generated_symbol = template_letter

    if template_letter.isupper():
        return generated_symbol.title()
    else:
        return generated_symbol


if __name__ == '__main__':
    template_raw = "Cvcvcv"
    template = Iterator([*template_raw])

    # Distribution test
    # distribution = {}
    # for _ in range(10000):
    #     gen = random_choice(DOUBLE_LETTERS)
    #     if gen in distribution.keys():
    #         distribution[gen] += 1
    #     else:
    #         distribution[gen] = 1
    #
    # print(sorted(distribution.items(), key=lambda x: x[1], reverse=True))

    name = ""

    while template.has_next():
        name += generate_letter(template)

    print(f'Name: {name}')
