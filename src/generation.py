import random


class Generator:
    def __init__(self):
        self.literal_flag = False
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w']
        self.rare_consonants = ['j', 'q', 'x', 'z']
        self.double_letters = ['e', 'l', 'n', 'o', 's', 't']  # maybe r's?
        self.diagraph_letters = ['c', 's', 't', 'w', 'q']  # maybe ck and ph?

        # chance defaults, overloaded by read_config
        self.rare_chance = 8
        self.double_chance = 13
        self.qu_chance = 7
        self.diagraph_chance = 15

    def chance(self, gen):
        if gen == 'r':
            return True if random.randrange(100) < self.rare_chance else False
        elif gen == 'd':
            return True if random.randrange(100) < self.double_chance else False
        elif gen == 'q':
            return True if random.randrange(100) < self.qu_chance else False
        elif gen == 'g':
            return True if random.randrange(100) < self.diagraph_chance else False

    def generate_consonant(self, is_upper):
        if is_upper:  # letter is upper case
            gen_let = random.choice(self.consonants).upper()  # generate a basic uppercase consonant
            gen_let = random.choice(self.rare_consonants).upper() if self.chance('r') else gen_let  # rare chance
            if gen_let.lower() in self.diagraph_letters and self.chance('g'):  # check for diagraph if possible
                gen_let = gen_let + 'u' if gen_let == 'Q' else gen_let + 'h'  # add the appropriate letter on

            return gen_let  # finally, return the letter

        # letter is lower case
        gen_let = random.choice(self.consonants)
        gen_let = random.choice(self.rare_consonants) if self.chance('r') else gen_let
        if gen_let in self.diagraph_letters and self.chance('g'):
            gen_let = gen_let + 'u' if gen_let == 'q' else gen_let + 'h'
        elif gen_let in self.double_letters and self.chance('d'):  # potentially create double letter
            gen_let = gen_let + gen_let

        return gen_let

    def generate_vowel(self, is_upper):
        if is_upper:  # letter is upper case
            return random.choice(self.vowels).upper()  # return a basic uppercase vowel

        # letter is lower case
        gen_let = random.choice(self.vowels)
        if gen_let in self.double_letters and self.chance('d'):  # potentially create a double letter
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
            return random.choice(self.consonants + self.rare_consonants + self.vowels)
        else:
            return let  # it is not a generated letter and we send it back literally


def parse_template(gen: Generator, template: str):
    letters = ([*template])  # parse the template into a list of its letters
    name = ""

    for letter in letters:
        name += gen.generate_letter(letter)

    return name  # would pass in name to process_name here


def process_name(gen, name):
    processed_name = ""
    # check for strange letter combinations here (qu must go together, Lr is odd)
    if "q" in name and "qu" not in name:
        if gen.chance('q'):  # currently a 7% chance
            processed_name = name.replace("q", "qu")
        else:
            processed_name = name.replace("q", gen.generate_letter('v'))
            while "q" in processed_name:
                processed_name = name.replace("q", gen.generate_letter('v'))

    return processed_name
