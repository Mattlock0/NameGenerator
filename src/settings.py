# system imports
from configparser import SafeConfigParser
from pathlib import Path
from typing import Any
import logging as log
import configparser

# project imports
from src.utils import func_name


class Settings:
    def __init__(self, config_path: Path):
        self.s = SafeConfigParser()
        self.path = config_path
        self.read(config_path)

        try:
            self.get('lightmode')
        except configparser.NoSectionError:
            log.warning("settings.ini file not found. Continuing with defaults.")
            self.create_default()

    # overloaded config functions
    def read(self, filepath: str | Path) -> None:
        self.s.read(filepath)

    def write(self, file: Any) -> None:
        self.s.write(file)

    def set(self, option: str, value: str) -> None:
        self.s.set('general', option, value)

    def get(self, option: str) -> str:
        return self.s.get('general', option)

    def getint(self, option: str) -> int:
        return self.s.getint('general', option)

    def getboolean(self, option: str) -> bool:
        return self.s.getboolean('general', option)

    # Settings-specific functions
    def getlist(self, option: str) -> list:
        log.trace(f"Entered: Settings.{func_name()}")
        return self.get(option).split(',')

    def create_default(self):
        log.trace(f"Entered: Settings.{func_name()}")
        self.s['general'] = {'lightmode': 'no',
                             'fontsize': '15',
                             'templates': 'Cvccvc,Cvccv,Cvcv,Cvcvc,Cvccvv',
                             'archivenames': 'yes'}

    def save(self):
        log.trace(f"Entered: Settings.{func_name()}")
        log.info(f"Saving settings to file...")

        log.warning(f"Settings filepath: {self.path}")

        with open(self.path, 'w') as configfile:
            self.write(configfile)
