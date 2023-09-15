from src.__main__ import main
from pathlib import Path
import logging as log

#  NAME INFORMATION  #
#  most common english letters:  e, t, a, i, o, n, s, h, r
#  most common starting letters: t, a, o, d, w
#  most common ending letters:   e, s, d, t

# PROJECT CONSTANTS
BUILD_CONFIG_PATH = 'settings.ini'
RUN_CONFIG_PATH = 'data/settings.ini'
CONFIG_PATH = Path(RUN_CONFIG_PATH)
LOG_LEVEL = log.DEBUG
VERSION = 'v1.1'

if __name__ == '__main__':
    # set up logging
    log.basicConfig(format="[%(levelname)s] %(message)s", level=LOG_LEVEL)
    log.info("Starting Mattlock's Names Generator!")

    # run main application
    main(CONFIG_PATH, VERSION)
