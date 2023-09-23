# system imports
import logging as log

# qt imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# project imports
from src.settings import Settings
from src.utils import style_button
from src.utils import get_border
from src.utils import get_font
from src.utils import Border
from src.utils import Mode


class SettingsDialog(QtWidgets.QDialog):
    def __init__(self, settings: Settings, font_size: int):
        super().__init__()
        self.settings = settings
        self.font_size = font_size

    def setup_ui(self, shading: Mode):
        log.trace(f"Entered: SettingsDialog.{self.setup_ui.__name__}")
        self.resize(500, 500)
        self.setModal(True)
        self.mode = shading

        # grid layout and top spacer
        self.gridLayout = QtWidgets.QGridLayout(self)
        spacerItem = QtWidgets.QSpacerItem(20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)

        # setup main layout
        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_main.setObjectName("layout_main")

        # shading mode
        self.layout_shading = QtWidgets.QHBoxLayout()
        self.layout_shading.setObjectName("layout_shading")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_shading.addItem(spacerItem4)
        self.checkbox_lightmode = QtWidgets.QCheckBox(self)
        self.checkbox_lightmode.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_lightmode.setFont(get_font(self.font_size))
        self.checkbox_lightmode.setObjectName("checkbox_lightmode")
        self.layout_shading.addWidget(self.checkbox_lightmode)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_shading.addItem(spacerItem5)
        self.layout_main.addLayout(self.layout_shading)

        # font size
        self.layout_fontsize = QtWidgets.QHBoxLayout()
        self.layout_fontsize.setObjectName("layout_fontsize")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_fontsize.addItem(spacerItem2)
        self.label_fontsize = QtWidgets.QLabel(self)
        self.label_fontsize.setFont(get_font(self.font_size))
        self.label_fontsize.setObjectName("label_fontsize")
        self.layout_fontsize.addWidget(self.label_fontsize)
        self.enter_fontsize = QtWidgets.QLineEdit(self)
        self.enter_fontsize.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_fontsize.setFont(get_font(self.font_size))
        self.enter_fontsize.setObjectName("enter_fontsize")
        self.layout_fontsize.addWidget(self.enter_fontsize)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_fontsize.addItem(spacerItem3)
        self.layout_main.addLayout(self.layout_fontsize)

        # templates
        self.layout_templates = QtWidgets.QHBoxLayout()
        self.layout_templates.setObjectName("layout_templates")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_templates.addItem(spacerItem7)
        self.label_templates = QtWidgets.QLabel(self)
        self.label_templates.setFont(get_font(self.font_size))
        self.label_templates.setObjectName("label_templates")
        self.layout_templates.addWidget(self.label_templates)
        self.enter_templates = QtWidgets.QLineEdit(self)
        # self.enter_templates.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_templates.setFont(get_font(self.font_size))
        self.enter_templates.setObjectName("enter_templates")
        self.layout_templates.addWidget(self.enter_templates)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_templates.addItem(spacerItem8)
        self.layout_main.addLayout(self.layout_templates)

        # archive names
        self.layout_archive = QtWidgets.QHBoxLayout()
        self.layout_archive.setObjectName("layout_archive")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_archive.addItem(spacerItem9)
        self.checkbox_archive = QtWidgets.QCheckBox(self)
        self.checkbox_archive.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_archive.setFont(get_font(self.font_size))
        self.checkbox_archive.setObjectName("checkbox_archive")
        self.layout_archive.addWidget(self.checkbox_archive)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_archive.addItem(spacerItem10)
        self.layout_main.addLayout(self.layout_archive)

        # bottom spacer
        self.gridLayout.addLayout(self.layout_main, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 1)

        # save and cancel buttons
        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.layout_buttons.setObjectName("layout_buttons")
        self.button_save = QtWidgets.QPushButton(self)
        self.button_save.setMinimumSize(QtCore.QSize(0, 35))
        self.button_save.setFont(get_font(self.font_size))
        self.button_save.setObjectName("button_save")
        self.button_save.clicked.connect(self.pressed_save)
        self.layout_buttons.addWidget(self.button_save)
        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setMinimumSize(QtCore.QSize(0, 35))
        self.button_cancel.setFont(get_font(self.font_size))
        self.button_cancel.setObjectName("button_cancel")
        self.button_cancel.clicked.connect(self.pressed_cancel)
        self.layout_buttons.addWidget(self.button_cancel)
        self.gridLayout.addLayout(self.layout_buttons, 3, 0, 1, 1)

        self.set_shading()
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        log.trace(f"Entered: SettingsDialog.{self.retranslate_ui.__name__}")
        _translate = QtCore.QCoreApplication.translate
        window_title = "SettingsDialog"
        self.setWindowTitle(_translate(window_title, "Settings"))
        self.checkbox_lightmode.setText(_translate(window_title, "Light Mode"))
        self.label_fontsize.setText(_translate(window_title, "Font Size"))
        self.label_templates.setText(_translate(window_title, "Templates"))
        self.enter_templates.setText(_translate(window_title, self.settings.get('nameGeneration', 'templates')))
        self.checkbox_archive.setText(_translate(window_title, "Archive Names"))
        self.button_save.setText(_translate(window_title, "Save"))
        self.button_cancel.setText(_translate(window_title, "Cancel"))
        self.initialize_settings()

    def set_shading(self):
        log.trace(f"Entered: SettingsDialog.{self.set_shading.__name__}")
        inset_border = get_border(Border.INSET, self.mode)

        self.setStyleSheet("QDialog {\n"
                           f"background-color:{self.mode.background}"
                           "}\n"
                           f"{style_button(self.mode)}"
                           "QCheckBox {"
                           f"color: {self.mode.text}\n"
                           "}\n"
                           "QLabel {\n"
                           f"color: {self.mode.text};\n"
                           "}\n"
                           "QLineEdit {\n"
                           f"background-color: {self.mode.edit};\n"
                           f"color: {self.mode.text};\n"
                           "border-style: outset;\n"
                           f"{inset_border}"
                           "}")

    def initialize_settings(self):
        if self.settings.get('general', 'shadingmode') == 'light':
            self.checkbox_lightmode.setChecked(True)
        self.enter_fontsize.setText(self.settings.get('general', 'fontsize'))

    def pressed_save(self):
        log.trace(f"Entered: SettingsDialog.{self.pressed_save.__name__}")

        # save settings to a file
        if self.settings.path.is_file():
            log.info("Saving settings to file...")
            self.settings.save()
        else:
            log.warning("Tried to save to file that did not exist!")
            self.no_config_file()

        self.done(0)

    def pressed_cancel(self):
        log.trace(f"Entered: SettingsDialog.{self.pressed_cancel.__name__}")
        self.done(1)

    def no_config_file(self):
        log.trace(f"Entered: MainWindow.{self.no_config_file.__name__}")
        # show a message to the user about the missing settings file
        config_generation = QMessageBox()
        config_generation.setWindowTitle("No File Found!")
        config_generation.setText(f"No settings.ini found! Would you like to generate one?")
        config_generation.setInformativeText("(In the same directory as the executable)")
        config_generation.setFont(get_font(self.font_size))
        config_generation.setIcon(QMessageBox.Warning)
        config_generation.setStandardButtons(QMessageBox.Ok | QMessageBox.No)

        config_generation.setStyleSheet(f"background-color: {self.mode.background}; color: {self.mode.text}")

        ret = config_generation.exec_()

        # if they choose to generate, generate
        # if not, just return and be sad :(
        match ret:
            case QMessageBox.Ok:
                log.info("Generating settings file...")
                self.settings.save()
            case QMessageBox.No:
                log.info("User did not want settings file :(")
