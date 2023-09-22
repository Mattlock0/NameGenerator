# system imports
from pathlib import Path
import logging as log

# qt imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# project imports
from src.settings_dialog import SettingsDialog
from src.utils import DARKMODE, LIGHTMODE
from src.generator_v2 import Generator
from src.utils import style_button
from src.utils import get_border
from src.utils import get_font
from src.utils import Border

# defaults
MAX_NAME_GEN = 40
NAME_FONT_SIZE = 20
TEXT_FONT_SIZE = NAME_FONT_SIZE - 5
MENU_FONT_SIZE = TEXT_FONT_SIZE - 3
DEFAULT_NUM_NAMES = 7


class MainWindow(object):
    def __init__(self, config_path: Path, version: str):
        # initialize generator
        self.gen = Generator(config_path)

        # initialize shading mode
        self.mode = DARKMODE

        # extra class elements
        self.settings_window = QtWidgets.QMainWindow()
        self.version = version

    def setup_ui(self, main_window: QtWidgets.QMainWindow):
        log.trace(f"Entered: MainWindow.{self.setup_ui.__name__}")
        log.debug("Setting up UI...")
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 4)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 25, 5, 25)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.template_select = QtWidgets.QComboBox(self.centralwidget)
        self.template_select.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.template_select.setFont(get_font(TEXT_FONT_SIZE))
        self.template_select.setObjectName("template_select")
        self.horizontalLayout.addWidget(self.template_select)

        for template in self.gen.templates:
            self.template_select.addItem(template)
        self.template_select.addItem("Custom")

        self.template_select.activated.connect(self.enable_enter)

        self.num_sel = QtWidgets.QSpinBox(self.centralwidget)
        self.num_sel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_sel.setMinimum(1)
        self.num_sel.setMaximum(MAX_NAME_GEN)
        self.num_sel.setValue(DEFAULT_NUM_NAMES)
        self.num_sel.setFont(get_font(TEXT_FONT_SIZE))
        self.num_sel.setObjectName("num_sel")
        self.horizontalLayout.addWidget(self.num_sel)

        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate_button.setFont(get_font(TEXT_FONT_SIZE))
        self.generate_button.clicked.connect(self.generate_names)
        self.generate_button.setObjectName("generate_button")
        self.horizontalLayout.addWidget(self.generate_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.template_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.template_enter.setFont(get_font(TEXT_FONT_SIZE))
        self.template_enter.setAlignment(QtCore.Qt.AlignCenter)
        self.template_enter.setObjectName("template_enter")
        self.verticalLayout.addWidget(self.template_enter)
        self.template_enter.hide()

        self.names_list = QtWidgets.QLabel(self.centralwidget)
        self.names_list.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.names_list.setAlignment(QtCore.Qt.AlignCenter)
        self.names_list.setObjectName("names_list")
        self.names_list.setFont(get_font(NAME_FONT_SIZE))
        self.verticalLayout.addWidget(self.names_list)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(main_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setFont(get_font(MENU_FONT_SIZE))
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMenu.setFont(get_font(MENU_FONT_SIZE))
        main_window.setMenuBar(self.menuBar)

        self.action_settings = QtWidgets.QAction(main_window)
        self.action_settings.triggered.connect(self.settings)
        self.action_settings.setObjectName("action_settings")
        self.menuMenu.addAction(self.action_settings)

        self.action_shading_mode = QtWidgets.QAction(main_window)
        self.action_shading_mode.triggered.connect(lambda: self.set_shading(main_window, True))
        self.action_shading_mode.setObjectName("action_shading_mode")
        self.menuMenu.addAction(self.action_shading_mode)

        self.action_about = QtWidgets.QAction(main_window)
        self.action_about.triggered.connect(self.about_page)
        self.action_about.setObjectName("action_about")
        self.menuMenu.addAction(self.action_about)

        self.menuBar.addAction(self.menuMenu.menuAction())

        self.set_shading(main_window)
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.setTabOrder(self.generate_button, self.template_select)
        main_window.setTabOrder(self.template_select, self.num_sel)
        main_window.setTabOrder(self.num_sel, self.template_enter)

    def retranslate_ui(self, main_window):
        log.trace(f"Entered: MainWindow.{self.retranslate_ui.__name__}")
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "main_window"))
        self.generate_button.setText(_translate("main_window", "Generate Names"))
        self.generate_button.setShortcut(_translate("main_window", "G"))
        self.template_enter.setPlaceholderText(_translate("main_window", "Enter template... (* is wildcard)"))
        self.names_list.setText(_translate("main_window", ""))
        self.menuMenu.setTitle(_translate("main_window", "Menu"))
        self.action_settings.setText(_translate("main_window", "Settings"))
        self.action_settings.setShortcut(_translate("main_window", "Ctrl+S"))
        self.action_shading_mode.setText(_translate("main_window", "Light Mode"))
        self.action_shading_mode.setShortcut(_translate("main_window", "Ctrl+Shift+L"))
        self.action_about.setText(_translate("main_window", "About"))

    def reverse_shading(self):
        log.trace(f"Entered: MainWindow.{self.reverse_shading.__name__}")
        if self.mode.type == 'darkmode':
            self.mode = LIGHTMODE
            return 'Dark Mode'
        else:
            self.mode = DARKMODE
            return 'Light Mode'

    def set_shading(self, window: QtWidgets.QMainWindow, switch: bool = False):
        log.trace(f"Entered: MainWindow.{self.set_shading.__name__}")

        #
        if switch:
            self.action_shading_mode.setText(self.reverse_shading())

        window.setStyleSheet(f"background-color:{self.mode.background}; color:{self.mode.text}")

        inset_border = get_border(Border.INSET, self.mode)

        self.centralwidget.setStyleSheet(f"{style_button(self.mode)}"
                                         "QSpinBox {\n"
                                         "border-style: outset;\n"
                                         f"{inset_border}"
                                         "}\n"
                                         "QLineEdit {\n"
                                         f"background-color: {self.mode.edit};\n"
                                         "border-style: outset;\n"
                                         f"{inset_border}"
                                         "}")
        self.menuBar.setStyleSheet(f"QMenuBar:item:hover {{ background-color: {self.mode.hover} }}\n"
                                   f"QMenuBar:item:selected {{ background-color: {self.mode.hover} }}")
        self.menuMenu.setStyleSheet(f"QMenu:item {{ background-color: {self.mode.background} }}\n"
                                    f"QMenu:item:selected {{ background-color: {self.mode.hover} }}")

    def enable_enter(self):
        log.trace(f"Entered: MainWindow.{self.enable_enter.__name__}")
        choice = self.template_select.currentText()

        if choice == "Custom":
            self.template_enter.show()
            log.debug("Template bar enabled")
        else:
            self.template_enter.hide()

    def generate_names(self):
        log.trace(f"Entered: MainWindow.{self.generate_names.__name__}")
        template = self.template_select.currentText()
        if template == "Custom":
            template = self.template_enter.text()
        generated_names = []

        log.debug(f"Generating... Rare: {self.gen.rare_chance}% | Diagraph: {self.gen.diagraph_chance}% | "
                  f"Double: {self.gen.double_chance}% | Qu: {self.gen.qu_chance}%")
        for _ in range(self.num_sel.value()):
            generated_names.append(self.gen.generate_name(template))  # sends in chosen template

        new_name_list = ""
        for name in generated_names:
            new_name_list += "\n" + name

        self.names_list.setText(new_name_list)

    def settings(self):
        log.trace(f"Entered: MainWindow.{self.settings.__name__}")

        settings_dialog = SettingsDialog(self.gen, MENU_FONT_SIZE)
        settings_dialog.setup_ui(self.mode)
        settings_dialog.exec_()

    def about_page(self):
        log.trace(f"Entered: MainWindow.{self.about_page.__name__}")
        about = QMessageBox()
        about.setWindowTitle("About")
        about.setText(f"Name Generator Version: {self.version}")
        about.setInformativeText("Creator: Matthew Marchetti")
        about.setFont(get_font(MENU_FONT_SIZE))
        about.setIcon(QMessageBox.Information)
        about.setStandardButtons(QMessageBox.Ok)

        about.setStyleSheet(f"background-color: {self.mode.background}; color: {self.mode.text}\n")

        x = about.exec_()
