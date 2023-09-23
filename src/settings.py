# system imports
from configparser import SafeConfigParser
from pathlib import Path
import logging as log
import configparser


class Settings(SafeConfigParser):
    def __init__(self, config_path: Path):
        super().__init__()
        self.path = config_path
        self.read(config_path)

        try:
            self.get('general', 'shadingmode')
        except configparser.NoSectionError:
            log.warning("settings.ini file not found. Continuing with defaults.")

    def getlist(self, section, key):
        log.trace(f"Entered: Config.{self.getlist.__name__}")
        return self.get(section, key).split(',')

    def gettemplates(self) -> list:
        log.trace(f"Entered: Config.{self.gettemplates.__name__}")
        return self.getlist('nameGeneration', 'templates')

    def create_default(self):
        log.trace(f"Entered: Config.{self.create_default.__name__}")
        # general settings
        self['general'] = {'shadingmode': 'dark',
                           'fontsize': '15'}

        # name generation settings
        self['nameGeneration'] = {'templates': 'Cvccvc,Cvccv,Cvcv,Cvcvc,Cvccvv',
                                  'archivenames': 'yes'}

    def save(self):
        log.trace(f"Entered: Config.{self.save.__name__}")
        log.info(f"Saving settings to file...")

        with open(self.path, 'w') as configfile:
            self.write(configfile)
