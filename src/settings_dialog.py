# system imports
import logging as log

# qt imports
from PyQt5 import QtCore, QtWidgets

# project imports
from src.generator_v2 import Generator
from src.shading import Mode


class SettingsDialog(QtWidgets.QDialog):
    def __init__(self, gen: Generator):
        super().__init__()
        self.gen = gen

    def setup_ui(self, shading: Mode):
        log.trace(f"Entered: SettingsDialog.{self.setup_ui.__name__}")
        self.resize(500, 500)
        self.setModal(True)

        self.gridLayout = QtWidgets.QGridLayout(self)

        vertical_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addItem(vertical_spacer)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        horizontal_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addItem(horizontal_spacer)

        self.label_rare = QtWidgets.QLabel(self)
        self.label_rare.setObjectName("label")
        self.horizontalLayout.addWidget(self.label_rare)

        self.enter_rare = QtWidgets.QLineEdit(self)
        self.enter_rare.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_rare.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enter_rare)

        horizontal_spacer_2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(horizontal_spacer_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        horizontal_spacer_3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addItem(horizontal_spacer_3)

        self.label_double = QtWidgets.QLabel(self)
        self.label_double.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_double)

        self.enter_double = QtWidgets.QLineEdit(self)
        self.enter_double.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_double.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.enter_double)

        horizontal_spacer_4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(horizontal_spacer_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        horizontal_spacer_5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.addItem(horizontal_spacer_5)

        self.label_qu = QtWidgets.QLabel(self)
        self.label_qu.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_qu)

        self.enter_qu = QtWidgets.QLineEdit(self)
        self.enter_qu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_qu.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.enter_qu)

        horizontal_spacer_6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(horizontal_spacer_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        horizontal_spacer_7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.addItem(horizontal_spacer_7)

        self.label_diagraph = QtWidgets.QLabel(self)
        self.label_diagraph.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_diagraph)

        self.enter_diagraph = QtWidgets.QLineEdit(self)
        self.enter_diagraph.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_diagraph.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.enter_diagraph)

        horizontal_spacer_8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(horizontal_spacer_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        horizontal_spacer_9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.addItem(horizontal_spacer_9)

        self.checkbox_popular = QtWidgets.QCheckBox(self)
        self.checkbox_popular.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_popular.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkbox_popular)

        horizontal_spacer_10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(horizontal_spacer_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        vertical_spacer_2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addItem(vertical_spacer_2)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.button_save = QtWidgets.QPushButton(self)
        self.button_save.setMinimumSize(QtCore.QSize(0, 35))
        self.button_save.clicked.connect(self.pressed_save)
        self.button_save.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.button_save)

        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setMinimumSize(QtCore.QSize(0, 35))
        self.button_cancel.clicked.connect(self.pressed_cancel)
        self.button_cancel.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.button_cancel)

        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.set_shading(shading)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        log.trace(f"Entered: SettingsDialog.{self.retranslate_ui.__name__}")
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.label_rare.setText(_translate("SettingsDialog", "Rare Consonant Chance (%)"))
        self.enter_rare.setText(_translate("SettingsDialog", str(self.gen.rare_chance)))
        self.label_double.setText(_translate("SettingsDialog", "Double Letter Chance (%)"))
        self.enter_double.setText(_translate("SettingsDialog", str(self.gen.double_chance)))
        self.label_qu.setText(_translate("SettingsDialog", "Qu Chance (%)"))
        self.enter_qu.setText(_translate("SettingsDialog", str(self.gen.qu_chance)))
        self.label_diagraph.setText(_translate("SettingsDialog", "Diagraph Chance (%)"))
        self.enter_diagraph.setText(_translate("SettingsDialog", str(self.gen.diagraph_chance)))
        self.checkbox_popular.setText(_translate("SettingsDialog", "Show only popular templates?"))
        self.button_save.setText(_translate("SettingsDialog", "Save"))
        self.button_cancel.setText(_translate("SettingsDialog", "Cancel"))

    def set_shading(self, shading):
        log.trace(f"Entered: SettingsDialog.{self.set_shading.__name__}")
        inset_border = (
            f"border-bottom: 1px solid {shading.light_border}; border-right: 1px solid {shading.light_border}; "
            f"border-left: 2px solid {shading.border}; border-top: 2px solid {shading.border}\n")
        hover_boarder = (
            f"border-top: 1px solid {shading.light_border}; border-left: 1px solid {shading.light_border}; border"
            f"-right: 2px solid {shading.border}; border-bottom: 2px solid {shading.border}\n")
        outset_boarder = (
            f"border-top: 1px solid {shading.light_border}; border-left: 1px solid {shading.light_border}; border"
            f"-right: 3px solid {shading.border}; border-bottom: 3px solid {shading.border}\n")

        self.setStyleSheet("QDialog {\n"
                           f"background-color:{shading.background}"
                           "}\n"
                           "QPushButton {\n"
                           f"color: {shading.text};\n"
                           "border-style: outset;\n"
                           "border-width: 1px;\n"
                           "border-radius: 5px;\n"
                           f"{outset_boarder}"
                           "}\n"
                           "QPushButton:hover {\n"
                           f"background-color: {shading.hover};\n"
                           f"color: {shading.text};\n"
                           "border-style: outset;\n"
                           "border-radius: 5px;\n"
                           f"{hover_boarder}"
                           "}\n"
                           "QPushButton:pressed {\n"
                           f"color: {shading.text};\n"
                           "border-style: inset;\n"
                           "border-radius: 5px;\n"
                           f"{inset_border}"
                           "}\n"
                           "QCheckBox {"
                           f"color: {shading.text}\n"
                           "}\n"
                           "QLabel {\n"
                           f"color: {shading.text};\n"
                           "}\n"
                           "QLineEdit {\n"
                           f"background-color: {shading.edit};\n"
                           f"color: {shading.text};\n"
                           "border-style: outset;\n"
                           "border-width: 1px;\n"
                           "border-radius: 5px;\n"
                           f"{inset_border}"
                           "}")

    def pressed_save(self):
        log.trace(f"Entered: SettingsDialog.{self.pressed_save.__name__}")
        rare_chance = int(self.enter_rare.text())
        double_chance = int(self.enter_double.text())
        qu_chance = int(self.enter_qu.text())
        diagraph_chance = int(self.enter_diagraph.text())

        self.gen.rare_chance = rare_chance
        self.gen.double_chance = double_chance
        self.gen.qu_chance = qu_chance
        self.gen.diagraph_chance = diagraph_chance

        self.done(0)

    def pressed_cancel(self):
        log.trace(f"Entered: SettingsDialog.{self.pressed_cancel.__name__}")
        self.done(1)
