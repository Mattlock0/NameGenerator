# project imports
from src.iterator import Iterator
from src.tuning import Tuning
from src.utils import *

from symbols import *

Y_CONSONANT_CHANCE = 35  # chance for y to generate as a consonant

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

        if not self.template.has_prev() and self.beginning_ending_y and self.y_consonant:
            if weighted_choice({'': 100-Y_CONSONANT_CHANCE, 'y': Y_CONSONANT_CHANCE}) == 'y':
                # force generate a y at the end
                log.debug("Generating beginning y...")
                return 'y'

        # check for ending enforcers
        if not self.template.has_next() and self.beginning_ending_y and self.y_consonant:
            if weighted_choice({'': 100-Y_CONSONANT_CHANCE, 'y': Y_CONSONANT_CHANCE}) == 'y':
                # force generate a y at the end
                log.debug("Generating ending y...")
                return 'y'

        # add y as a consonant if checked
        if self.y_consonant:
            RARE_CONSONANTS['y'] = Y_CONSONANT_CHANCE
        else:
            if 'y' in RARE_CONSONANTS.keys():
                del RARE_CONSONANTS['y']

        # see if we can generate a common pair
        if self.template.get_next() == 'c':
            weighted_symbol_dict[Symbols.COMMON_CONSONANT_PAIR] = self.common_chance
            weighted_symbol_dict[Symbols.CONSONANT] = consonant_chance + (100 - self.common_chance)

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

        if not self.template.has_prev() and self.beginning_ending_y:
            if weighted_choice({'': 100-Y_CONSONANT_CHANCE, 'y': Y_CONSONANT_CHANCE}) == 'y':
                # force generate a y at the end
                log.debug("Generating beginning y...")
                return 'y'

        # check for ending enforcers
        if not self.template.has_next() and self.beginning_ending_y:
            if weighted_choice({'': 100-Y_CONSONANT_CHANCE, 'y': Y_CONSONANT_CHANCE}) == 'y':
                # force generate a y at the end
                log.debug("Generating ending y...")
                return 'y'

        # see if we can generate a common pair
        if self.template.get_next() == 'v':
            weighted_symbol_dict[Symbols.COMMON_VOWEL_PAIR] = self.common_chance
            weighted_symbol_dict[Symbols.CONSONANT] = vowel_chance + (100 - self.common_chance)

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
        proc_name = name

        # check for strange letter combinations here (qu must go together, Lr is odd)
        if self.qu_replace:
            # 50% chance that a u is added to q; else q is replaced
            while "q" in proc_name and "qu" not in proc_name:
                if random.randrange(100) < 50:
                    # add a u after any qs
                    proc_name = proc_name.replace('q', 'qu')
                else:
                    # or, just replace q with another consonant
                    proc_name = proc_name.replace('q', self.generate_consonant())

        if self.xs_replace:
            # 50% chance that xs is removed; else a xV pair is generated
            while "xs" in proc_name:
                if random.randrange(100) < 50:
                    proc_name = proc_name.replace('xs', self.generate_consonant() + self.generate_consonant())
                else:
                    proc_name = proc_name.replace('xs', 'x' + self.generate_vowel())  # maybe a consonant instead?

        # convert name to a list
        proc_name = list(proc_name)

        # add a chance to add a vowel onto the end
        while self.ending_j and proc_name[-1] == 'j' or self.ending_v and proc_name[-1] == 'v':
            log.debug(f"Replacing ending from {''.join(proc_name)}")
            generated = self.generate_consonant()
            proc_name[-1] = generated
        if self.ending_j or self.ending_v:
            pass

        return "".join(proc_name)
