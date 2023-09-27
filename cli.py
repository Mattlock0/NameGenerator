# system imports
from pathlib import Path
import logging as log

# project imports
from src.__main__ import main
from src.utils import add_log_level

#  NAME INFORMATION  #
#  most common english letters:  e, t, a, i, o, n, s, h, r
#  most common starting letters: t, a, o, d, w
#  most common ending letters:   e, s, d, t

# PROJECT CONSTANTS
BUILD_CONFIG_PATH, RUN_CONFIG_PATH = 'settings.ini', 'data/settings.ini'
CONFIG_PATH = Path(RUN_CONFIG_PATH)
add_log_level('TRACE', log.DEBUG - 5)
LOG_LEVEL = log.TRACE
VERSION = 'v1.1'

if __name__ == '__main__':
    # set up logging
    log.basicConfig(format="[%(levelname)s] %(message)s", level=LOG_LEVEL)
    log.info("Starting Mattlock's Name Generator!")

    # run main application
    main(CONFIG_PATH, VERSION)
