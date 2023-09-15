from PyQt5 import QtCore, QtWidgets
from .config import Config
from src.generator_v2 import Generator
from .shading import Mode


class SettingsUI(QtWidgets.QWidget):
    def __init__(self, config: Config, gen: Generator, shading: Mode):
        QtWidgets.QWidget.__init__(self)
        self.config = config
        self.gen = gen
        self.shading = shading

    def setupUi(self, MainWindow):
        MainWindow.resize(550, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        h_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        v_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addItem(v_spacer)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addItem(h_spacer)

        self.label_rare = QtWidgets.QLabel(self.centralwidget)
        self.label_rare.setObjectName("label")
        self.horizontalLayout.addWidget(self.label_rare)

        self.enter_rare = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_rare.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_rare.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.enter_rare)

        self.horizontalLayout.addItem(h_spacer)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addItem(h_spacer)

        self.label_double = QtWidgets.QLabel(self.centralwidget)
        self.label_double.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_double)

        self.enter_double = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_double.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_double.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.enter_double)

        self.horizontalLayout_2.addItem(h_spacer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.addItem(h_spacer)

        self.label_qu = QtWidgets.QLabel(self.centralwidget)
        self.label_qu.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_qu)

        self.enter_qu = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_qu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_qu.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.enter_qu)

        self.horizontalLayout_3.addItem(h_spacer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.addItem(h_spacer)

        self.label_diagraph = QtWidgets.QLabel(self.centralwidget)
        self.label_diagraph.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_diagraph)

        self.enter_diagraph = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_diagraph.setMaximumSize(QtCore.QSize(50, 16777215))
        self.enter_diagraph.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.enter_diagraph)

        self.horizontalLayout_4.addItem(h_spacer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.addItem(h_spacer)

        self.checkbox_popular = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_popular.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_popular.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkbox_popular)

        self.horizontalLayout_5.addItem(h_spacer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addItem(v_spacer)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setMinimumSize(QtCore.QSize(0, 35))
        self.button_save.clicked.connect(lambda: self.pressed_save(MainWindow))
        self.button_save.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.button_save)

        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setMinimumSize(QtCore.QSize(0, 35))
        self.button_cancel.clicked.connect(lambda: self.pressed_cancel(MainWindow))
        self.button_cancel.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.button_cancel)

        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.set_shading(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.label_rare.setText(_translate("MainWindow", "Rare Consonant Chance (%)"))
        self.enter_rare.setText(_translate("MainWindow", str(self.gen.rare_chance)))
        self.label_double.setText(_translate("MainWindow", "Double Letter Chance (%)"))
        self.enter_double.setText(_translate("MainWindow", str(self.gen.double_chance)))
        self.label_qu.setText(_translate("MainWindow", "Qu Chance (%)"))
        self.enter_qu.setText(_translate("MainWindow", str(self.gen.qu_chance)))
        self.label_diagraph.setText(_translate("MainWindow", "Diagraph Chance (%)"))
        self.enter_diagraph.setText(_translate("MainWindow", str(self.gen.diagraph_chance)))
        self.checkbox_popular.setText(_translate("MainWindow", "Show only popular templates?"))
        self.button_save.setText(_translate("MainWindow", "Save"))
        self.button_cancel.setText(_translate("MainWindow", "Cancel"))

    def set_shading(self, window: QtWidgets.QMainWindow):
        window.setStyleSheet(f"background-color:{self.shading.background}; color:{self.shading.text}")

        inset_border = (
            f"border-bottom: 1px solid {self.shading.light_border}; border-right: 1px solid {self.shading.light_border}; "
            f"border-left: 2px solid {self.shading.border}; border-top: 2px solid {self.shading.border}\n")
        hover_boarder = (
            f"border-top: 1px solid {self.shading.light_border}; border-left: 1px solid {self.shading.light_border}; border"
            f"-right: 2px solid {self.shading.border}; border-bottom: 2px solid {self.shading.border}\n")
        outset_boarder = (
            f"border-top: 1px solid {self.shading.light_border}; border-left: 1px solid {self.shading.light_border}; border"
            f"-right: 3px solid {self.shading.border}; border-bottom: 3px solid {self.shading.border}\n")

        self.centralwidget.setStyleSheet("QPushButton {\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 5px;\n"
                                         f"{outset_boarder}"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         f"background-color: {self.shading.hover};\n"
                                         "border-style: outset;\n"
                                         "border-radius: 5px;\n"
                                         f"{hover_boarder}"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "border-style: inset;\n"
                                         "border-radius: 5px;\n"
                                         f"{inset_border}"
                                         "}\n"
                                         "QLineEdit {\n"
                                         f"background-color: {self.shading.edit};\n"
                                         "border-style: outset;\n"
                                         "border-width: 1px;\n"
                                         "border-radius: 5px;\n"
                                         f"{inset_border}"
                                         "}")

    def pressed_save(self, win: QtWidgets.QMainWindow):
        rare_chance = int(self.enter_rare.text())
        double_chance = int(self.enter_double.text())
        qu_chance = int(self.enter_qu.text())
        diagraph_chance = int(self.enter_diagraph.text())

        self.gen.rare_chance = rare_chance
        self.gen.double_chance = double_chance
        self.gen.qu_chance = qu_chance
        self.gen.diagraph_chance = diagraph_chance

        win.close()

    def pressed_cancel(self, win: QtWidgets.QMainWindow):
        win.close()
