import configparser
import logging as log


class Config:
    def __init__(self, ini_file):
        self.config_f = configparser.ConfigParser()
        self.config_f.read(ini_file)
        self.read_config_file = True

    def read_config(self, gen) -> bool:
        sec1 = 'letterGeneration'

        try:  # have to store the failure in case the settings file was misplaced
            gen.rare_chance = self.read_int(sec1, 'rare_chance')
        except configparser.NoSectionError:
            log.error("settings.ini file not found. Continuing with defaults.")
            self.read_config_file = False
            return False

        gen.double_chance = self.read_int(sec1, 'double_chance')
        gen.qu_chance = self.read_int(sec1, 'qu_chance')
        gen.diagraph_chance = self.read_int(sec1, 'diagraph_chance')
        return True

    def read(self, section, key):
        return self.config_f[section][key]

    def read_bool(self, section, key):
        return self.config_f.getboolean(section, key)

    def read_int(self, section, key):
        return self.config_f.getint(section, key)

    def read_list(self, section, key):
        return self.config_f.get(section, key).split(',')

    def print_config(self):
        for section_name in self.config_f.sections():
            print('Section: ', section_name)
            print('\tOptions: ', self.config_f.options(section_name))

            for name, value in self.config_f.items(section_name):
                print('\t%s: %s' % (name, value))
        # full example, separate per section

    def change_chances(self):
        # have this print out for any setting (parse options into a dict)

        sec = "letterGeneration"

        print(f'--==Current Chances==--\n'
              f'1) Rare Consonants:\t\t{self.config_f.get(sec, "rare_chance")}%\n'
              f'2) Double Letters:\t\t{self.config_f.get(sec, "double_chance")}%\n'
              f'3) Qu Replacement:\t\t{self.config_f.get(sec, "qu_chance")}%\n'
              f'4) Diagraphs:\t\t\t{self.config_f.get(sec, "diagraph_chance")}%')

        chances = {1: "rare_chance", 2: "double_chance", 3: "qu_chance", 4: "diagraph_chance"}
        inp = int(input('Which percentage would you like to change? '))

        while inp < 1 or inp > 4:
            inp = int(input('Improper input. Enter your choice: '))

        new_percent = input('Enter new percentage: ')
        self.config_f.set(sec, chances.get(inp), new_percent)
        self.config_f.write('../data/settings.ini')

        print(f'Read-in percentage: {self.config_f.get(sec, chances.get(inp))}')

    def change_settings(self):
        # print(f'Settings sections: {self.config_f.sections()}')
        self.print_config()
        sec = input('Investigate which section? ')

        while sec not in self.config_f.sections():
            sec = input('Improper input. Enter name of section: ')

        #print(f'Settings in {sec}: {self.r_config.items(sec)}')
        if sec == 'letterGeneration':
            self.change_chances()

    def get_templates(self) -> list:
        if self.read_bool('general', 'printAllTemplates'):
            return self.read_list('nameGeneration', 'allTemplates')
        else:
            return self.read_list('nameGeneration', 'popularTemplates')
