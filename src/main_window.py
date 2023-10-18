# system imports
from pathlib import Path

# qt imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# project imports
from src.settings_dialog import SettingsDialog
from src.tuning_dialog import TuningDialog
from src.generators.generator_v3 import Generator
from src.settings import Settings
from src.utils import *

# consts
MAX_NAME_GEN = 40
DEFAULT_NUM_NAMES = 7
ARCHIVE_PATH = "data/generated_names.txt"


class MainWindow(object):
    def __init__(self, config_path: Path, version: str):
        # initialize generator
        self.gen = Generator()

        # initialize settings
        self.settings = Settings(config_path)
        self.templates = []
        self.font_size = 0
        self.lightmode = False
        self.archive = False

        # extra class elements
        self.settings_window = QtWidgets.QMainWindow()
        self.version = version

    def setup_ui(self, main_window: QtWidgets.QMainWindow):
        log.trace(f"Entered: MainWindow.{func_name()}")
        log.debug("Setting up UI...")

        self.main_window = main_window
        self.main_window.setObjectName("main_window")
        self.main_window.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 4)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 25, 5, 25)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.combo_template = QtWidgets.QComboBox(self.centralwidget)
        self.combo_template.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.combo_template.setObjectName("template_select")
        self.horizontalLayout.addWidget(self.combo_template)

        self.combo_template.activated.connect(self.enable_enter)

        self.spin_num_gens = QtWidgets.QSpinBox(self.centralwidget)
        self.spin_num_gens.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spin_num_gens.setMinimum(1)
        self.spin_num_gens.setMaximum(MAX_NAME_GEN)
        self.spin_num_gens.setValue(DEFAULT_NUM_NAMES)
        self.spin_num_gens.setObjectName("num_sel")
        self.horizontalLayout.addWidget(self.spin_num_gens)

        self.button_generate = QtWidgets.QPushButton(self.centralwidget)
        self.button_generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_generate.clicked.connect(self.generate_names)
        self.button_generate.setObjectName("generate_button")
        self.button_generate.setDefault(True)
        self.horizontalLayout.addWidget(self.button_generate)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.enter_template = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_template.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_template.setObjectName("template_enter")
        self.verticalLayout.addWidget(self.enter_template)
        self.enter_template.hide()

        self.label_names = QtWidgets.QLabel(self.centralwidget)
        self.label_names.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_names.setAlignment(QtCore.Qt.AlignCenter)
        self.label_names.setObjectName("names_list")
        self.verticalLayout.addWidget(self.label_names)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.main_window.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(self.main_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.main_window.setMenuBar(self.menuBar)

        self.action_settings = QtWidgets.QAction(self.main_window)
        self.action_settings.triggered.connect(self.open_settings)
        self.action_settings.setObjectName("action_settings")
        self.menuMenu.addAction(self.action_settings)

        self.action_tuning = QtWidgets.QAction(self.main_window)
        self.action_tuning.triggered.connect(self.open_tuning)
        self.action_tuning.setObjectName("action_tuning")
        self.menuMenu.addAction(self.action_tuning)

        self.action_about = QtWidgets.QAction(self.main_window)
        self.action_about.triggered.connect(self.open_about)
        self.action_about.setObjectName("action_about")
        self.menuMenu.addAction(self.action_about)

        self.menuBar.addAction(self.menuMenu.menuAction())

        self.set_shading()
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)
        self.main_window.setTabOrder(self.button_generate, self.combo_template)
        self.main_window.setTabOrder(self.combo_template, self.spin_num_gens)
        self.main_window.setTabOrder(self.spin_num_gens, self.enter_template)

    def retranslate_ui(self):
        log.trace(f"Entered: MainWindow.{func_name()}")
        _translate = QtCore.QCoreApplication.translate
        self.main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_generate.setText(_translate("MainWindow", "Generate Names"))
        self.button_generate.setShortcut(_translate("MainWindow", "G"))
        self.enter_template.setPlaceholderText(_translate("MainWindow", "Enter template... (* is wildcard)"))
        self.label_names.setText(_translate("MainWindow", ""))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.action_settings.setText(_translate("MainWindow", "Settings"))
        self.action_settings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_tuning.setText(_translate("MainWindow", "Tuning"))
        self.action_tuning.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.read_settings()

    def set_shading(self, switch: bool = False):
        log.trace(f"Entered: MainWindow.{func_name()}")
        shading = LIGHTMODE if self.lightmode else DARKMODE

        self.main_window.setStyleSheet(f"background-color:{shading.background}; color:{shading.text}")

        inset_border = get_border(Border.INSET, shading)

        self.centralwidget.setStyleSheet(f"{style_button(shading)}"
                                         "QSpinBox {\n"
                                         "border-style: outset;\n"
                                         f"{inset_border}"
                                         "}\n"
                                         "QLineEdit {\n"
                                         f"background-color: {shading.edit};\n"
                                         "border-style: outset;\n"
                                         f"{inset_border}"
                                         "}")
        self.menuBar.setStyleSheet(f"QMenuBar:item:hover {{ background-color: {shading.hover} }}\n"
                                   f"QMenuBar:item:selected {{ background-color: {shading.hover} }}")
        self.menuMenu.setStyleSheet(f"QMenu:item {{ background-color: {shading.background} }}\n"
                                    f"QMenu:item:selected {{ background-color: {shading.hover} }}")

    def update_fonts(self):
        self.combo_template.setFont(get_font(self.font_size))
        self.spin_num_gens.setFont(get_font(self.font_size))
        self.button_generate.setFont(get_font(self.font_size))
        self.enter_template.setFont(get_font(self.font_size))
        self.label_names.setFont(get_font(self.font_size + 5))
        self.menuBar.setFont(get_font(self.font_size - 3))
        self.menuMenu.setFont(get_font(self.font_size - 3))

    def read_settings(self):
        log.trace(f"Entered: MainWindow.{func_name()}")

        # shading mode
        self.lightmode = self.settings.getboolean('lightmode')
        self.set_shading()

        # templates
        self.templates = self.settings.getlist('templates')
        self.combo_template.clear()
        for template in self.templates:
            self.combo_template.addItem(template)
        self.combo_template.addItem("Custom")

        # font size
        self.font_size = self.settings.getint('font_size')
        self.update_fonts()

        # archive
        self.archive = self.settings.getboolean('archive_names')

    def enable_enter(self):
        log.trace(f"Entered: MainWindow.{func_name()}")
        choice = self.combo_template.currentText()

        if choice == "Custom":
            self.enter_template.show()
            log.debug("Template bar enabled")
        else:
            self.enter_template.hide()

    def generate_names(self):
        log.trace(f"Entered: MainWindow.{func_name()}")
        template = self.combo_template.currentText()
        if template == "Custom":
            template = self.enter_template.text()
        generated_names = []

        log.debug(f"Generating... Rare: {self.gen.rare_chance}% | Diagraph: {self.gen.diagraph_chance}% | "
                  f"Double: {self.gen.double_chance}% | Common: {self.gen.common_chance}%")
        for _ in range(self.spin_num_gens.value()):
            generated_names.append(self.gen.generate_name(template))  # sends in chosen template

        generated_names.sort()
        new_name_list = "\n".join(generated_names)
        self.label_names.setText(new_name_list)
        self.archive_names(generated_names)

    def archive_names(self, name_list: list):
        if self.settings.getboolean('archive_names'):
            archive_list = f" {self.settings.get('archive_separator')} ".join(name_list)
            log.info(f"Archiving names to {ARCHIVE_PATH}")

            with open(ARCHIVE_PATH, "a") as archivefile:
                archivefile.write(archive_list + "\n")

    def open_settings(self):
        log.trace(f"Entered: MainWindow.{func_name()}")
        settings_dialog = SettingsDialog(self.settings, self.font_size - 2)
        settings_dialog.setup_ui(LIGHTMODE if self.lightmode else DARKMODE)
        settings_dialog.exec_()

        self.read_settings()

    def open_tuning(self):
        log.trace(f"Entered: MainWindow.{func_name()}")
        tuning_dialog = TuningDialog(self.gen, self.font_size - 4)
        tuning_dialog.setup_ui(LIGHTMODE if self.lightmode else DARKMODE)
        tuning_dialog.exec_()

    def open_about(self):
        log.trace(f"Entered: MainWindow.{func_name()}")

        shading = LIGHTMODE if self.lightmode else DARKMODE

        about = QMessageBox()
        about.setWindowTitle("About")
        about.setText(f"Name Generator Version: {self.version}")
        about.setInformativeText("Creator: Matthew Marchetti")
        about.setFont(get_font(self.font_size - 3))
        about.setIcon(QMessageBox.Information)
        about.setStandardButtons(QMessageBox.Ok)

        about.setStyleSheet(f"background-color: {shading.background}; color: {shading.text}\n")

        x = about.exec_()
