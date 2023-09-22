# system imports
import configparser
from pathlib import Path
import logging as log
from configparser import SafeConfigParser

DEFAULTS = {'rare': '5', 'diagraph': '15', 'double': '5'}


class Config(SafeConfigParser):
    def __init__(self, config_path: Path):
        super().__init__()
        self.path = config_path
        self.read(config_path)

        try:
            self.getint('generationChances', 'rare')
            self.config_exists = True
        except configparser.NoSectionError:
            log.warning("settings.ini file not found. Continuing with defaults.")
            self.config_exists = False

    def getlist(self, section, key):
        log.trace(f"Entered: Config.{self.getlist.__name__}")
        return self.get(section, key).split(',')

    def setgen(self, key, value):
        log.trace(f"Entered: Config.{self.setgen.__name__}")
        self.set('generationChances', key, str(value))

    def setreplace(self, key, value):
        log.trace(f"Entered: Config.{self.setreplace.__name__}")
        self.set('replaceChances', key, str(value))

    def templates(self) -> list:
        log.trace(f"Entered: Config.{self.templates.__name__}")
        if self.getboolean('general', 'printAllTemplates'):
            return self.getlist('nameGeneration', 'allTemplates')
        else:
            return self.getlist('nameGeneration', 'popularTemplates')

    def create_default_config(self):
        log.trace(f"Entered: Config.{self.create_default_config.__name__}")
        # general settings
        self['general'] = {'printAllTemplates': 'no',
                           'shadingmode': 'dark'}

        # generation chances settings
        self['generationChances'] = {'rare': DEFAULTS['rare'],
                                     'diagraph': DEFAULTS['diagraph'],
                                     'double': DEFAULTS['double']}

        # replace chances settings
        self['replaceChances'] = {'qu': '25',
                                  'xs': '40'}

        # name generation settings
        self['nameGeneration'] = {'popularTemplates': 'Cvccvc,Cvccv,Cvcv,Cvcvc,Cvccvv',
                                  'allTemplates': 'Cvccvc,Cvccv,Cvcv,Cvcvc,Cvccvv,Cvcvcv,Cvcvv,Cvcvccv,Cvvcv,Vccvc,'
                                                  'Cvcvvc,Cvcc,Cvccvcv,Crvc,Cvcy',
                                  'total_random': 'no'}
