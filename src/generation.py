import random

VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w']
RARE_CONSONANTS = ['j', 'q', 'x', 'z']
DOUBLE_LETTERS = ['e', 'l', 'n', 'o', 's', 't']  # maybe r's?
DIAGRAPH_LETTERS = ['c', 's', 't', 'w', 'q']  # maybe ck and ph?


class Generator:
    def __init__(self):
        self.literal_flag = False

        # chance defaults, overloaded by read_config
        self.rare_chance = 8
        self.double_chance = 13
        self.qu_chance = 7
        self.diagraph_chance = 15

    def chance(self, gen: str) -> bool:
        if gen == 'r':
            return True if random.randrange(100) < self.rare_chance else False
        elif gen == 'd':
            return True if random.randrange(100) < self.double_chance else False
        elif gen == 'q':
            return True if random.randrange(100) < self.qu_chance else False
        elif gen == 'g':
            return True if random.randrange(100) < self.diagraph_chance else False

    def generate_consonant(self, is_upper: bool) -> str:
        if is_upper:  # letter is upper case
            gen_let = random.choice(CONSONANTS).upper()  # generate a basic uppercase consonant
            gen_let = random.choice(RARE_CONSONANTS).upper() if self.chance('r') else gen_let  # rare chance
            if gen_let.lower() in DIAGRAPH_LETTERS and self.chance('g'):  # check for diagraph if possible
                gen_let = gen_let + 'u' if gen_let == 'Q' else gen_let + 'h'  # add the appropriate letter on

            return gen_let  # finally, return the letter

        # letter is lower case
        gen_let = random.choice(CONSONANTS)
        gen_let = random.choice(RARE_CONSONANTS) if self.chance('r') else gen_let
        if gen_let in DIAGRAPH_LETTERS and self.chance('g'):
            gen_let = gen_let + 'u' if gen_let == 'q' else gen_let + 'h'
        elif gen_let in DOUBLE_LETTERS and self.chance('d'):  # potentially create double letter
            gen_let = gen_let + gen_let

        return gen_let

    def generate_vowel(self, is_upper):
        if is_upper:  # letter is upper case
            return random.choice(VOWELS).upper()  # return a basic uppercase vowel

        # letter is lower case
        gen_let = random.choice(VOWELS)
        if gen_let in DOUBLE_LETTERS and self.chance('d'):  # potentially create a double letter
            gen_let = gen_let + gen_let

        return gen_let

    def generate_letter(self, let):
        if let == "\\" or let == "/":  # check for literal slashes
            literal_flag = True  # if so, set the flag to True
            return ""
        elif self.literal_flag:  # we just read in a slash
            literal_flag = False
            return let  # return the letter literally

        if let.lower() == 'c':  # we need to generate a consonant
            return self.generate_consonant(let.isupper())
        elif let.lower() == 'v':  # we need to generate a vowel
            return self.generate_vowel(let.isupper())
        elif let == '*':  # we need any letter
            return random.choice(CONSONANTS + RARE_CONSONANTS + VOWELS)
        else:
            return let  # it is not a generated letter and we send it back literally

    def parse_template(self, template: str):
        letters = ([*template])  # parse the template into a list of its letters
        name = ""

        for letter in letters:
            name += self.generate_letter(letter)

        return name  # would pass in name to process_name here

    def process_name(self, name):
        processed_name = ""
        # check for strange letter combinations here (qu must go together, Lr is odd)
        if "q" in name and "qu" not in name:
            if self.chance('q'):  # currently a 7% chance
                processed_name = name.replace("q", "qu")
            else:
                processed_name = name.replace("q", self.generate_letter('v'))
                while "q" in processed_name:
                    processed_name = name.replace("q", self.generate_letter('v'))

        return processed_name
