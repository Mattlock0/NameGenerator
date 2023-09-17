from pathlib import Path
import logging as log
import configparser


class Config:
    def __init__(self, ini_file: Path):
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

    def get_templates(self) -> list:
        if self.read_bool('general', 'printAllTemplates'):
            return self.read_list('nameGeneration', 'allTemplates')
        else:
            return self.read_list('nameGeneration', 'popularTemplates')
