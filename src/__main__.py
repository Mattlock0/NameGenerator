from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from .generation import Generator
from .generation import parse_template
from .config import Config
from .shading import DARKMODE
from .shading import LIGHTMODE
import logging as log
import sys

NAME_FONT_SIZE = 20
TEXT_FONT_SIZE = 15
DEFAULT_NUM_NAMES = 7

BUILD_CONFIG_PATH = 'settings.ini'
RUN_CONFIG_PATH = 'data/settings.ini'
CONFIG_PATH = BUILD_CONFIG_PATH
LOG_LEVEL = log.INFO
VERSION = '1.1'


class GeneratorUI(object):
    def __init__(self):
        self.gen = Generator()  # setup generator
        self.config = Config(CONFIG_PATH)
        self.config.read_config(self.gen)

        if self.config.read_config(self.gen):
            self.template_list = self.config.get_templates()
        else:
            self.template_list = ["Cvccvc", "Cvccv", "Cvcv", "Cvcvc", "Cvccvv", "Cvcvcv", "Cvcvv", "Cvcvccv", "Cvvcv",
                                  "Vccvc", "Cvcvvc", "Cvcc", "Cvccvcv", "Crvc", "Cvcy"]

    def setup_ui(self, main_window: QtWidgets.QMainWindow):
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

        self.template_sel = QtWidgets.QComboBox(self.centralwidget)
        self.template_sel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.template_sel.setFont(self.get_font(TEXT_FONT_SIZE))
        self.template_sel.setObjectName("template_sel")
        self.horizontalLayout.addWidget(self.template_sel)

        for template in self.template_list:
            self.template_sel.addItem(template)
        self.template_sel.addItem("Custom")

        self.template_sel.activated.connect(self.enable_enter)

        self.num_sel = QtWidgets.QSpinBox(self.centralwidget)
        self.num_sel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.num_sel.setMinimum(1)
        self.num_sel.setMaximum(20)
        self.num_sel.setValue(DEFAULT_NUM_NAMES)
        self.num_sel.setFont(self.get_font(TEXT_FONT_SIZE))
        self.num_sel.setObjectName("num_sel")
        self.horizontalLayout.addWidget(self.num_sel)

        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate_button.setFont(self.get_font(TEXT_FONT_SIZE))
        self.generate_button.clicked.connect(self.generate_names)
        self.generate_button.setObjectName("generate_button")
        self.horizontalLayout.addWidget(self.generate_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.template_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.template_enter.setFont(self.get_font(TEXT_FONT_SIZE))
        self.template_enter.setAlignment(QtCore.Qt.AlignCenter)
        self.template_enter.setObjectName("template_enter")
        self.verticalLayout.addWidget(self.template_enter)
        self.template_enter.hide()

        self.names_list = QtWidgets.QLabel(self.centralwidget)
        self.names_list.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.names_list.setAlignment(QtCore.Qt.AlignCenter)
        self.names_list.setObjectName("names_list")
        self.names_list.setFont(self.get_font(NAME_FONT_SIZE))
        self.verticalLayout.addWidget(self.names_list)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        main_window.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(main_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        main_window.setMenuBar(self.menuBar)

        self.action_settings = QtWidgets.QAction(main_window)
        self.action_settings.triggered.connect(self.settings)
        self.action_settings.setObjectName("action_settings")
        self.menuMenu.addAction(self.action_settings)

        self.action_shading_mode = QtWidgets.QAction(main_window)
        self.action_shading_mode.triggered.connect(lambda: self.set_shading(main_window))
        self.action_shading_mode.setObjectName("action_shading_mode")
        self.menuMenu.addAction(self.action_shading_mode)

        self.action_about = QtWidgets.QAction(main_window)
        self.action_about.triggered.connect(self.about_page)
        self.action_about.setObjectName("action_about")
        self.menuMenu.addAction(self.action_about)

        self.menuBar.addAction(self.menuMenu.menuAction())

        self.set_shading(main_window)
        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.setTabOrder(self.generate_button, self.template_sel)
        main_window.setTabOrder(self.template_sel, self.num_sel)
        main_window.setTabOrder(self.num_sel, self.template_enter)

    def retranslateUi(self, main_window):
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

    def get_font(self, pt_size):
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(pt_size)
        font.setWeight(75)

        return font

    def enable_enter(self):
        choice = self.template_sel.currentText()

        if choice == "Custom":
            self.template_enter.show()
            log.debug("Template bar enabled")
        else:
            self.template_enter.hide()

    def generate_names(self):
        template = self.template_sel.currentText()
        if template == "Custom":
            template = self.template_enter.text()
        generated_names = []

        log.info(f"Generating {self.num_sel.value()} names")
        for _ in range(self.num_sel.value()):
            generated_names.append(parse_template(self.gen, template))  # sends in chosen template

        new_name_list = ""
        for name in generated_names:
            new_name_list += "\n" + name

        self.names_list.setText(new_name_list)

    def settings(self):
        if not self.config.read_config_file:
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Settings file not found!")
            msg.setIcon(QMessageBox.Critical)
            return msg.exec_()

        log.info("Settings chosen...")

    def set_shading(self, window: QtWidgets.QMainWindow):
        if self.action_shading_mode.text() == "Light Mode":
            mode = LIGHTMODE
            self.action_shading_mode.setText("Dark Mode")
        else:
            mode = DARKMODE
            self.action_shading_mode.setText("Light Mode")

        window.setStyleSheet(f"background-color:{mode.background}; color:{mode.text}")

        inset_border = (
            f"border-bottom: 1px solid {mode.light_border}; border-right: 1px solid {mode.light_border}; "
            f"border-left: 2px solid {mode.border}; border-top: 2px solid {mode.border}\n")
        hover_boarder = (
            f"border-top: 1px solid {mode.light_border}; border-left: 1px solid {mode.light_border}; border"
            f"-right: 2px solid {mode.border}; border-bottom: 2px solid {mode.border}\n")
        outset_boarder = (
            f"border-top: 1px solid {mode.light_border}; border-left: 1px solid {mode.light_border}; border"
            f"-right: 3px solid {mode.border}; border-bottom: 3px solid {mode.border}\n")

        self.centralwidget.setStyleSheet("QPushButton {\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 5px;\n"
                                         f"{outset_boarder}"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         f"background-color: {mode.hover};\n"
                                         "border-style: outset;\n"
                                         "border-radius: 5px;\n"
                                         f"{hover_boarder}"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "border-style: inset;\n"
                                         "border-radius: 5px;\n"
                                         f"{inset_border}"
                                         "}\n"
                                         "QSpinBox {\n"
                                         "border-style: outset;\n"
                                         f"{inset_border}"
                                         "}\n"
                                         "QLineEdit {\n"
                                         f"background-color: {mode.edit};\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 5px;\n"
                                         f"{inset_border}"
                                         "}")
        self.menuBar.setStyleSheet(f"QMenuBar:item:hover {{ background-color: {mode.hover} }}\n"
                                   f"QMenuBar:item:selected {{ background-color: {mode.hover} }}")
        self.menuMenu.setStyleSheet(f"QMenu:item {{ background-color: {mode.background} }}\n"
                                    f"QMenu:item:selected {{ background-color: {mode.hover} }}")

    def about_page(self):
        about = QMessageBox()
        about.setWindowTitle("About")
        about.setText(f"Name Generator Version: {VERSION}")
        about.setInformativeText("Creator: Matthew Marchetti")
        about.setIcon(QMessageBox.Information)
        about.setStandardButtons(QMessageBox.Ok)

        mode = DARKMODE if self.action_shading_mode.text() == "Light Mode" else LIGHTMODE

        about.setStyleSheet(f"background-color: {mode.background}; color: {mode.text}")

        x = about.exec_()


def main():
    log.basicConfig(format="[%(levelname)s] %(message)s", level=LOG_LEVEL)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GeneratorUI()
    ui.setup_ui(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
