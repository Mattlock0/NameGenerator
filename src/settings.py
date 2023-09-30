# system imports
from configparser import ConfigParser
from pathlib import Path
from typing import Any
import logging as log
import configparser

# project imports
from src.utils import func_name


class Settings:
    def __init__(self, config_path: Path):
        self._configparser = ConfigParser()
        self.path = config_path
        self.read(config_path)

        # see if we actually opened a config file
        try:
            self.get('lightmode')
        except configparser.NoSectionError:
            log.warning("settings.ini file not found. Continuing with defaults.")
            self.create_default()

    # overloaded config functions
    def read(self, filepath: str | Path) -> None:
        self._configparser.read(filepath)

    def write(self, file: Any) -> None:
        self._configparser.write(file)

    def set(self, option: str, value: str) -> None:
        self._configparser.set('general', option, value)

    def get(self, option: str) -> str:
        return self._configparser.get('general', option)

    def getint(self, option: str) -> int:
        return self._configparser.getint('general', option)

    def getboolean(self, option: str) -> bool:
        return self._configparser.getboolean('general', option)

    # Settings-specific functions
    def getlist(self, option: str) -> list:
        log.trace(f"Entered: Settings.{func_name()}")
        return self.get(option).split(',')

    def create_default(self):
        log.trace(f"Entered: Settings.{func_name()}")
        self._configparser['general'] = {'templates': 'Cvccvc,Cvccv,Cvcv,Cvcvc,Cvccvv',
                                         'archive_separator': '|',
                                         'archive_names': 'no',
                                         'lightmode': 'no',
                                         'font_size': '15'}

    def save(self):
        log.trace(f"Entered: Settings.{func_name()}")
        log.info(f"Saving settings to file...")

        with open(self.path, 'w') as configfile:
            self.write(configfile)
