# project imports
from src.iterator import Iterator
from src.tuning import Tuning
from src.utils import *

LITERAL_SYMBOLS = ['\\', '/', '|', '$', '@']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'r', 's', 't', 'v', 'w']
RARE_CONSONANTS = {'p': 252, 'z': 191, 'x': 71, 'q': 61}  # q should be quite low because by itself it appeared thrice
DIAGRAPHS = {'sh': 275, 'th': 219, 'ch': 185, 'ck': 77, 'ph': 71, 'qu': 58, 'ng': 58}
DOUBLE_CONSONANTS = {'ll': 398, 'nn': 310, 'tt': 199, 'rr': 157, 'ss': 126, 'mm': 44, 'dd': 31, 'ff': 29, 'bb': 27}
COMMON_CONSONANT_PAIRS = {'nd': 249, 'st': 238, 'ly': 193, 'rl': 190, 'br': 142, 'rt': 139, 'rd': 134, 'nt': 130,
                          'rn': 107, 'ld': 96, 'dr': 96, 'tr': 88, 'nc': 83, 'cl': 78, 'fr': 62, 'rm': 57, 'lm': 56,
                          'rg': 56, 'lv': 55}

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


class Generator:
    def __init__(self):
        self.template = Iterator([])
        self.tuning = Tuning()
        self.double_flag = False

        # chances
        self.rare_chance, self.diagraph_chance, self.double_chance, self.common_chance = 0, 0, 0, 0

        # enforcers
        (self.beginning_double, self.ending_j, self.ending_v, self.ending_double, self.beginning_ending_y,
         self.y_consonant, self.qu_replace, self.xs_replace) = False, False, False, False, False, False, False, False

        self.read_tunings()

    def read_tunings(self):
        log.trace(f"Entered: Generator.{func_name()}")
        self.rare_chance = self.tuning.get_chance('rare')
        self.diagraph_chance = self.tuning.get_chance('diagraph')
        self.double_chance = self.tuning.get_chance('double')
        self.common_chance = self.tuning.get_chance('common')

        # enforcers
        self.beginning_double = self.tuning.get_enforcer('b_double')
        self.ending_j = self.tuning.get_enforcer('e_j')
        self.ending_v = self.tuning.get_enforcer('e_v')
        self.ending_double = self.tuning.get_enforcer('e_double')
        self.beginning_ending_y = self.tuning.get_enforcer('b_e_y')
        self.y_consonant = self.tuning.get_enforcer('y_conso')
        self.qu_replace = self.tuning.get_enforcer('qu')
        self.xs_replace = self.tuning.get_enforcer('xs')

    def generate_consonant(self) -> str:
        log.trace(f"Entered: Generator.{func_name()}")
        # set up basic consonant chance based on other chances
        consonant_chance = 300 - self.rare_chance - self.diagraph_chance - self.double_chance
        weighted_symbol_dict = {Symbols.CONSONANT: consonant_chance, Symbols.RARE_CONSONANT: self.rare_chance,
                                Symbols.DIAGRAPH: self.diagraph_chance, Symbols.DOUBLE_CONSONANT: self.double_chance}

        # check for beginning enforcers or whether we've already generated double letters this name
        if not self.template.has_prev() and self.beginning_double or self.double_flag:
            del weighted_symbol_dict[Symbols.DOUBLE_CONSONANT]

        # add y as a consonant if checked
        if self.y_consonant:
            RARE_CONSONANTS['y'] = 35
        else:
            if 'y' in RARE_CONSONANTS.keys():
                del RARE_CONSONANTS['y']

        # see if we can generate a common pair
        if self.template.get_next() == 'c':
            weighted_symbol_dict[Symbols.COMMON_CONSONANT_PAIR] = self.common_chance

        # choose one generation type based on weights
        symbol_type = weighted_choice(weighted_symbol_dict)

        # if we chose a pair, move the marker up twice
        if symbol_type == Symbols.COMMON_CONSONANT_PAIR:
            log.debug('Generating a common pair...')
            self.template.next()
        elif symbol_type == Symbols.DOUBLE_CONSONANT:
            self.double_flag = True

        # generate a consonant of that type
        return weighted_choice(ALL_SYMBOLS[symbol_type])

    def generate_vowel(self) -> str:
        log.trace(f"Entered: Generator.{func_name()}")
        # set up basic vowel chance based on double chance
        vowel_chance = 100 - self.double_chance
        weighted_symbol_dict = {Symbols.VOWEL: vowel_chance, Symbols.DOUBLE_VOWEL: self.double_chance}

        # check for beginning enforcers or whether we've already generated double letters this name
        if not self.template.has_prev() and self.beginning_double or self.double_flag:
            del weighted_symbol_dict[Symbols.DOUBLE_VOWEL]
            weighted_symbol_dict[Symbols.VOWEL] = 100

        # see if we can generate a common pair
        if self.template.get_next() == 'v':
            weighted_symbol_dict[Symbols.COMMON_VOWEL_PAIR] = self.common_chance

        # choose one generation type based on weights
        symbol_type = weighted_choice(weighted_symbol_dict)

        # if we chose a pair, move the marker up twice
        if symbol_type == Symbols.COMMON_VOWEL_PAIR:
            log.debug('Generating a common pair...')
            self.template.next()
        elif symbol_type == Symbols.DOUBLE_VOWEL:
            self.double_flag = True

        # generate a vowel of that type
        return weighted_choice(ALL_SYMBOLS[symbol_type])

    def generate_letter(self) -> str:
        log.trace(f"Entered: Generator.{func_name()}")

        # check for literal symbol
        if self.template.curr() in LITERAL_SYMBOLS:
            log.debug("Literal symbol read, skipping letter...")
            # if one was passed in, return whatever the next symbol is (c, v)
            if self.template.has_prev():
                self.template.next()
                return self.template.next()
            else:
                return self.template.curr()

        template_letter = self.template.curr()

        if template_letter.lower() == 'c':
            generated_symbol = self.generate_consonant()
        elif template_letter.lower() == 'v':
            generated_symbol = self.generate_vowel()
        elif template_letter == '*':
            generated_symbol = random.choice([self.generate_vowel(), self.generate_consonant()])
        else:  # no template letter was passed in; generate nothing
            generated_symbol = template_letter

        if template_letter.isupper():
            return generated_symbol.title()
        else:
            return generated_symbol

    def generate_name(self, template_raw: str):
        log.trace(f"Entered: Generator.{func_name()}")
        self.template, self.double_flag = Iterator([*template_raw]), False
        name = ""

        while True:
            log.trace(f"Template progress: {self.template}")
            name += self.generate_letter()

            if not self.template.has_next():
                break
            self.template.next()

        return self.process_name(name)  # would pass in name to process_name here

    def process_name(self, name):
        log.trace(f"Entered: Generator.{func_name()}")
        proc_name = list(name)

        # add a chance to add a vowel onto the end
        if self.ending_j or self.ending_v:
            while self.ending_j and proc_name[-1] == 'j' or self.ending_v and proc_name[-1] == 'v':
                log.debug(f"Replacing ending from {name}")
                generated = self.generate_consonant()
                log.debug(f"Replacement: {generated}")
                proc_name[-1] = generated

        proc_name = "".join(proc_name)

        # check for strange letter combinations here (qu must go together, Lr is odd)
        if self.qu_replace and "q" in proc_name and "qu" not in proc_name:
            # check for a u after any qs
            proc_name = proc_name.replace('q', 'qu')

        # allow for the chance to replace q with a different consonant
        # if random.randrange(100) < 50:
        #     processed_name = name.replace("q", self.generate_consonant())
        #     while "q" in processed_name:
        #         processed_name = name.replace("q", self.generate_consonant())

        return "".join(proc_name)
