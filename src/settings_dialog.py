# qt imports
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# project imports
from src.settings import Settings
from src.utils import Mode, get_font, log, func_name, get_border, Border, style_button, LIGHTMODE, DARKMODE


class SettingsDialog(QtWidgets.QDialog):
    def __init__(self, settings: Settings, font_size: int):
        super().__init__()
        self.settings = settings
        self.font_size = font_size

    def setup_ui(self, shading: Mode):
        log.trace(f"Entered: SettingsDialog.{func_name()}")
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
        self.checkbox_lightmode.stateChanged.connect(self.update_shading)
        self.layout_shading.addWidget(self.checkbox_lightmode)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_shading.addItem(spacerItem5)
        self.layout_main.addLayout(self.layout_shading)

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

        # archive separator
        self.layout_separator = QtWidgets.QHBoxLayout()
        self.layout_separator.setObjectName("layout_separator")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_separator.addItem(spacerItem13)
        self.label_separator = QtWidgets.QLabel(self)
        self.label_separator.setFont(get_font(self.font_size))
        self.label_separator.setObjectName("label_separator")
        self.layout_separator.addWidget(self.label_separator)
        self.enter_separator = QtWidgets.QLineEdit(self)
        self.enter_separator.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_separator.setFont(get_font(self.font_size))
        self.enter_separator.setObjectName("enter_separator")
        self.layout_separator.addWidget(self.enter_separator)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_separator.addItem(spacerItem14)
        self.layout_main.addLayout(self.layout_separator)

        # font size
        self.layout_font_size = QtWidgets.QHBoxLayout()
        self.layout_font_size.setObjectName("layout_font_size")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_font_size.addItem(spacerItem2)
        self.label_font_size = QtWidgets.QLabel(self)
        self.label_font_size.setFont(get_font(self.font_size))
        self.label_font_size.setObjectName("label_font_size")
        self.layout_font_size.addWidget(self.label_font_size)
        self.enter_font_size = QtWidgets.QLineEdit(self)
        self.enter_font_size.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_font_size.setFont(get_font(self.font_size))
        self.enter_font_size.setObjectName("enter_font_size")
        self.layout_font_size.addWidget(self.enter_font_size)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_font_size.addItem(spacerItem3)
        self.layout_main.addLayout(self.layout_font_size)

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
        self.enter_templates.setMinimumWidth(130)
        self.enter_templates.setFont(get_font(self.font_size))
        self.enter_templates.setObjectName("enter_templates")
        self.layout_templates.addWidget(self.enter_templates)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_templates.addItem(spacerItem8)
        self.layout_main.addLayout(self.layout_templates)

        # default button
        self.layout_default = QtWidgets.QHBoxLayout()
        self.layout_default.setObjectName("layout_default")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_default.addItem(spacerItem11)
        self.button_default = QtWidgets.QPushButton(self)
        self.button_default.setMaximumSize(QtCore.QSize(600, 16777215))
        self.button_default.setFont(get_font(self.font_size))
        self.button_default.setObjectName("button_default")
        self.layout_default.addWidget(self.button_default)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_default.addItem(spacerItem12)
        self.layout_main.addLayout(self.layout_default)

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
        self.button_save.setDefault(True)
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
        log.trace(f"Entered: SettingsDialog.{func_name()}")
        _translate = QtCore.QCoreApplication.translate
        window_title = "SettingsDialog"
        self.setWindowTitle(_translate(window_title, "Settings"))
        self.checkbox_lightmode.setText(_translate(window_title, "Light Mode"))
        self.checkbox_archive.setText(_translate(window_title, "Archive Names"))
        self.label_separator.setText(_translate(window_title, "Archive Name Separator"))
        self.label_font_size.setText(_translate(window_title, "Font Size"))
        self.label_templates.setText(_translate(window_title, "Templates"))
        self.button_default.setText(_translate(window_title, "Return to Default"))
        self.button_save.setText(_translate(window_title, "Save"))
        self.button_cancel.setText(_translate(window_title, "Cancel"))
        self.initialize_settings()

    def set_shading(self):
        log.trace(f"Entered: SettingsDialog.{func_name()}")
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

    def update_shading(self):
        self.mode = LIGHTMODE if self.checkbox_lightmode.isChecked() else DARKMODE
        self.set_shading()

    def initialize_settings(self):
        log.trace(f"Entered: SettingsDialog.{func_name()}")
        self.checkbox_lightmode.setChecked(self.settings.getboolean('lightmode'))
        self.checkbox_archive.setChecked(self.settings.getboolean('archive_names'))
        self.enter_separator.setText(self.settings.get('archive_separator'))
        self.enter_templates.setText(self.settings.get('templates'))
        self.enter_font_size.setText(self.settings.get('font_size'))

    def check(self, checkbox: QtWidgets.QCheckBox):
        log.trace(f"Entered: SettingsDialog.{func_name()}")
        return 'yes' if checkbox.isChecked() else 'no'

    def pressed_save(self):
        log.trace(f"Entered: SettingsDialog.{func_name()}")

        self.settings.set('templates', self.enter_templates.text())
        self.settings.set('archive_names', self.check(self.checkbox_archive))
        self.settings.set('archive_separator', self.enter_separator.text())
        self.settings.set('lightmode', self.check(self.checkbox_lightmode))
        self.settings.set('font_size', self.enter_font_size.text())

        # save settings to a file
        if self.settings.path.is_file():
            self.settings.save()
        else:
            log.warning("Tried to save to file that did not exist!")
            self.no_config_file()

        self.done(0)

    def pressed_cancel(self):
        log.trace(f"Entered: SettingsDialog.{func_name()}")
        self.done(1)

    def no_config_file(self):
        log.trace(f"Entered: MainWindow.{func_name()}")
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
