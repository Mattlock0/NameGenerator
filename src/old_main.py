from datetime import date
from generation import Generator
from config import Config


def print_names(generated_names):
    # making it look pretty
    if len(generated_names) == 1:
        print(f'Your name is: {generated_names[0]}!')
        file = open("../data/generatedNamesList.txt", "a")
        file.write(str(date.today()) + " |  " + generated_names[0] + "\n")
        file.close()

    elif len(generated_names) > 1:
        print(f'Your names are: ', end="")
        file = open("../data/generatedNamesList.txt", "a")
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


if __name__ == '__main__':
    print(f'Welcome to the name generator!')

    gen = Generator()  # setup generator
    config = Config('../data/settings.ini')  # setup config
    config.read_config(gen)

    # templates = config.get_templates()
    #
    #
    # ##### OLD CODE #####
    #
    # route = True  # setting up in case we aren't displaying print
    #
    # while route:
    #     choice = choose_template(templates)  # prompts user to select a template
    #     generated_names = []
    #     times = int(input('How many names would you like to generate? '))
    #
    #     for _ in range(times):
    #         generated_names.append(parse_template(gen, choice))  # sends in chosen template
    #
    #     print_names(generated_names)  # print all the names
    #
    #     if not config.read_bool('general', 'repeat'):
    #         break  # another setting that can be changed
    #
    #     cont = input('Would you like to generate more names? ')
    #     if cont == 'y' or cont == 'Y' or cont == "Yes" or cont == "yes" or cont == '1':
    #         route = 1
    #     else:
    #         route = 0
