from PyQt5 import QtCore, QtGui, QtWidgets
from .generation import Generator
from .generation import parse_template
from .config import Config
import logging as log
import sys

NAME_FONT_SIZE = 20
TEXT_FONT_SIZE = 15
DEFAULT_NUM_NAMES = 7

BUILD_CONFIG_PATH = '../data/settings.ini'
RUN_CONFIG_PATH = 'data/settings.ini'
CONFIG_PATH = RUN_CONFIG_PATH


class GeneratorUI(object):
    def setup_ui(self, MainWindow, gen: Generator, templates: list):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:#2b2e33; color:#ebebeb")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.template_sel = QtWidgets.QComboBox(self.centralwidget)
        self.template_sel.setObjectName("template_sel")
        self.template_sel.setFont(self.get_font(TEXT_FONT_SIZE))
        self.horizontalLayout.addWidget(self.template_sel)

        for template in templates:
            self.template_sel.addItem(template)
        self.template_sel.addItem("Custom")

        self.template_sel.activated.connect(self.enable_enter)

        self.num_sel = QtWidgets.QSpinBox(self.centralwidget)
        self.num_sel.setMinimum(1)
        self.num_sel.setMaximum(20)
        self.num_sel.setValue(DEFAULT_NUM_NAMES)
        self.num_sel.setObjectName("num_sel")
        self.num_sel.setFont(self.get_font(TEXT_FONT_SIZE))
        self.horizontalLayout.addWidget(self.num_sel)

        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setObjectName("generate_button")
        self.generate_button.setFont(self.get_font(TEXT_FONT_SIZE))
        self.horizontalLayout.addWidget(self.generate_button)
        self.generate_button.clicked.connect(lambda: self.generate_names(gen))

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.template_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.template_enter.setObjectName("template_enter")
        self.template_enter.setFont(self.get_font(TEXT_FONT_SIZE))
        self.verticalLayout.addWidget(self.template_enter)
        self.template_enter.hide()

        self.names_list = QtWidgets.QLabel(self.centralwidget)
        self.names_list.setAlignment(QtCore.Qt.AlignCenter)
        self.names_list.setObjectName("names_list")
        self.names_list.setFont(self.get_font(NAME_FONT_SIZE))
        self.verticalLayout.addWidget(self.names_list)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.generate_button, self.template_sel)
        MainWindow.setTabOrder(self.template_sel, self.num_sel)
        MainWindow.setTabOrder(self.num_sel, self.template_enter)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generate_button.setText(_translate("MainWindow", "Generate Names"))
        self.template_enter.setPlaceholderText(_translate("MainWindow", "Enter template..."))
        self.names_list.setText(_translate("MainWindow", ""))

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
        else:
            self.template_enter.hide()

    def generate_names(self, gen):
        template = self.template_sel.currentText()
        if template == "Custom":
            template = self.template_enter.text()
        generated_names = []

        for _ in range(self.num_sel.value()):
            generated_names.append(parse_template(gen, template))  # sends in chosen template

        new_name_list = ""
        for name in generated_names:
            new_name_list += "\n" + name

        self.names_list.setText(new_name_list)


def main():
    gen = Generator()  # setup generator
    config = Config(CONFIG_PATH)  #
    config.read_config(gen)
    template_list = config.get_templates()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GeneratorUI()
    ui.setup_ui(MainWindow, gen, template_list)
    MainWindow.show()

    sys.exit(app.exec_())
