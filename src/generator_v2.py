# system imports
from enum import IntEnum
from pathlib import Path
import logging as log
import random

# project imports
from src.utils import random_choice
from src.config import Config
from src.iterator import Iterator

LITERAL_SYMBOLS = ['\\', '/', '|', '$', '@']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'r', 's', 't', 'v', 'w']
RARE_CONSONANTS = {'p': 252, 'z': 191, 'x': 71, 'q': 61, 'y': 35}
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
    def __init__(self, config_path: Path):
        self.config = Config(config_path)
        if self.config.config_exists:
            self.templates = self.config.templates()
        else:
            self.config.create_default_config()
            self.templates = ['Cvccvc', 'Cvccv', 'Cvcv', 'Cvcvc', 'Cvccvv']

        self.rare_chance = self.config.getint('generationChances', 'rare')
        self.diagraph_chance = self.config.getint('generationChances', 'diagraph')
        self.double_chance = self.config.getint('generationChances', 'double')
        self.qu_chance = self.config.getint('replaceChances', 'qu')
        self.xs_chance = self.config.getint('replaceChances', 'xs')

    def generate_consonant(self) -> str:
        log.trace(f"Entered: Generator.{self.generate_consonant.__name__}")
        # set up basic consonant chance based on other chances
        consonant_chance = 100 - self.rare_chance - self.diagraph_chance - self.double_chance

        # choose one generation type based on weights
        type_to_generate = random_choice({Symbols.CONSONANT: consonant_chance,
                                          Symbols.RARE_CONSONANT: self.rare_chance,
                                          Symbols.DIAGRAPH: self.diagraph_chance,
                                          Symbols.DOUBLE_CONSONANT: self.double_chance})

        # generate a consonant of that type
        return random_choice(ALL_SYMBOLS[type_to_generate])

    def generate_vowel(self) -> str:
        log.trace(f"Entered: Generator.{self.generate_vowel.__name__}")
        # set up basic vowel chance based on double chance
        vowel_chance = 100 - self.double_chance

        # choose one generation type based on weights
        type_to_generate = random_choice({Symbols.VOWEL: vowel_chance,
                                          Symbols.DOUBLE_VOWEL: self.double_chance})

        # generate a vowel of that type
        return random_choice(ALL_SYMBOLS[type_to_generate])

    def generate_letter(self, template: Iterator) -> str:
        log.trace(f"Entered: Generator.{self.generate_letter.__name__}")
        # check for literal symbol
        if template.curr() in LITERAL_SYMBOLS:
            # if one was passed in, return whatever the next symbol is (c, v)
            if template.has_next():
                template.next()
                return template.next()
            else:
                return template.curr()

        template_letter = template.next()
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
        log.trace(f"Entered: Generator.{self.generate_name.__name__}")
        template = Iterator([*template_raw])
        name = ""

        while template.has_next():
            name += self.generate_letter(template)

        return name  # would pass in name to process_name here

    def process_name(self, name):
        log.trace(f"Entered: Generator.{self.process_name.__name__}")
        processed_name = ""
        # check for strange letter combinations here (qu must go together, Lr is odd)
        if "q" in name and "qu" not in name:
            if random.randrange(100) < self.qu_chance:
                processed_name = name.replace("q", "qu")
            else:
                processed_name = name.replace("q", self.generate_letter('v'))
                while "q" in processed_name:
                    processed_name = name.replace("q", self.generate_letter('v'))

        return processed_name

    def save_config(self):
        log.trace(f"Entered: Generator.{self.save_config.__name__}")
        self.config.setgen('rare', self.rare_chance)
        self.config.setgen('diagraph', self.diagraph_chance)
        self.config.setgen('double', self.double_chance)
        self.config.setreplace('qu', self.qu_chance)
        self.config.setreplace('xs', self.xs_chance)

        with open(self.config.path, 'w') as configfile:
            self.config.write(configfile)
