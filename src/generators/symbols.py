from enum import IntEnum

LITERAL_SYMBOLS = ['\\', '/', '|', '$', '@']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'r', 's', 't', 'v', 'w']
RARE_CONSONANTS = {'p': 252, 'z': 191, 'x': 71, 'q': 61}  # q should be quite low because by itself it appeared thrice
DIAGRAPHS = {'sh': 275, 'th': 219, 'ch': 185, 'ck': 77, 'ph': 71, 'qu': 58, 'ng': 58}
DOUBLE_CONSONANTS = {'ll': 398, 'nn': 310, 'tt': 199, 'rr': 157, 'ss': 126, 'mm': 44, 'dd': 31, 'ff': 29, 'bb': 27}
COMMON_CONSONANT_PAIRS = {'nd': 249, 'st': 238, 'ly': 193, 'rl': 190, 'br': 142, 'rt': 139, 'rd': 134, 'nt': 130,
                          'rn': 107, 'ld': 96, 'dr': 96, 'tr': 88, 'nc': 83, 'cl': 78, 'fr': 62, 'rm': 57, 'lm': 56,
                          'rg': 56, 'lv': 55}  # should ly really be in here?

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
DOUBLE_VOWELS = {'ee': 152, 'oo': 28, 'aa': 15}
COMMON_VOWEL_PAIRS = {'ie': 586, 'ia': 369, 'ey': 193, 'ay': 180, 'ea': 157, 'ai': 143, 'ya': 120, 'au': 105, 'io': 99,
                      'eo': 80, 'ae': 59, 'ue': 57, 'ei': 55}

ALL_SYMBOLS = [CONSONANTS, RARE_CONSONANTS, DIAGRAPHS, DOUBLE_CONSONANTS, COMMON_CONSONANT_PAIRS, VOWELS, DOUBLE_VOWELS,
               COMMON_VOWEL_PAIRS]


class Symbols(IntEnum):
    CONSONANT = 0
    RARE_CONSONANT = 1
    DIAGRAPH = 2
    DOUBLE_CONSONANT = 3
    COMMON_CONSONANT_PAIR = 4
    VOWEL = 5
    DOUBLE_VOWEL = 6
    COMMON_VOWEL_PAIR = 7