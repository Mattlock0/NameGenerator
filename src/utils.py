# system imports
from collections import namedtuple
from enum import IntEnum
from PyQt5 import QtGui
import logging as log
import random
import inspect

Mode = namedtuple('Mode', 'type background text border light_border hover edit')

DARKMODE = Mode('darkmode', 'rgb(43, 46, 51)', 'rgb(235, 235, 235)', 'rgb(29, 29, 29)', 'rgb(49, 49, 49)',
                'rgb(50, 54, 60)', 'rgb(42, 45, 50)')

LIGHTMODE = Mode('lightmode', 'rgb(235, 235, 235)', 'rgb(62, 65, 73)', 'rgb(215, 215, 215)', 'rgb(207, 207, 207)',
                 'rgb(222, 222, 222)', 'rgb(230, 230, 230)')


class Border(IntEnum):
    INSET = 0
    HOVER = 1
    OUTSET = 2


def random_choice(choices):
    log.trace(f"Entered: utils.{random_choice.__name__}")
    if type(choices) == list:
        return random.choice(choices)
    return random.choices(list(choices.keys()), weights=list(choices.values()), k=1)[0]


def get_font(pt_size):
    log.trace(f"Entered: utils.{get_font.__name__}")
    font = QtGui.QFont()
    font.setFamily("Segoe UI Black")
    font.setPointSize(pt_size)
    font.setWeight(75)

    return font


def get_border(border_type: Border, shading: Mode) -> str:
    match border_type:
        case Border.INSET:
            return (
                f"border-radius: 5px; "
                f"border-bottom: 1px solid {shading.light_border}; border-right: 1px solid {shading.light_border}; "
                f"border-left: 2px solid {shading.border}; border-top: 2px solid {shading.border}\n")
        case Border.HOVER:
            return (
                f"border-radius: 5px; "
                f"border-top: 1px solid {shading.light_border}; border-left: 1px solid {shading.light_border}; border"
                f"-right: 2px solid {shading.border}; border-bottom: 2px solid {shading.border}\n")
        case Border.OUTSET:
            return (
                f"border-radius: 5px; "
                f"border-top: 1px solid {shading.light_border}; border-left: 1px solid {shading.light_border}; border"
                f"-right: 3px solid {shading.border}; border-bottom: 3px solid {shading.border}\n")


def style_button(shading: Mode) -> str:
    outset_border = get_border(Border.OUTSET, shading)
    hover_border = get_border(Border.HOVER, shading)
    inset_border = get_border(Border.INSET, shading)

    return ("QPushButton {\n"
            f"color: {shading.text};\n"
            "border-style: outset;\n"
            f"{outset_border}"
            "}\n"
            "QPushButton:hover {\n"
            f"background-color: {shading.hover};\n"
            f"color: {shading.text};\n"
            "border-style: outset;\n"
            f"{hover_border}"
            "}\n"
            "QPushButton:pressed {\n"
            f"color: {shading.text};\n"
            "border-style: inset;\n"
            f"{inset_border}"
            "}\n")


def func_name():
    return inspect.currentframe().f_back.f_code.co_name


def add_log_level(level_name, level_num, method_name=None):
    """
    Comprehensively adds a new logging level to the `logging` module and the
    currently configured logging class.

    `levelName` becomes an attribute of the `logging` module with the value
    `levelNum`. `methodName` becomes a convenience method for both `logging`
    itself and the class returned by `logging.getLoggerClass()` (usually just
    `logging.Logger`). If `methodName` is not specified, `levelName.lower()` is
    used.

    To avoid accidental clobbering of existing attributes, this method will
    raise an `AttributeError` if the level name is already an attribute of the
    `logging` module or if the method name is already present
    """
    if not method_name:
        method_name = level_name.lower()

    if hasattr(log, level_name):
        raise AttributeError('{} already defined in log module'.format(level_name))
    if hasattr(log, method_name):
        raise AttributeError('{} already defined in log module'.format(method_name))
    if hasattr(log.getLoggerClass(), method_name):
        raise AttributeError('{} already defined in logger class'.format(method_name))

    def log_for_level(self, message, *args, **kwargs):
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs)

    def log_to_root(message, *args, **kwargs):
        log.log(level_num, message, *args, **kwargs)

    log.addLevelName(level_num, level_name)
    setattr(log, level_name, level_num)
    setattr(log.getLoggerClass(), method_name, log_for_level)
    setattr(log, method_name, log_to_root)
