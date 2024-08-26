# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 867)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-7, -7, 1241, 881))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget_2 = QWidget(self.layoutWidget)
        self.icon_only_widget_2.setObjectName(u"icon_only_widget_2")
        self.icon_only_widget_2.setMinimumSize(QSize(71, 0))
        self.icon_only_widget_2.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.icon_only_widget_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_5 = QLabel(self.icon_only_widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(40, 40))
        self.label_5.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget_2)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/icons/dashboardsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/dashboardsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.dashboard_1)

        self.instituiton_1 = QPushButton(self.icon_only_widget_2)
        self.instituiton_1.setObjectName(u"instituiton_1")
        icon1 = QIcon()
        icon1.addFile(u":/icons/institutionsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/institutionsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.instituiton_1.setIcon(icon1)
        self.instituiton_1.setIconSize(QSize(100, 16))
        self.instituiton_1.setCheckable(True)
        self.instituiton_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.instituiton_1)

        self.students_1 = QPushButton(self.icon_only_widget_2)
        self.students_1.setObjectName(u"students_1")
        icon2 = QIcon()
        icon2.addFile(u":/icons/studentssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/studentssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.students_1.setIcon(icon2)
        self.students_1.setIconSize(QSize(100, 20))
        self.students_1.setCheckable(True)
        self.students_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.students_1)

        self.teachers_1 = QPushButton(self.icon_only_widget_2)
        self.teachers_1.setObjectName(u"teachers_1")
        icon3 = QIcon()
        icon3.addFile(u":/icons/teacherssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icons/teacherssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers_1.setIcon(icon3)
        self.teachers_1.setIconSize(QSize(100, 20))
        self.teachers_1.setCheckable(True)
        self.teachers_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.teachers_1)

        self.finances_1 = QPushButton(self.icon_only_widget_2)
        self.finances_1.setObjectName(u"finances_1")
        icon4 = QIcon()
        icon4.addFile(u":/icons/financessmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/financessmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finances_1.setIcon(icon4)
        self.finances_1.setIconSize(QSize(100, 20))
        self.finances_1.setCheckable(True)
        self.finances_1.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.finances_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 437, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.settings_1 = QPushButton(self.icon_only_widget_2)
        self.settings_1.setObjectName(u"settings_1")
        icon5 = QIcon()
        icon5.addFile(u":/icons/settingssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/settingssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(100, 20))
        self.settings_1.setCheckable(True)

        self.verticalLayout_10.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.icon_only_widget_2)
        self.signout_1.setObjectName(u"signout_1")
        icon6 = QIcon()
        icon6.addFile(u":/icons/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/signoutsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_1.setIcon(icon6)
        self.signout_1.setIconSize(QSize(100, 20))
        self.signout_1.setCheckable(True)

        self.verticalLayout_10.addWidget(self.signout_1)


        self.verticalLayout_12.addLayout(self.verticalLayout_10)


        self.gridLayout.addWidget(self.icon_only_widget_2, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.layoutWidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"height:30px;\n"
"border: none;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icons/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_14.addLayout(self.horizontalLayout_3)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/dashboard2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/dashboard1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon7)
        self.dashboard_2.setIconSize(QSize(100, 60))
        self.dashboard_2.setCheckable(True)

        self.verticalLayout_15.addWidget(self.dashboard_2)

        self.institution_2 = QPushButton(self.icon_text_widget)
        self.institution_2.setObjectName(u"institution_2")
        self.institution_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-65px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/institution2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icons/institution1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_2.setIcon(icon8)
        self.institution_2.setIconSize(QSize(95, 45))
        self.institution_2.setCheckable(True)

        self.verticalLayout_15.addWidget(self.institution_2)

        self.students_2 = QFrame(self.icon_text_widget)
        self.students_2.setObjectName(u"students_2")
        self.students_2.setFrameShape(QFrame.StyledPanel)
        self.students_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.students_2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.student_2 = QPushButton(self.students_2)
        self.student_2.setObjectName(u"student_2")
        icon9 = QIcon()
        icon9.addFile(u":/icons/students3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/icons/students4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.student_2.setIcon(icon9)
        self.student_2.setIconSize(QSize(200, 60))
        self.student_2.setCheckable(True)

        self.verticalLayout_16.addWidget(self.student_2)

        self.students_dropdown_2 = QFrame(self.students_2)
        self.students_dropdown_2.setObjectName(u"students_dropdown_2")
        self.students_dropdown_2.setFrameShape(QFrame.StyledPanel)
        self.students_dropdown_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.students_dropdown_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.student_info = QPushButton(self.students_dropdown_2)
        self.student_info.setObjectName(u"student_info")
        self.student_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.student_info.setCheckable(True)

        self.verticalLayout_17.addWidget(self.student_info)

        self.student_payment = QPushButton(self.students_dropdown_2)
        self.student_payment.setObjectName(u"student_payment")
        self.student_payment.setStyleSheet(u"QPushButton{\n"
"	padding-left:11px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.student_payment.setCheckable(True)

        self.verticalLayout_17.addWidget(self.student_payment)

        self.student_trans = QPushButton(self.students_dropdown_2)
        self.student_trans.setObjectName(u"student_trans")
        self.student_trans.setStyleSheet(u"QPushButton{\n"
"	padding-left:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.student_trans.setCheckable(True)

        self.verticalLayout_17.addWidget(self.student_trans)


        self.verticalLayout_16.addWidget(self.students_dropdown_2)


        self.verticalLayout_15.addWidget(self.students_2)

        self.teachers_2 = QFrame(self.icon_text_widget)
        self.teachers_2.setObjectName(u"teachers_2")
        self.teachers_2.setFrameShape(QFrame.StyledPanel)
        self.teachers_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.teachers_2)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.teachers_3 = QPushButton(self.teachers_2)
        self.teachers_3.setObjectName(u"teachers_3")
        icon10 = QIcon()
        icon10.addFile(u":/icons/teachers3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/icons/teachers4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teachers_3.setIcon(icon10)
        self.teachers_3.setIconSize(QSize(200, 60))
        self.teachers_3.setCheckable(True)

        self.verticalLayout_18.addWidget(self.teachers_3)

        self.teachers_dropdown_2 = QFrame(self.teachers_2)
        self.teachers_dropdown_2.setObjectName(u"teachers_dropdown_2")
        self.teachers_dropdown_2.setFrameShape(QFrame.StyledPanel)
        self.teachers_dropdown_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.teachers_dropdown_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.teachers_info = QPushButton(self.teachers_dropdown_2)
        self.teachers_info.setObjectName(u"teachers_info")
        self.teachers_info.setStyleSheet(u"QPushButton{\n"
"	padding-left:20px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.teachers_info.setCheckable(True)

        self.verticalLayout_19.addWidget(self.teachers_info)

        self.teachers_payment = QPushButton(self.teachers_dropdown_2)
        self.teachers_payment.setObjectName(u"teachers_payment")
        self.teachers_payment.setStyleSheet(u"QPushButton{\n"
"	padding-left:4px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.teachers_payment.setCheckable(True)

        self.verticalLayout_19.addWidget(self.teachers_payment)

        self.teachers_tranc = QPushButton(self.teachers_dropdown_2)
        self.teachers_tranc.setObjectName(u"teachers_tranc")
        self.teachers_tranc.setStyleSheet(u"QPushButton{\n"
"	padding-left:25px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.teachers_tranc.setCheckable(True)

        self.verticalLayout_19.addWidget(self.teachers_tranc)


        self.verticalLayout_18.addWidget(self.teachers_dropdown_2)


        self.verticalLayout_15.addWidget(self.teachers_2)

        self.finances_2 = QFrame(self.icon_text_widget)
        self.finances_2.setObjectName(u"finances_2")
        self.finances_2.setFrameShape(QFrame.StyledPanel)
        self.finances_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.finances_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.finances_3 = QPushButton(self.finances_2)
        self.finances_3.setObjectName(u"finances_3")
        icon11 = QIcon()
        icon11.addFile(u":/icons/finances3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/icons/finances4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finances_3.setIcon(icon11)
        self.finances_3.setIconSize(QSize(200, 100))
        self.finances_3.setCheckable(True)

        self.verticalLayout_20.addWidget(self.finances_3)

        self.finances_dropdown = QFrame(self.finances_2)
        self.finances_dropdown.setObjectName(u"finances_dropdown")
        self.finances_dropdown.setFrameShape(QFrame.StyledPanel)
        self.finances_dropdown.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.finances_dropdown)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.budgets = QPushButton(self.finances_dropdown)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setStyleSheet(u"QPushButton{\n"
"	padding-left:-40px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.budgets.setCheckable(True)

        self.verticalLayout_21.addWidget(self.budgets)

        self.expences = QPushButton(self.finances_dropdown)
        self.expences.setObjectName(u"expences")
        self.expences.setStyleSheet(u"QPushButton{\n"
"	padding-left:-32px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.expences.setCheckable(True)

        self.verticalLayout_21.addWidget(self.expences)

        self.business_overview = QPushButton(self.finances_dropdown)
        self.business_overview.setObjectName(u"business_overview")
        self.business_overview.setStyleSheet(u"QPushButton{\n"
"	padding-left:13px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #12B298\n"
"\n"
"}")
        self.business_overview.setCheckable(True)

        self.verticalLayout_21.addWidget(self.business_overview)


        self.verticalLayout_20.addWidget(self.finances_dropdown)


        self.verticalLayout_15.addWidget(self.finances_2)


        self.verticalLayout_14.addLayout(self.verticalLayout_15)

        self.verticalSpacer_3 = QSpacerItem(20, 63, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-65px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/icons/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_2.setIcon(icon12)
        self.settings_2.setIconSize(QSize(100, 60))
        self.settings_2.setCheckable(True)

        self.verticalLayout_22.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.icon_text_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setStyleSheet(u"QPushButton{\n"
"	padding-left:-60px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:3px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/signout2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/icons/signout1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.signout_2.setIcon(icon13)
        self.signout_2.setIconSize(QSize(100, 60))
        self.signout_2.setCheckable(True)

        self.verticalLayout_22.addWidget(self.signout_2)


        self.verticalLayout_14.addLayout(self.verticalLayout_22)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border:none")
        icon14 = QIcon()
        icon14.addFile(u":/icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 25, -1, 25)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.header_widget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(72,72,72);")

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(360, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/icons/profile.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(841, 741))
        self.main_screen_widget.setMaximumSize(QSize(920, 741))
        self.main_screen_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 901, 721))
        self.stackedWidget.setMaximumSize(QSize(920, 16777215))
        font3 = QFont()
        font3.setPointSize(8)
        self.stackedWidget.setFont(font3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(320, 270, 161, 151))
        font4 = QFont()
        font4.setPointSize(25)
        self.label_7.setFont(font4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(320, 270, 161, 151))
        self.label_8.setFont(font4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 191, 61))
        self.label_9.setFont(font)
        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 40, 261, 61))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        self.label_19.setFont(font5)
        self.studentinfo_table = QTableWidget(self.page_3)
        if (self.studentinfo_table.columnCount() < 10):
            self.studentinfo_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.studentinfo_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.studentinfo_table.setObjectName(u"studentinfo_table")
        self.studentinfo_table.setGeometry(QRect(0, 220, 950, 501))
        self.studentinfo_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	background-color:black;\n"
"	color:white;\n"
"}\n"
"QTableWidget{\n"
"	alternate-background-color: #BDEDFB;\n"
"	background-color: #F4F9FA;\n"
"}")
        self.studentinfo_table.setAlternatingRowColors(True)
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 100, 381, 43))
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.saveStudent_btn = QPushButton(self.widget)
        self.saveStudent_btn.setObjectName(u"saveStudent_btn")
        self.saveStudent_btn.setMinimumSize(QSize(0, 41))
        self.saveStudent_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0,0,0);\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:12px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icons/add student.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveStudent_btn.setIcon(icon15)

        self.horizontalLayout_6.addWidget(self.saveStudent_btn)

        self.exportExport_btn = QPushButton(self.widget)
        self.exportExport_btn.setObjectName(u"exportExport_btn")
        self.exportExport_btn.setMinimumSize(QSize(0, 41))
        self.exportExport_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:12px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportExport_btn.setIcon(icon16)

        self.horizontalLayout_6.addWidget(self.exportExport_btn)

        self.pdfExport_btn = QPushButton(self.widget)
        self.pdfExport_btn.setObjectName(u"pdfExport_btn")
        self.pdfExport_btn.setMinimumSize(QSize(0, 41))
        self.pdfExport_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255,78,78);\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:12px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pdfExport_btn.setIcon(icon17)

        self.horizontalLayout_6.addWidget(self.pdfExport_btn)

        self.widget1 = QWidget(self.page_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 160, 561, 43))
        self.horizontalLayout_7 = QHBoxLayout(self.widget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.select_gender = QComboBox(self.widget1)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 0))
        self.select_gender.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius: 8px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height:35px;\n"
"	padding-left:15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#298089\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.select_gender)

        self.select_class = QComboBox(self.widget1)
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(150, 0))
        self.select_class.setStyleSheet(u"QComboBox{\n"
"	border: 2px solid white;\n"
"	border-radius: 8px;\n"
"	padding: 1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height:35px;\n"
"	padding-left:15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#298089\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.select_class)

        self.search_student = QLineEdit(self.widget1)
        self.search_student.setObjectName(u"search_student")
        self.search_student.setMinimumSize(QSize(0, 38))
        self.search_student.setMaximumSize(QSize(16777215, 38))
        self.search_student.setStyleSheet(u"QLineEdit{\n"
"	padding-left:20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.search_student)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(290, 210, 271, 151))
        self.label_10.setFont(font4)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(330, 190, 311, 151))
        self.label_11.setFont(font4)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(350, 240, 311, 151))
        self.label_12.setFont(font4)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(290, 270, 281, 151))
        self.label_13.setFont(font4)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(350, 240, 321, 151))
        self.label_14.setFont(font4)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(440, 310, 161, 151))
        self.label_15.setFont(font4)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(370, 260, 161, 151))
        self.label_16.setFont(font4)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(240, 290, 301, 151))
        self.label_17.setFont(font4)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(280, 260, 301, 151))
        self.label_18.setFont(font4)
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_4.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.student_2.toggled.connect(self.students_dropdown_2.setHidden)
        self.teachers_3.toggled.connect(self.teachers_dropdown_2.setHidden)
        self.finances_3.toggled.connect(self.finances_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.institution_2.toggled.connect(self.instituiton_1.setChecked)
        self.student_2.toggled.connect(self.students_1.setChecked)
        self.teachers_3.toggled.connect(self.teachers_1.setChecked)
        self.finances_3.toggled.connect(self.finances_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget_2.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.dashboard_1.setText("")
        self.instituiton_1.setText("")
        self.students_1.setText("")
        self.teachers_1.setText("")
        self.finances_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"School", None))
        self.dashboard_2.setText("")
        self.institution_2.setText("")
        self.student_2.setText("")
        self.student_info.setText(QCoreApplication.translate("MainWindow", u"Student \u0130nformation", None))
        self.student_payment.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.student_trans.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.teachers_3.setText("")
        self.teachers_info.setText(QCoreApplication.translate("MainWindow", u"Teacher \u0130nformation", None))
        self.teachers_payment.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.teachers_tranc.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.finances_3.setText("")
        self.budgets.setText(QCoreApplication.translate("MainWindow", u"Budget", None))
        self.expences.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.business_overview.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.settings_2.setText("")
        self.signout_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello, Mark", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here...", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0130nstitution", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student \u0130nfo", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Welcome to the students information page", None))
        ___qtablewidgetitem = self.studentinfo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.studentinfo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Student id", None));
        ___qtablewidgetitem2 = self.studentinfo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.studentinfo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem4 = self.studentinfo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birthday", None));
        ___qtablewidgetitem5 = self.studentinfo_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem6 = self.studentinfo_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem7 = self.studentinfo_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem8 = self.studentinfo_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem9 = self.studentinfo_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.saveStudent_btn.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.exportExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.pdfExport_btn.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.select_class.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT CLASS", None))
        self.select_class.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.select_class.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.select_class.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.select_class.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.select_class.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.select_class.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.select_class.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.select_class.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.select_class.setItemText(9, QCoreApplication.translate("MainWindow", u"Grade 9", None))
        self.select_class.setItemText(10, QCoreApplication.translate("MainWindow", u"Grade 10", None))
        self.select_class.setItemText(11, QCoreApplication.translate("MainWindow", u"Grade 11", None))
        self.select_class.setItemText(12, QCoreApplication.translate("MainWindow", u"Grade 12", None))

        self.search_student.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Student...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Teacher \u0130nformation", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Budget", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

