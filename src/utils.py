# system imports
import random
import logging as log


def random_choice(choices):
    log.trace(f"Entered: utils.{random_choice.__name__}")
    if type(choices) == list:
        return random.choice(choices)
    return random.choices(list(choices.keys()), weights=list(choices.values()), k=1)[0]


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
