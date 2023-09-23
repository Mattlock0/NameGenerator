# system imports
from configparser import SafeConfigParser
from pathlib import Path
import logging as log

GEN_SECTION = 'generation_chances'
ENF_SECTION = 'enforcers'


class Tuning:
    def __init__(self):
        self.export = SafeConfigParser()
        self.export[GEN_SECTION] = {'rare': '5', 'diagraph': '15', 'double': '5', 'common': '0', 'qu': '25', 'xs': '40'}
        self.export[ENF_SECTION] = {'b_double': 'yes', 'e_j': 'yes', 'e_v': 'no', 'e_double': 'no', 'b_e_y': 'yes',
                                    'y_conso': 'no'}
        # self.chances = {'rare': 5, 'diagraph': 15, 'double': 5, 'common': 0, 'qu': 25, 'xs': 40}
        # self.enforcers = {'b_double': 'yes', 'e_j': 'yes', 'e_v': 'no', 'e_double': 'no', 'b_e_y': 'yes',
        #                   'y_conso': 'no'}

    def get_chance(self, section: str):
        return self.export.getint(GEN_SECTION, section)

    def get_enforcer(self, section: str):
        return True if self.export.get(ENF_SECTION, section) == 'yes' else False

    def export_tuning(self, tuning_path: Path):
        log.trace(f"Entered: Tuning.{self.export_tuning.__name__}")
        self.export[GEN_SECTION] = {
            'rare': self.export.get(GEN_SECTION, 'rare'),
            'diagraph': self.export.get(GEN_SECTION, 'diagraph'),
            'double': self.export.get(GEN_SECTION, 'double'),
            'common': self.export.get(GEN_SECTION, 'common'),
            'qu': self.export.get(GEN_SECTION, 'qu'),
            'xs': self.export.get(GEN_SECTION, 'xs')
        }
        self.export[ENF_SECTION] = {
            'b_double': self.export.get(ENF_SECTION, 'b_double'),
            'e_j': self.export.get(ENF_SECTION, 'e_j'),
            'e_v': self.export.get(ENF_SECTION, 'e_v'),
            'e_double': self.export.get(ENF_SECTION, 'e_double'),
            'b_e_y': self.export.get(ENF_SECTION, 'b_e_y'),
            'y_conso': self.export.get(ENF_SECTION, 'y_conso')
        }

        # have the user pass in a location instead
        with open(tuning_path, 'w') as configfile:
            self.export.write(configfile)

    def import_tuning(self, import_path: Path):
        log.trace(f"Entered: Tuning.{self.import_tuning.__name__}")
        log.info(f"Import Path: {import_path}")
        self.export.read(import_path)
        log.info(f"Common Chance: {self.get_chance('common')}")
