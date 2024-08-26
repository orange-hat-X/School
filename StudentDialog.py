# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studentDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,QMessageBox,QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

import mysql.connector
from random import randint
from datetime import datetime


class Ui_StuentsDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        self.resize(548, 584)
        self.setStyleSheet(u"QDialog{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height: 35px;\n"
"}\n"
"QDateEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height: 31px;\n"
"}\n"
"QComboBox{\n"
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
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 241, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 90, 501, 401))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.layoutWidget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.name_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.layoutWidget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.verticalLayout_5.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.class_comboBox = QComboBox(self.layoutWidget)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")

        self.verticalLayout_6.addWidget(self.class_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.layoutWidget)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")

        self.verticalLayout_7.addWidget(self.dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.address_lineEdit = QLineEdit(self.layoutWidget)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.address_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.phone_lineEdit = QLineEdit(self.layoutWidget)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.phone_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.email_lineEdit = QLineEdit(self.layoutWidget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.email_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(310, 510, 221, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveStudent_btn = QPushButton(self.layoutWidget1)
        self.saveStudent_btn.setObjectName(u"saveStudent_btn")
        self.saveStudent_btn.setMinimumSize(QSize(0, 41))
        self.saveStudent_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.saveStudent_btn)

        self.cancel_btn = QPushButton(self.layoutWidget1)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 41))
        self.cancel_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.cancel_btn)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, StuentsDialog):
        StuentsDialog.setWindowTitle(QCoreApplication.translate("StuentsDialog", u"Students Dialog", None))
        self.label.setText(QCoreApplication.translate("StuentsDialog", u"Add New Student", None))
        self.label_2.setText(QCoreApplication.translate("StuentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("StuentsDialog", u"Select Gender", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StuentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StuentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("StuentsDialog", u"Select Class", None))
        self.class_comboBox.setItemText(0, QCoreApplication.translate("StuentsDialog", u"Grade 1", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("StuentsDialog", u"Grade 2", None))
        self.class_comboBox.setItemText(2, QCoreApplication.translate("StuentsDialog", u"Grade 3", None))
        self.class_comboBox.setItemText(3, QCoreApplication.translate("StuentsDialog", u"Grade 4", None))
        self.class_comboBox.setItemText(4, QCoreApplication.translate("StuentsDialog", u"Grade 5", None))
        self.class_comboBox.setItemText(5, QCoreApplication.translate("StuentsDialog", u"Grade 6", None))
        self.class_comboBox.setItemText(6, QCoreApplication.translate("StuentsDialog", u"Grade 7", None))
        self.class_comboBox.setItemText(7, QCoreApplication.translate("StuentsDialog", u"Grade 8", None))
        self.class_comboBox.setItemText(8, QCoreApplication.translate("StuentsDialog", u"Grade 9", None))
        self.class_comboBox.setItemText(9, QCoreApplication.translate("StuentsDialog", u"Grade 10", None))
        self.class_comboBox.setItemText(10, QCoreApplication.translate("StuentsDialog", u"Grade 11", None))
        self.class_comboBox.setItemText(11, QCoreApplication.translate("StuentsDialog", u"Grade 12", None))

        self.label_8.setText(QCoreApplication.translate("StuentsDialog", u"Date Of Birth", None))
        self.label_3.setText(QCoreApplication.translate("StuentsDialog", u"Address", None))
        self.label_4.setText(QCoreApplication.translate("StuentsDialog", u"Phone Number", None))
        self.label_5.setText(QCoreApplication.translate("StuentsDialog", u"Email", None))
        self.saveStudent_btn.setText(QCoreApplication.translate("StuentsDialog", u"Add Student", None))
        self.cancel_btn.setText(QCoreApplication.translate("StuentsDialog", u"Cancel", None))
    # retranslateUi

        self.saveStudent_btn.clicked.connect(self.add_student)
        self.cancel_btn.clicked.connect(self.close)
        
    
    def create_connection(self):
        host_name = "localhost"
        user_name = "root"
        mypassword = ""
        database_name = "my_school"
        
        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = mypassword,
        )
        cursor = self.mydb.cursor()
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = mypassword,
            database = database_name 
        )
        
        return self.mydb

    #yeni student insert
    
    def insert_new_student(self):
        try:
            
            connection = self.create_connection()
            if connection is None:
                return
            
            cursor = connection.cursor()
            
            gender = self.gender_comboBox.currentText()
            student_id = self.generate_studentId(gender)
            
            birthday = self.handleDateChange()
            
            birth_date = self.dob_dateEdit.date()
            age = self.calculate_age(birth_date)
            
            self.new_student = [
                self.name_lineEdit.text(),
                student_id,
                self.gender_comboBox.currentText(),
                self.class_comboBox.currentText(),
                birthday,
                age,
                self.address_lineEdit.text(),
                self.phone_lineEdit.text(),
                self.email_lineEdit.text()
            ]
            
            insert_student_query = f""" INSERT INTO students_table (names, student_id, gender, class, birthday, age, address, phone_number, email) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            cursor.execute(insert_student_query, self.new_student)
            self.show_inserted_message()
            connection.commit()
            cursor.close()
            connection.close()
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    
    def generate_studentId(self,gender):
        cursor = self.create_connection().cursor()
        
        while True:
            if gender == "Male":
                id_start_value = '24' + '/U/M'
            else:
                id_start_value = '24' + '/U/F'
            
            random_value = self.generate_randomNumber()
            student_id = id_start_value + random_value
            
            #oluşturulan öğrenci id si tbloda varmı kontrol et 
            cursor.execute("SELECT student_id FROM students_table WHERE student_id = %s", (student_id,))
            existing_id = cursor.fetchone()
            
            if not existing_id:
                return student_id
            
    
    def generate_randomNumber(self):
        
        number = randint(1,1000)
        random_number = f"{number:04d}"
        
        return random_number
    
    
    def handleDateChange(self):
        select_date = self.dob_dateEdit.date()
        self.date_string = select_date.toString(Qt.ISODate)
        
        return self.date_string
    
    def calculate_age(self,birth_date):
        current_date = datetime.now().date()
        
        birth_datetime = datetime(birth_date.year(),birth_date.month(),birth_date.day()).date()
        
        age = current_date.year - birth_datetime.year
        
        if(current_date.month,current_date.day) < (birth_datetime.month, birth_datetime.day):
            age -= 1
        
        return age
    
    def show_inserted_message(self):
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.name_lineEdit.text() + " İnserted into the database")
        msg_box.exec()
    
    def add_student(self):
        self.insert_new_student()
        self.accept()
    