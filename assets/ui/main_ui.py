# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 301)
        self.main_container = QWidget(MainWindow)
        self.main_container.setObjectName(u"main_container")
        self.verticalLayout_4 = QVBoxLayout(self.main_container)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.title_layout = QHBoxLayout()
        self.title_layout.setObjectName(u"title_layout")
        self.title_lbl = QLabel(self.main_container)
        self.title_lbl.setObjectName(u"title_lbl")

        self.title_layout.addWidget(self.title_lbl)

        self.title_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.title_layout.addItem(self.title_spacer)


        self.verticalLayout_4.addLayout(self.title_layout)

        self.body1_layout = QHBoxLayout()
        self.body1_layout.setObjectName(u"body1_layout")
        self.prompt_layout = QVBoxLayout()
        self.prompt_layout.setSpacing(0)
        self.prompt_layout.setObjectName(u"prompt_layout")
        self.prompt_lbl = QLabel(self.main_container)
        self.prompt_lbl.setObjectName(u"prompt_lbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prompt_lbl.sizePolicy().hasHeightForWidth())
        self.prompt_lbl.setSizePolicy(sizePolicy)
        self.prompt_lbl.setMargin(4)

        self.prompt_layout.addWidget(self.prompt_lbl)

        self.prompt_txt = QTextEdit(self.main_container)
        self.prompt_txt.setObjectName(u"prompt_txt")

        self.prompt_layout.addWidget(self.prompt_txt)


        self.body1_layout.addLayout(self.prompt_layout)

        self.voices_layout = QVBoxLayout()
        self.voices_layout.setSpacing(0)
        self.voices_layout.setObjectName(u"voices_layout")
        self.voices_title_layout = QHBoxLayout()
        self.voices_title_layout.setObjectName(u"voices_title_layout")
        self.voices_title_layout.setContentsMargins(-1, -1, -1, 0)
        self.voices_lbl = QLabel(self.main_container)
        self.voices_lbl.setObjectName(u"voices_lbl")

        self.voices_title_layout.addWidget(self.voices_lbl)

        self.voices_spacer = QSpacerItem(40, 8, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.voices_title_layout.addItem(self.voices_spacer)

        self.voices_reload_btn = QToolButton(self.main_container)
        self.voices_reload_btn.setObjectName(u"voices_reload_btn")

        self.voices_title_layout.addWidget(self.voices_reload_btn)


        self.voices_layout.addLayout(self.voices_title_layout)

        self.voices_list = QListWidget(self.main_container)
        self.voices_list.setObjectName(u"voices_list")
        self.voices_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.voices_layout.addWidget(self.voices_list)


        self.body1_layout.addLayout(self.voices_layout)


        self.verticalLayout_4.addLayout(self.body1_layout)

        self.body2_layout = QHBoxLayout()
        self.body2_layout.setSpacing(6)
        self.body2_layout.setObjectName(u"body2_layout")
        self.body2_layout.setContentsMargins(-1, 0, -1, -1)
        self.samples_layout = QVBoxLayout()
        self.samples_layout.setSpacing(0)
        self.samples_layout.setObjectName(u"samples_layout")
        self.samples_lbl = QLabel(self.main_container)
        self.samples_lbl.setObjectName(u"samples_lbl")

        self.samples_layout.addWidget(self.samples_lbl)

        self.samples_spin_box = QSpinBox(self.main_container)
        self.samples_spin_box.setObjectName(u"samples_spin_box")
        self.samples_spin_box.setMinimum(1)
        self.samples_spin_box.setMaximum(10)

        self.samples_layout.addWidget(self.samples_spin_box)


        self.body2_layout.addLayout(self.samples_layout)

        self.quality_layout = QVBoxLayout()
        self.quality_layout.setSpacing(0)
        self.quality_layout.setObjectName(u"quality_layout")
        self.label_5 = QLabel(self.main_container)
        self.label_5.setObjectName(u"label_5")

        self.quality_layout.addWidget(self.label_5)

        self.quality_combo_box = QComboBox(self.main_container)
        self.quality_combo_box.addItem("")
        self.quality_combo_box.addItem("")
        self.quality_combo_box.addItem("")
        self.quality_combo_box.addItem("")
        self.quality_combo_box.setObjectName(u"quality_combo_box")

        self.quality_layout.addWidget(self.quality_combo_box)


        self.body2_layout.addLayout(self.quality_layout)


        self.verticalLayout_4.addLayout(self.body2_layout)

        self.body3_layout = QHBoxLayout()
        self.body3_layout.setObjectName(u"body3_layout")
        self.body3_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.body3_layout.addItem(self.body3_spacer)

        self.generate_btn = QPushButton(self.main_container)
        self.generate_btn.setObjectName(u"generate_btn")

        self.body3_layout.addWidget(self.generate_btn)

        self.output_btn = QToolButton(self.main_container)
        self.output_btn.setObjectName(u"output_btn")

        self.body3_layout.addWidget(self.output_btn)


        self.verticalLayout_4.addLayout(self.body3_layout)

        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")
        self.result_layout.setContentsMargins(-1, 15, -1, -1)

        self.verticalLayout_4.addLayout(self.result_layout)

        MainWindow.setCentralWidget(self.main_container)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_lbl.setText(QCoreApplication.translate("MainWindow", u"Tortoise TTS", None))
        self.prompt_lbl.setText(QCoreApplication.translate("MainWindow", u"Write your Prompt", None))
        self.voices_lbl.setText(QCoreApplication.translate("MainWindow", u"Select a voice:", None))
        self.samples_lbl.setText(QCoreApplication.translate("MainWindow", u"Samples:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Quality", None))
        self.quality_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"high_quality", None))
        self.quality_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"standard", None))
        self.quality_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"fast", None))
        self.quality_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"ultra_fast", None))

        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
    # retranslateUi

