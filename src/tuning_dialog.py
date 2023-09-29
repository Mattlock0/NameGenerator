# system imports
from pathlib import Path
import math

# qt imports
from PyQt5 import QtCore, QtWidgets

# project imports
from src.generator_v2 import Generator
from src.utils import *


class TuningDialog(QtWidgets.QDialog):
    def __init__(self, gen: Generator, font_size: int):
        super().__init__()
        self.gen = gen
        self.main_font_size = font_size
        self.header_font_size = font_size + 4

    def setup_ui(self, shading: Mode):
        log.trace(f"Entered: TuningDialog.{self.setup_ui.__name__}")
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

        # HEADER: Letter Generation
        self.header_letter_gen = QtWidgets.QLabel(self)
        self.header_letter_gen.setAlignment(QtCore.Qt.AlignCenter)
        self.header_letter_gen.setFont(get_font(self.header_font_size))
        self.header_letter_gen.setObjectName("header_letter_gen")
        self.layout_main.addWidget(self.header_letter_gen)

        # rare chance
        self.layout_rare = QtWidgets.QHBoxLayout()
        self.layout_rare.setObjectName("layout_rare")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_rare.addItem(spacerItem1)
        self.label_rare = QtWidgets.QLabel(self)
        self.label_rare.setFont(get_font(self.main_font_size))
        self.label_rare.setObjectName("label_rare")
        self.layout_rare.addWidget(self.label_rare)
        self.slider_rare = QtWidgets.QSlider(self)
        self.slider_rare.setOrientation(QtCore.Qt.Horizontal)
        self.slider_rare.setMinimum(0)
        self.slider_rare.setMaximum(100)
        self.slider_rare.valueChanged.connect(self.update_percents)
        self.slider_rare.setObjectName("slider_rare")
        self.layout_rare.addWidget(self.slider_rare)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_rare.addItem(spacerItem2)
        self.layout_main.addLayout(self.layout_rare)

        # diagraph chance
        self.layout_diagraph = QtWidgets.QHBoxLayout()
        self.layout_diagraph.setObjectName("layout_diagraph")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_diagraph.addItem(spacerItem3)
        self.label_diagraph = QtWidgets.QLabel(self)
        self.label_diagraph.setFont(get_font(self.main_font_size))
        self.label_diagraph.setObjectName("label_diagraph")
        self.layout_diagraph.addWidget(self.label_diagraph)
        self.slider_diagraph = QtWidgets.QSlider(self)
        self.slider_diagraph.setOrientation(QtCore.Qt.Horizontal)
        self.slider_diagraph.setMinimum(0)
        self.slider_diagraph.setMaximum(100)
        self.slider_diagraph.valueChanged.connect(self.update_percents)
        self.slider_diagraph.setObjectName("slider_diagraph")
        self.layout_diagraph.addWidget(self.slider_diagraph)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_diagraph.addItem(spacerItem4)
        self.layout_main.addLayout(self.layout_diagraph)

        # double chance
        self.layout_double = QtWidgets.QHBoxLayout()
        self.layout_double.setObjectName("layout_double")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_double.addItem(spacerItem5)
        self.label_double = QtWidgets.QLabel(self)
        self.label_double.setFont(get_font(self.main_font_size))
        self.label_double.setObjectName("label_double")
        self.layout_double.addWidget(self.label_double)
        self.slider_double = QtWidgets.QSlider(self)
        self.slider_double.setOrientation(QtCore.Qt.Horizontal)
        self.slider_double.setMinimum(0)
        self.slider_double.setMaximum(100)
        self.slider_double.valueChanged.connect(self.update_percents)
        self.slider_double.setObjectName("slider_double")
        self.layout_double.addWidget(self.slider_double)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_double.addItem(spacerItem6)
        self.layout_main.addLayout(self.layout_double)

        # common chance
        self.layout_common = QtWidgets.QHBoxLayout()
        self.layout_common.setObjectName("layout_common")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_common.addItem(spacerItem7)
        self.label_common = QtWidgets.QLabel(self)
        self.label_common.setFont(get_font(self.main_font_size))
        self.label_common.setObjectName("label_common")
        self.layout_common.addWidget(self.label_common)
        self.slider_common = QtWidgets.QSlider(self)
        self.slider_common.setOrientation(QtCore.Qt.Horizontal)
        self.slider_common.setMinimum(0)
        self.slider_common.setMaximum(100)
        self.slider_common.valueChanged.connect(self.update_percents)
        self.slider_common.setObjectName("slider_common")
        self.layout_common.addWidget(self.slider_common)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_common.addItem(spacerItem8)
        self.layout_main.addLayout(self.layout_common)

        # spacer line 1
        self.layout_line_1 = QtWidgets.QHBoxLayout()
        self.layout_line_1.setObjectName("layout_line_1")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_line_1.addItem(spacerItem13)
        self.line_1 = QtWidgets.QFrame(self)
        self.line_1.setMinimumSize(QtCore.QSize(300, 0))
        self.line_1.setMaximumSize(QtCore.QSize(500, 16777215))
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_1")
        self.layout_line_1.addWidget(self.line_1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_line_1.addItem(spacerItem14)
        self.layout_main.addLayout(self.layout_line_1)

        # HEADER: Letter Replacement
        self.header_replacement = QtWidgets.QLabel(self)
        self.header_replacement.setAlignment(QtCore.Qt.AlignCenter)
        self.header_replacement.setFont(get_font(self.header_font_size))
        self.header_replacement.setObjectName("header_replacement")
        self.layout_main.addWidget(self.header_replacement)

        # qu replacement
        self.layout_qu = QtWidgets.QHBoxLayout()
        self.layout_qu.setObjectName("layout_qu")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_qu.addItem(spacerItem15)
        self.label_qu = QtWidgets.QLabel(self)
        self.label_qu.setFont(get_font(self.main_font_size))
        self.label_qu.setObjectName("label_qu")
        self.layout_qu.addWidget(self.label_qu)
        self.slider_qu = QtWidgets.QSlider(self)
        self.slider_qu.setOrientation(QtCore.Qt.Horizontal)
        self.slider_qu.setMinimum(0)
        self.slider_qu.setMaximum(100)
        self.slider_qu.valueChanged.connect(self.update_percents)
        self.slider_qu.setObjectName("slider_qu")
        self.layout_qu.addWidget(self.slider_qu)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_qu.addItem(spacerItem16)
        self.layout_main.addLayout(self.layout_qu)

        # xs replacement
        self.layout_xs = QtWidgets.QHBoxLayout()
        self.layout_xs.setObjectName("layout_xs")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_xs.addItem(spacerItem17)
        self.label_xs = QtWidgets.QLabel(self)
        self.label_xs.setFont(get_font(self.main_font_size))
        self.label_xs.setObjectName("label_xs")
        self.layout_xs.addWidget(self.label_xs)
        self.slider_xs = QtWidgets.QSlider(self)
        self.slider_xs.setOrientation(QtCore.Qt.Horizontal)
        self.slider_xs.setMinimum(0)
        self.slider_xs.setMaximum(100)
        self.slider_xs.valueChanged.connect(self.update_percents)
        self.slider_xs.setObjectName("slider_xs")
        self.layout_xs.addWidget(self.slider_xs)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_xs.addItem(spacerItem18)
        self.layout_main.addLayout(self.layout_xs)

        # spacer line 2
        self.layout_line_2 = QtWidgets.QHBoxLayout()
        self.layout_line_2.setObjectName("layout_line_2")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_line_2.addItem(spacerItem19)
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setMinimumSize(QtCore.QSize(300, 0))
        self.line_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layout_line_2.addWidget(self.line_2)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_line_2.addItem(spacerItem20)
        self.layout_main.addLayout(self.layout_line_2)

        # HEADER: Enforcers
        self.header_enforcers = QtWidgets.QLabel(self)
        self.header_enforcers.setAlignment(QtCore.Qt.AlignCenter)
        self.header_enforcers.setFont(get_font(self.header_font_size))
        self.header_enforcers.setObjectName("header_enforcers")
        self.layout_main.addWidget(self.header_enforcers)

        # beginning double letters
        self.layout_beginning_double = QtWidgets.QHBoxLayout()
        self.layout_beginning_double.setObjectName("layout_beginning_double")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_beginning_double.addItem(spacerItem21)
        self.checkbox_beginning_double = QtWidgets.QCheckBox(self)
        self.checkbox_beginning_double.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_beginning_double.setFont(get_font(self.main_font_size))
        self.checkbox_beginning_double.setObjectName("checkbox_beginning_double")
        self.layout_beginning_double.addWidget(self.checkbox_beginning_double)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_beginning_double.addItem(spacerItem22)
        self.layout_main.addLayout(self.layout_beginning_double)

        # remove ending js
        self.layout_ending_j = QtWidgets.QHBoxLayout()
        self.layout_ending_j.setObjectName("layout_ending_j")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_ending_j.addItem(spacerItem23)
        self.checkbox_ending_j = QtWidgets.QCheckBox(self)
        self.checkbox_ending_j.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_ending_j.setFont(get_font(self.main_font_size))
        self.checkbox_ending_j.setObjectName("checkbox_ending_j")
        self.layout_ending_j.addWidget(self.checkbox_ending_j)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_ending_j.addItem(spacerItem24)
        self.layout_main.addLayout(self.layout_ending_j)

        # remove ending vs
        self.layout_ending_v = QtWidgets.QHBoxLayout()
        self.layout_ending_v.setObjectName("layout_ending_v")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_ending_v.addItem(spacerItem25)
        self.checkbox_ending_v = QtWidgets.QCheckBox(self)
        self.checkbox_ending_v.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_ending_v.setFont(get_font(self.main_font_size))
        self.checkbox_ending_v.setObjectName("checkbox_ending_v")
        self.layout_ending_v.addWidget(self.checkbox_ending_v)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_ending_v.addItem(spacerItem26)
        self.layout_main.addLayout(self.layout_ending_v)

        # add double letters to endings
        self.layout_ending_double = QtWidgets.QHBoxLayout()
        self.layout_ending_double.setObjectName("layout_ending_double")
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_ending_double.addItem(spacerItem27)
        self.checkbox_ending_double = QtWidgets.QCheckBox(self)
        self.checkbox_ending_double.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_ending_double.setFont(get_font(self.main_font_size))
        self.checkbox_ending_double.setObjectName("checkbox_ending_double")
        self.layout_ending_double.addWidget(self.checkbox_ending_double)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_ending_double.addItem(spacerItem28)
        self.layout_main.addLayout(self.layout_ending_double)

        # begin and end names with y
        self.layout_beg_end_y = QtWidgets.QHBoxLayout()
        self.layout_beg_end_y.setObjectName("layout_beg_end_y")
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_beg_end_y.addItem(spacerItem29)
        self.checkbox_beginning_ending_y = QtWidgets.QCheckBox(self)
        self.checkbox_beginning_ending_y.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_beginning_ending_y.setFont(get_font(self.main_font_size))
        self.checkbox_beginning_ending_y.setObjectName("checkbox_beg_end_y")
        self.layout_beg_end_y.addWidget(self.checkbox_beginning_ending_y)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_beg_end_y.addItem(spacerItem30)
        self.layout_main.addLayout(self.layout_beg_end_y)

        # add y as a consonant
        self.layout_y_consonant = QtWidgets.QHBoxLayout()
        self.layout_y_consonant.setObjectName("layout_y_consonant")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_y_consonant.addItem(spacerItem11)
        self.checkbox_y_consonant = QtWidgets.QCheckBox(self)
        self.checkbox_y_consonant.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkbox_y_consonant.setFont(get_font(self.main_font_size))
        self.checkbox_y_consonant.setObjectName("checkbox_y_consonant")
        self.layout_y_consonant.addWidget(self.checkbox_y_consonant)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_y_consonant.addItem(spacerItem12)
        self.layout_main.addLayout(self.layout_y_consonant)

        # spacer line 3
        self.layout_line_3 = QtWidgets.QHBoxLayout()
        self.layout_line_3.setObjectName("layout_line_3")
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_line_3.addItem(spacerItem31)
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setMinimumSize(QtCore.QSize(300, 0))
        self.line_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.layout_line_3.addWidget(self.line_3)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_line_3.addItem(spacerItem32)
        self.layout_main.addLayout(self.layout_line_3)

        # HEADER: Import/Export
        self.header_import_export = QtWidgets.QLabel(self)
        self.header_import_export.setAlignment(QtCore.Qt.AlignCenter)
        self.header_import_export.setFont(get_font(self.header_font_size))
        self.header_import_export.setObjectName("header_import_export")
        self.layout_main.addWidget(self.header_import_export)

        # import and output buttons
        self.layout_import_export = QtWidgets.QHBoxLayout()
        self.layout_import_export.setObjectName("layout_import_export")
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_import_export.addItem(spacerItem33)
        self.button_import = QtWidgets.QPushButton(self)
        self.button_import.setMaximumSize(QtCore.QSize(200, 16777215))
        self.button_import.setFont(get_font(self.main_font_size))
        self.button_import.setObjectName("button_import")
        self.button_import.clicked.connect(self.pressed_import)
        self.layout_import_export.addWidget(self.button_import)
        self.button_export = QtWidgets.QPushButton(self)
        self.button_export.setMaximumSize(QtCore.QSize(200, 16777215))
        self.button_export.setFont(get_font(self.main_font_size))
        self.button_export.setObjectName("button_export")
        self.button_export.clicked.connect(self.pressed_export)
        self.layout_import_export.addWidget(self.button_export)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_import_export.addItem(spacerItem34)
        self.layout_main.addLayout(self.layout_import_export)

        # bottom spacer
        self.gridLayout.addLayout(self.layout_main, 1, 0, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem35, 2, 0, 1, 1)

        # save and cancel buttons
        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.layout_buttons.setObjectName("layout_buttons")
        self.button_save = QtWidgets.QPushButton(self)
        self.button_save.setMinimumSize(QtCore.QSize(0, 35))
        self.button_save.setFont(get_font(self.main_font_size))
        self.button_save.setObjectName("button_save")
        self.button_save.clicked.connect(self.pressed_save)
        self.button_save.setDefault(True)
        self.layout_buttons.addWidget(self.button_save)
        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setMinimumSize(QtCore.QSize(0, 35))
        self.button_cancel.setFont(get_font(self.main_font_size))
        self.button_cancel.setObjectName("button_cancel")
        self.button_cancel.clicked.connect(self.pressed_cancel)
        self.layout_buttons.addWidget(self.button_cancel)
        self.gridLayout.addLayout(self.layout_buttons, 3, 0, 1, 1)

        self.set_shading()
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        log.trace(f"Entered: TuningDialog.{self.retranslate_ui.__name__}")
        _translate = QtCore.QCoreApplication.translate
        window_title = "Tuning"
        self.setWindowTitle(_translate(window_title, window_title))

        rare_text = "Rare Consonant Chance"
        diagraph_text = "Diagraph Chance"
        double_text = "Double Letter Chance"
        common_text = "Common Pairs Chance"
        qu_text = "Qu Replace"
        xs_text = "Xs Replace"

        self.set_min(self.label_rare, rare_text)
        self.set_min(self.label_diagraph, diagraph_text)
        self.set_min(self.label_double, double_text)
        self.set_min(self.label_common, common_text)
        self.set_min(self.label_qu, qu_text)
        self.set_min(self.label_xs, xs_text)

        # letter generation
        self.header_letter_gen.setText(_translate(window_title, "Letter Generation"))
        self.label_rare.setText(_translate(window_title, f"{rare_text} ({self.slider_rare.value()}%)"))
        self.label_diagraph.setText(_translate(window_title, f"{diagraph_text} ({self.slider_diagraph.value()}%)"))
        self.label_double.setText(_translate(window_title, f"{double_text} ({self.slider_double.value()}%)"))
        self.label_common.setText(_translate(window_title, f"{common_text} ({self.slider_common.value()}%)"))

        # replacement
        self.header_replacement.setText(_translate(window_title, "Pair Replacement"))
        self.label_qu.setText(_translate(window_title, f"Qu Replace ({self.slider_qu.value()}%)"))
        self.label_xs.setText(_translate(window_title, f"Xs Replace ({self.slider_xs.value()}%)"))

        # enforcers
        self.header_enforcers.setText(_translate(window_title, "Enforcers"))
        self.checkbox_beginning_double.setText(_translate(window_title, "Beginning: No double letters"))
        self.checkbox_ending_j.setText(_translate(window_title, "Ending: No \"J\"s"))
        self.checkbox_ending_v.setText(_translate(window_title, "Ending: No \"V\"s"))
        self.checkbox_ending_double.setText(_translate(window_title, "Ending: Double \"F\", \"L\", and \"S\"s"))
        self.checkbox_beginning_ending_y.setText(_translate(window_title, "Beginning/Ending: \"Y\" Bias"))
        self.checkbox_y_consonant.setText(_translate(window_title, "Include \"Y\" as Consonant"))

        # import/export
        self.header_import_export.setText(_translate(window_title, "Tuning Batch Importing/Exporting"))
        self.button_import.setText(_translate(window_title, "Import"))
        self.button_export.setText(_translate(window_title, "Export"))

        # save/cancel
        self.button_save.setText(_translate(window_title, "Save"))
        self.button_cancel.setText(_translate(window_title, "Cancel"))

        # setup the variable labels
        self.initialize_tunings()

    def set_shading(self):
        log.trace(f"Entered: TuningDialog.{self.set_shading.__name__}")
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

    def initialize_tunings(self):
        log.trace(f"Entered: TuningDialog.{self.initialize_tunings.__name__}")

        # first, chances
        self.slider_rare.setValue(self.gen.rare_chance)
        self.slider_diagraph.setValue(self.gen.diagraph_chance)
        self.slider_double.setValue(self.gen.double_chance)
        self.slider_common.setValue(self.gen.common_chance)
        self.slider_qu.setValue(self.gen.qu_chance)
        self.slider_xs.setValue(self.gen.xs_chance)

        # then the enforcers
        self.checkbox_beginning_double.setChecked(self.gen.beginning_double)
        self.checkbox_ending_j.setChecked(self.gen.ending_j)
        self.checkbox_ending_v.setChecked(self.gen.ending_v)
        self.checkbox_ending_double.setChecked(self.gen.ending_double)
        self.checkbox_beginning_ending_y.setChecked(self.gen.beginning_ending_y)
        self.checkbox_y_consonant.setChecked(self.gen.y_consonant)

    def set_min(self, label: QtWidgets.QLabel, text: str) -> None:
        max_percent = " (100%)"
        width = len(text + max_percent) * (self.main_font_size - 2)  # this looks kind of ugly, but it works
        label.setMinimumWidth(width)

    def update_percents(self) -> None:
        self.label_rare.setText(f"Rare Consonant Chance ({self.slider_rare.value()}%)")
        self.label_diagraph.setText(f"Diagraph Chance ({self.slider_diagraph.value()}%)")
        self.label_double.setText(f"Double Letter Chance ({self.slider_double.value()}%)")
        self.label_common.setText(f"Common Pairs Chance ({self.slider_common.value()}%)")
        self.label_qu.setText(f"Qu Replace ({self.slider_qu.value()}%)")
        self.label_xs.setText(f"Xs Replace ({self.slider_xs.value()}%)")

    def pressed_import(self) -> None:
        log.trace(f"Entered: TuningDialog.{self.pressed_import.__name__}")

        # setup the file dialog
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Ini files (*.ini)")
        filename = ""

        # execute it and extract the filepath
        if file_dialog.exec_():
            filename = file_dialog.selectedFiles()[0]

        # read that file path into the generator
        if not filename == "":
            self.gen.tuning.import_tuning(filename)
            self.gen.read_tunings()
            self.initialize_tunings()
        else:
            log.warning("No settings file chosen.")

    def pressed_export(self) -> None:
        log.trace(f"Entered: TuningDialog.{self.pressed_export.__name__}")

        # save to file
        tuning_path = 'tuning.ini'
        log.info(f'Saving tunings to {tuning_path}...')
        self.gen.tuning.export_tuning(Path(tuning_path))

    def pressed_save(self) -> None:
        log.trace(f"Entered: TuningDialog.{self.pressed_save.__name__}")

        # update generator chances
        self.gen.rare_chance = self.slider_rare.value()
        self.gen.diagraph_chance = self.slider_diagraph.value()
        self.gen.double_chance = self.slider_double.value()
        self.gen.common_chance = self.slider_common.value()
        self.gen.qu_chance = self.slider_qu.value()
        self.gen.xs_chance = self.slider_xs.value()

        self.done(0)

    def pressed_cancel(self) -> None:
        log.trace(f"Entered: TuningDialog.{self.pressed_cancel.__name__}")
        self.done(1)
