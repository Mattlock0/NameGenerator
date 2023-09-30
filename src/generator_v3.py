# system imports
from pathlib import Path

# project imports
from src.iterator import Iterator
from src.tuning import Tuning
from src.utils import *

LITERAL_SYMBOLS = ['\\', '/', '|', '$', '@']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'r', 's', 't', 'v', 'w']
RARE_CONSONANTS = {'p': 252, 'z': 191, 'x': 71, 'q': 61}  # 'y': 35
DIAGRAPHS = {'sh': 275, 'th': 219, 'ch': 185, 'ck': 77, 'ph': 71, 'qu': 58, 'ng': 58}
DOUBLE_CONSONANTS = {'ll': 398, 'nn': 310, 'tt': 199, 'rr': 157, 'ss': 126, 'mm': 44, 'dd': 31, 'ff': 29, 'bb': 27}
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
DOUBLE_VOWELS = {'ee': 152, 'oo': 28, 'aa': 15}

ALL_SYMBOLS = [CONSONANTS, RARE_CONSONANTS, DIAGRAPHS, DOUBLE_CONSONANTS, VOWELS, DOUBLE_VOWELS]


class Symbols(IntEnum):
    CONSONANT = 0
    RARE_CONSONANT = 1
    DIAGRAPH = 2
    DOUBLE_CONSONANT = 3
    VOWEL = 4
    DOUBLE_VOWEL = 5


class Generator:
    def __init__(self):
        self.tuning = Tuning()
        self.template = None

        # chances
        self.rare_chance, self.diagraph_chance, self.double_chance, self.common_chance, self.qu_chance, self.xs_chance \
            = 0, 0, 0, 0, 0, 0

        # enforcers
        (self.beginning_double, self.ending_j, self.ending_v, self.ending_double, self.beginning_ending_y,
         self.y_consonant) = False, False, False, False, False, False

        self.read_tunings()

    def read_tunings(self):
        log.trace(f"Entered: Generator.{func_name()}")
        self.rare_chance = self.tuning.get_chance('rare')
        self.diagraph_chance = self.tuning.get_chance('diagraph')
        self.double_chance = self.tuning.get_chance('double')
        self.common_chance = self.tuning.get_chance('common')
        self.qu_chance = self.tuning.get_chance('qu')
        self.xs_chance = self.tuning.get_chance('xs')

        # enforcers
        self.beginning_double = self.tuning.get_enforcer('b_double')
        self.ending_j = self.tuning.get_enforcer('e_j')
        self.ending_v = self.tuning.get_enforcer('e_v')
        self.ending_double = self.tuning.get_enforcer('e_double')
        self.beginning_ending_y = self.tuning.get_enforcer('b_e_y')
        self.y_consonant = self.tuning.get_enforcer('y_conso')

    def generate_consonant(self) -> str:
        log.trace(f"Entered: Generator.{func_name()}")
        # set up basic consonant chance based on other chances
        consonant_chance = 300 - self.rare_chance - self.diagraph_chance - self.double_chance
        weighted_symbol_dict = {Symbols.CONSONANT: consonant_chance, Symbols.RARE_CONSONANT: self.rare_chance,
                                Symbols.DIAGRAPH: self.diagraph_chance, Symbols.DOUBLE_CONSONANT: self.double_chance}

        # check for beginning enforcers
        if not self.template.has_prev():
            if self.beginning_double:
                del weighted_symbol_dict[Symbols.DOUBLE_CONSONANT]

        # add y as a consonant if checked
        if self.y_consonant:
            RARE_CONSONANTS['y'] = 35
        else:
            if 'y' in RARE_CONSONANTS.keys():
                del RARE_CONSONANTS['y']

        # choose one generation type based on weights
        symbol_type = weighted_choice(weighted_symbol_dict)

        if not self.template.has_prev():
            if self.beginning_double:
                if symbol_type == Symbols.DOUBLE_CONSONANT:
                    log.error("Bogus, man!")

        # generate a consonant of that type
        return weighted_choice(ALL_SYMBOLS[symbol_type])

    def generate_vowel(self) -> str:
        log.trace(f"Entered: Generator.{func_name()}")
        # set up basic vowel chance based on double chance
        vowel_chance = 100 - self.double_chance
        weighted_symbol_dict = {Symbols.VOWEL: vowel_chance, Symbols.DOUBLE_VOWEL: self.double_chance}

        # check for beginning enforcers
        if not self.template.has_prev():
            if self.beginning_double:
                del weighted_symbol_dict[Symbols.DOUBLE_VOWEL]

        # choose one generation type based on weights
        symbol_type = weighted_choice(weighted_symbol_dict)

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
        log.trace(f"Template progress: {self.template}")

        if template_letter.lower() == 'c':
            generated_symbol = self.generate_consonant()
        elif template_letter.lower() == 'v':
            generated_symbol = self.generate_vowel()
        elif template_letter == '*':
            generated_symbol = random.choice([self.generate_vowel(), self.generate_consonant()])
        else:  # no template letter was passed in; generate nothing
            generated_symbol = template_letter

        self.template.next()
        if template_letter.isupper():
            return generated_symbol.title()
        else:
            return generated_symbol

    def generate_name(self, template_raw: str):
        log.trace(f"Entered: Generator.{func_name()}")
        self.template = Iterator([*template_raw])
        name = ""

        while self.template.has_next():
            name += self.generate_letter()

        return name  # would pass in name to process_name here

    def process_name(self, name):
        log.trace(f"Entered: Generator.{func_name()}")
        processed_name = ""
        # check for strange letter combinations here (qu must go together, Lr is odd)
        if "q" in name and "qu" not in name:
            if random.randrange(100) < self.qu_chance:
                processed_name = name.replace("q", "qu")
            else:
                processed_name = name.replace("q", self.generate_vowel())
                while "q" in processed_name:
                    processed_name = name.replace("q", self.generate_vowel())

        return processed_name
