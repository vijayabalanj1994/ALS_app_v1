# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QLabel, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)
import gui_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1422, 989)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/NeroBioMark_Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_4 = QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_2 = QGroupBox(self.groupBox_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(225, 300))
        self.groupBox_2.setMaximumSize(QSize(225, 325))
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_browse_image = QPushButton(self.groupBox_2)
        self.pb_browse_image.setObjectName(u"pb_browse_image")
        self.pb_browse_image.setMinimumSize(QSize(200, 50))
        self.pb_browse_image.setMaximumSize(QSize(200, 75))

        self.verticalLayout.addWidget(self.pb_browse_image)

        self.lb_input_image = QLabel(self.groupBox_2)
        self.lb_input_image.setObjectName(u"lb_input_image")
        self.lb_input_image.setMinimumSize(QSize(200, 200))
        self.lb_input_image.setMaximumSize(QSize(200, 200))
        self.lb_input_image.setFrameShape(QFrame.WinPanel)
        self.lb_input_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_input_image)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.groupBox_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(425, 450))
        self.groupBox.setMaximumSize(QSize(425, 450))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_cam_image = QLabel(self.groupBox)
        self.lb_cam_image.setObjectName(u"lb_cam_image")
        self.lb_cam_image.setMinimumSize(QSize(400, 400))
        self.lb_cam_image.setFrameShape(QFrame.WinPanel)
        self.lb_cam_image.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_cam_image, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 1, 2, 1)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(425, 450))
        self.groupBox_6.setMaximumSize(QSize(425, 450))
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_filtered_image = QLabel(self.groupBox_6)
        self.lb_filtered_image.setObjectName(u"lb_filtered_image")
        self.lb_filtered_image.setMinimumSize(QSize(400, 400))
        self.lb_filtered_image.setFrameShape(QFrame.WinPanel)
        self.lb_filtered_image.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_filtered_image, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_6, 0, 2, 2, 1)

        self.groupBox_8 = QGroupBox(self.groupBox_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(225, 225))
        self.groupBox_8.setMaximumSize(QSize(225, 225))
        self.groupBox_8.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pb_run_analysis = QPushButton(self.groupBox_8)
        self.pb_run_analysis.setObjectName(u"pb_run_analysis")
        self.pb_run_analysis.setMinimumSize(QSize(200, 50))

        self.verticalLayout_3.addWidget(self.pb_run_analysis)

        self.pb_clear = QPushButton(self.groupBox_8)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setMinimumSize(QSize(200, 50))

        self.verticalLayout_3.addWidget(self.pb_clear)

        self.pb_export_results = QPushButton(self.groupBox_8)
        self.pb_export_results.setObjectName(u"pb_export_results")
        self.pb_export_results.setMinimumSize(QSize(200, 50))

        self.verticalLayout_3.addWidget(self.pb_export_results)


        self.gridLayout_4.addWidget(self.groupBox_8, 1, 0, 2, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(850, 75))
        self.groupBox_7.setMaximumSize(QSize(850, 75))
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.s_filter_slider = QSlider(self.groupBox_7)
        self.s_filter_slider.setObjectName(u"s_filter_slider")
        self.s_filter_slider.setMinimumSize(QSize(800, 25))
        self.s_filter_slider.setMaximumSize(QSize(16777215, 25))
        self.s_filter_slider.setMaximum(100)
        self.s_filter_slider.setOrientation(Qt.Horizontal)
        self.s_filter_slider.setTickPosition(QSlider.TicksBothSides)

        self.gridLayout_3.addWidget(self.s_filter_slider, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_7, 2, 1, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_9 = QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_4 = QGroupBox(self.groupBox_9)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(250, 250))
        self.groupBox_4.setMaximumSize(QSize(16777215, 250))
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox_4)
        self.formLayout.setObjectName(u"formLayout")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(200, 75))
        self.label_10.setStyleSheet(u"background-color: #FFC107;\n"
"color: white;\n"
"padding: 4px;\n"
"border-radius: 3px;")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_10)

        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(110, 25))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.p_bar_concordant = QProgressBar(self.groupBox_4)
        self.p_bar_concordant.setObjectName(u"p_bar_concordant")
        self.p_bar_concordant.setMinimumSize(QSize(110, 25))
        self.p_bar_concordant.setValue(24)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.p_bar_concordant)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(110, 25))

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_13)

        self.p_bar_discordant = QProgressBar(self.groupBox_4)
        self.p_bar_discordant.setObjectName(u"p_bar_discordant")
        self.p_bar_discordant.setMinimumSize(QSize(110, 25))
        self.p_bar_discordant.setValue(24)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.p_bar_discordant)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(110, 25))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.p_bar_control = QProgressBar(self.groupBox_4)
        self.p_bar_control.setObjectName(u"p_bar_control")
        self.p_bar_control.setMinimumSize(QSize(110, 25))
        self.p_bar_control.setValue(24)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.p_bar_control)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.groupBox_9)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(250, 275))
        self.groupBox_3.setMaximumSize(QSize(16777215, 275))
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 25))

        self.verticalLayout_2.addWidget(self.label_4)

        self.lb_image_no = QLabel(self.groupBox_3)
        self.lb_image_no.setObjectName(u"lb_image_no")
        self.lb_image_no.setMinimumSize(QSize(200, 25))
        self.lb_image_no.setStyleSheet(u"background-color: #1976D2;\n"
"color: white;\n"
"padding: 4px;\n"
"border-radius: 3px;")

        self.verticalLayout_2.addWidget(self.lb_image_no)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 25))

        self.verticalLayout_2.addWidget(self.label_5)

        self.lb_case_id = QLabel(self.groupBox_3)
        self.lb_case_id.setObjectName(u"lb_case_id")
        self.lb_case_id.setMinimumSize(QSize(200, 25))
        self.lb_case_id.setStyleSheet(u"background-color: #1976D2;\n"
"color: white;\n"
"padding: 4px;\n"
"border-radius: 3px;")

        self.verticalLayout_2.addWidget(self.lb_case_id)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(200, 25))

        self.verticalLayout_2.addWidget(self.label_6)

        self.lb_region = QLabel(self.groupBox_3)
        self.lb_region.setObjectName(u"lb_region")
        self.lb_region.setMinimumSize(QSize(200, 25))
        self.lb_region.setStyleSheet(u"background-color: #1976D2;\n"
"color: white;\n"
"padding: 4px;\n"
"border-radius: 3px;")

        self.verticalLayout_2.addWidget(self.lb_region)


        self.verticalLayout_4.addWidget(self.groupBox_3)


        self.gridLayout_5.addWidget(self.groupBox_9, 0, 1, 1, 1)

        self.te_notes = QTextEdit(self.centralwidget)
        self.te_notes.setObjectName(u"te_notes")
        self.te_notes.setMinimumSize(QSize(1400, 300))
        self.te_notes.setFrameShape(QFrame.WinPanel)

        self.gridLayout_5.addWidget(self.te_notes, 1, 0, 1, 2)

        self.lb_status = QLabel(self.centralwidget)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setMinimumSize(QSize(1400, 25))
        self.lb_status.setMaximumSize(QSize(16777215, 25))
        self.lb_status.setStyleSheet(u"background-color: #F44336;  /* Material Design red */\n"
"color: white;\n"
"padding: 4px;\n"
"border-radius: 3px;")
        self.lb_status.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_status, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1422, 34))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ALS Diagnostic Assistant", None))
        self.groupBox_5.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.pb_browse_image.setText(QCoreApplication.translate("MainWindow", u"Browse Image", None))
        self.lb_input_image.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"CAM Image Viewer", None))
        self.lb_cam_image.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Filtered Image Viewer", None))
        self.lb_filtered_image.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.pb_run_analysis.setText(QCoreApplication.translate("MainWindow", u"Run Analysis", None))
        self.pb_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pb_export_results.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Filter Slider ", None))
        self.groupBox_9.setTitle("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Model Diagnosis:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Concordant:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Discordant:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Control:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Meta Data", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Image No:", None))
        self.lb_image_no.setText(QCoreApplication.translate("MainWindow", u"0-9", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Case ID:", None))
        self.lb_case_id.setText(QCoreApplication.translate("MainWindow", u"0-9/A-Z/a-z", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Region:", None))
        self.lb_region.setText(QCoreApplication.translate("MainWindow", u"0-9/A-Z", None))
        self.te_notes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your notes or observations here...", None))
        self.lb_status.setText(QCoreApplication.translate("MainWindow", u"Status: Waiting for Image", None))
    # retranslateUi

