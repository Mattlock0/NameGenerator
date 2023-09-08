import random
from src.iterator import Iterator

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w']
RARE_CONSONANTS = {'p': 252, 'z': 191, 'x': 71, 'q': 61}
DOUBLE_LETTERS = {'ll': 398, 'nn': 310, 'tt': 199, 'rr': 157, 'ee': 152, 'ss': 126, 'mm': 44, 'dd': 31, 'ff': 29,
                  'oo': 28, 'bb': 27, 'aa': 15}
DIAGRAPH_LETTERS = {'sh': 275, 'th': 219, 'ch': 185, 'ck': 77, 'ph': 71, 'qu': 58, 'ng': 58, 'ou': 40}


def cut_tuple(tuple_list, index):
    return list(map(lambda x: x[index], tuple_list))


def random_choice(choices: dict):
    return random.choices(list(choices.keys()), weights=list(choices.values()), k=1)[0]


if __name__ == '__main__':
    word = "Tester"
    letter = Iterator([*word])

    rand_double = random_choice(DOUBLE_LETTERS)

    distribution = {}
    for _ in range(10000):
        gen = random_choice(DOUBLE_LETTERS)
        if gen in distribution.keys():
            distribution[gen] += 1
        else:
            distribution[gen] = 1

    print(sorted(distribution.items(), key=lambda x: x[1], reverse=True))

    # while letter.has_next():
    #     print(f'Letter: {letter.next()}')
