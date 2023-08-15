from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class GeneratorUI(object):
    def setup_ui(self, MainWindow):
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
        self.horizontalLayout.addWidget(self.template_sel)
        self.template_sel.addItem("Dog")
        self.template_sel.addItem("Cat")
        self.template_sel.addItem("Raccoon")

        self.num_sel = QtWidgets.QSpinBox(self.centralwidget)
        self.num_sel.setMinimum(1)
        self.num_sel.setMaximum(20)
        self.num_sel.setObjectName("num_sel")
        self.horizontalLayout.addWidget(self.num_sel)

        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setObjectName("generate_button")
        self.horizontalLayout.addWidget(self.generate_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.template_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.template_enter.setObjectName("template_enter")
        self.verticalLayout.addWidget(self.template_enter)

        self.names_list = QtWidgets.QLabel(self.centralwidget)
        self.names_list.setAlignment(QtCore.Qt.AlignCenter)
        self.names_list.setObjectName("names_list")
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = GeneratorUI()
    ui.setup_ui(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
