from datetime import date
from generation import generator
from config import config

#  most common english letters:  e, t, a, i, o, n, s, h, r
#  most common starting letters: t, a, o, d, w
#  most common ending letters:   e, s, d, t
#  english diagraphs:            ch, sh, th, wh, qu [ck, ph?]

#  TO-DO
#  Add a grab bag choice (with any template)?
#  Let users change settings
#  Potential: replace letters from certain combinations (with process_name)
#  Potential: add name meanings (prefixes & suffixes)


def parse_template(gen, template):
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


def print_names(generated_names):
    # making it look pretty
    if len(generated_names) == 1:
        print(f'Your name is: {generated_names[0]}!')
        file = open("generatedNamesList.txt", "a")
        file.write(str(date.today()) + " |  " + generated_names[0] + "\n")
        file.close()

    elif len(generated_names) > 1:
        print(f'Your names are: ', end="")
        file = open("generatedNamesList.txt", "a")
        file.write(str(date.today()) + " |  ")  # line header

        for name in generated_names:
            if name == generated_names[-1]:
                print(f'and {name}!')
                file.write(name + "\n")
            else:
                print(f'{name}, ', end="")
                file.write(name + ", ")
        file.close()
    else:
        print(f'You don\'t want any names...? :(')


def choose_template(templates):
    print(f'Please select a template from the ones below.')
    print(f'KEY: c = consonant | v = vowel | * = literal letter')

    # prints all templates in order
    for x in range(len(templates)):
        print(f'{str(x + 1)}) {templates[x]}')
    print(f'{str(len(templates) + 1)}) Custom')

    # allows user to choose which template they would like
    choice = int(input('Enter the corresponding number: '))
    while choice > len(templates) + 1 or choice < 1:
        print(f'Improper selection. Make another.')
        choice = int(input('Enter the corresponding number: '))

    # Checks between custom and prebuilt templates
    if choice == len(templates) + 1:
        selected = input('Enter your template (/ to force a letter): ')
    else:
        selected = templates[choice - 1]  # the list is always off by one

    return selected


if __name__ == '__main__':
    print(f'Welcome to the name generator!')

    gen = generator()  # setup generator
    config = config('settings.ini')  # setup config

    if config.read_bool('general', 'printAllTemplates'):
        templates = config.read_list('nameGeneration', 'allTemplates')
    else:
        templates = config.read_list('nameGeneration', 'popularTemplates')

    route = 1  # setting up in case we aren't displaying print

    if config.read_bool('general', 'displaySettings'):  # if we give the settings option to users
        print(f'Would you like to...')
        print(f'1) Generate a name')
        print(f'2) Change the settings')

        to_print = config.read_bool('general', 'displayPrint')
        if to_print:
            print(f'3) See all generated names')

        route = int(input('Enter your choice: '))
        while route < 1 or (not to_print and route > 2) or (to_print and route > 3):  # trust me, it's right.
            print(f'Improper selection. Make another.')
            route = int(input('Enter your choice: '))

        if route == 2:
            config.change_settings()
            quit()

        if route == 3:
            file = open("generatedNamesList.txt", "r")
            print(file.read())
            quit()

    while route:
        choice = choose_template(templates)  # prompts user to select a template
        generated_names = []
        times = int(input('How many names would you like to generate? '))

        for _ in range(times):
            generated_names.append(parse_template(gen, choice))  # sends in chosen template

        print_names(generated_names)  # print all the names

        if not config.read_bool('general', 'repeat'):
            break  # another setting that can be changed

        cont = input('Would you like to generate more names? ')
        if cont == 'y' or cont == 'Y' or cont == "Yes" or cont == "yes" or cont == '1':
            route = 1
        else:
            route = 0
