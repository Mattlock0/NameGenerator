# system imports
from pathlib import Path
import sys

# qt imports
from PyQt5 import QtWidgets

# project imports
from src.main_window import MainWindow


def main(config_path: Path, version: str):
    # set up main widget window
    app = QtWidgets.QApplication(sys.argv)
    main_widget = QtWidgets.QMainWindow()

    # create new MainWindow class
    ui = MainWindow(config_path, version)
    ui.setup_ui(main_widget)

    # show the built widget to the screen
    main_widget.show()

    # once the user clicks exit, close the window cleanly
    sys.exit(app.exec_())
