# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateStudentDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget,QMessageBox)

import mysql.connector
from random import randint
from datetime import datetime

class UpdateStuentsDialog(QDialog):
    
    data_updated = Signal()
    
    def __init__(self, row_index, row_data):
        super().__init__()
        
        self.row_index = row_index
        self.row_data = row_data
        
        self.student_info = self.select_student()[0]
        
        print(self.student_info)
        
        self.student_name_info = self.student_info[0]
        self.student_id_info = self.student_info[1]
        self.student_gender_info = self.student_info[2]
        self.student_class_info = self.student_info[3]
        self.student_birthday_info = self.student_info[4]
        self.student_age_info = self.student_info[5]
        self.student_address_info = self.student_info[6]
        self.student_phone_info = self.student_info[7]
        self.student_email_info = self.student_info[8]

        
        
        
        
        
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
        self.label.setGeometry(QRect(20, 10, 391, 31))
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

        self.update_name_lineEdit = QLineEdit(self.layoutWidget)
        self.update_name_lineEdit.setObjectName(u"update_name_lineEdit")
        self.update_name_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout.addWidget(self.update_name_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.update_gender_comboBox = QComboBox(self.layoutWidget)
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.setObjectName(u"update_gender_comboBox")

        self.verticalLayout_5.addWidget(self.update_gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.update_class_comboBox = QComboBox(self.layoutWidget)
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.addItem("")
        self.update_class_comboBox.setObjectName(u"update_class_comboBox")

        self.verticalLayout_6.addWidget(self.update_class_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.update_dob_dateEdit = QDateEdit(self.layoutWidget)
        self.update_dob_dateEdit.setObjectName(u"update_dob_dateEdit")

        self.verticalLayout_7.addWidget(self.update_dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.update_address_lineEdit = QLineEdit(self.layoutWidget)
        self.update_address_lineEdit.setObjectName(u"update_address_lineEdit")
        self.update_address_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_2.addWidget(self.update_address_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.update_phone_lineEdit = QLineEdit(self.layoutWidget)
        self.update_phone_lineEdit.setObjectName(u"update_phone_lineEdit")
        self.update_phone_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.update_phone_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.update_email_lineEdit = QLineEdit(self.layoutWidget)
        self.update_email_lineEdit.setObjectName(u"update_email_lineEdit")
        self.update_email_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.update_email_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(250, 510, 281, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.updateStudent_btn = QPushButton(self.layoutWidget1)
        self.updateStudent_btn.setObjectName(u"updateStudent_btn")
        self.updateStudent_btn.setMinimumSize(QSize(0, 41))
        self.updateStudent_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.updateStudent_btn)

        self.update_cancel_btn = QPushButton(self.layoutWidget1)
        self.update_cancel_btn.setObjectName(u"update_cancel_btn")
        self.update_cancel_btn.setMinimumSize(QSize(0, 41))
        self.update_cancel_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color:white;\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	font-weight:bold;\n"
"	font-size:15px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.update_cancel_btn)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("UpdateStuentsDialog", u"Update Student Dialog", None))
        self.setWindowIcon(QIcon(":/icons/logo.png"))
        self.label.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Update Student \u0130nformation", None))
        self.label_2.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Select Gender", None))
        self.update_gender_comboBox.setItemText(0, QCoreApplication.translate("UpdateStuentsDialog", u"Male", None))
        self.update_gender_comboBox.setItemText(1, QCoreApplication.translate("UpdateStuentsDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Select Class", None))
        self.update_class_comboBox.setItemText(0, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 1", None))
        self.update_class_comboBox.setItemText(1, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 2", None))
        self.update_class_comboBox.setItemText(2, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 3", None))
        self.update_class_comboBox.setItemText(3, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 4", None))
        self.update_class_comboBox.setItemText(4, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 5", None))
        self.update_class_comboBox.setItemText(5, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 6", None))
        self.update_class_comboBox.setItemText(6, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 7", None))
        self.update_class_comboBox.setItemText(7, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 8", None))
        self.update_class_comboBox.setItemText(8, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 9", None))
        self.update_class_comboBox.setItemText(9, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 10", None))
        self.update_class_comboBox.setItemText(10, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 11", None))
        self.update_class_comboBox.setItemText(11, QCoreApplication.translate("UpdateStuentsDialog", u"Grade 12", None))

        self.label_8.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Date Of Birth", None))
        self.label_3.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Address", None))
        self.label_4.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Phone Number", None))
        self.label_5.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Email", None))
        self.updateStudent_btn.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Update Student", None))
        self.update_cancel_btn.setText(QCoreApplication.translate("UpdateStuentsDialog", u"Cancel", None))
    # retranslateUi

    #for the date from mysql database

        date_object = QDate.fromString(self.student_birthday_info,"yyyy-MM-dd")
        
        self.update_name_lineEdit.setText(str(self.student_name_info))
        self.update_gender_comboBox.setCurrentText(str(self.student_gender_info))
        self.update_class_comboBox.setCurrentText(str(self.student_class_info))
        self.update_dob_dateEdit.setDate(date_object)
        self.update_address_lineEdit.setText(str(self.student_address_info))
        self.update_phone_lineEdit.setText(str(self.student_phone_info))
        self.update_email_lineEdit.setText(str(self.student_email_info))
        
        #initial gender
        
        self.lastIndex = self.update_gender_comboBox.currentText()      
        
        self.updateStudent_btn.clicked.connect(self.update_Data)  

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

    def select_student(self):
        
        self.cursor = self.create_connection().cursor()
        
        self.student_name = self.row_data[0]
        self.student_id = self.row_data[1]
        
        params = [
            self.student_name,
            self.student_id
        ]
        
        select_query = f"SELECT * FROM students_table WHERE names=%s AND student_id=%s"
        
        self.cursor.execute(select_query, params)

        records = self.cursor.fetchall()
        
        self.mydb.commit()
        self.mydb.close
        return records
        
    def update_Data(self):
        
        try:
            connection = self.create_connection()
            
            if connection is None:
                return
            
            cursor = connection.cursor()
            
            birth_date = self.update_dob_dateEdit.date()
            
            birthday = self.handleDateChange()
            age = self.calculate_age(birth_date)
            
            #check if the gender
            current_Student_id = self.on_gender_changed(self.update_gender_comboBox.currentText())
            
            params = (
                self.update_name_lineEdit.text(),
                current_Student_id,
                self.update_gender_comboBox.currentText(),
                self.update_class_comboBox.currentText(),
                birthday,
                age,
                self.update_address_lineEdit.text(),
                self.update_phone_lineEdit.text(),
                self.update_email_lineEdit.text(),
                self.student_id_info
            )
            
            print(params)
            
            update_query = f"UPDATE students_table SET names=%s, student_id=%s, gender=%s, class=%s, birthday=%s, age=%s, address=%s, phone_number=%s, email=%s WHERE student_id=%s"
            
            cursor.execute(update_query, params)
            connection.commit()
            self.show_updated_message()
            cursor.close()
            connection.close()
            self.close()
            
            self.data_updated.emit()
        
        except mysql.connector.Error as err:
            
            print(f"Error: {err}")
            
            
    def handleDateChange(self):
        select_date = self.update_dob_dateEdit.date()
        self.date_string = select_date.toString(Qt.ISODate)
        
        return self.date_string
    
    def calculate_age(self,birth_date):
        current_date = datetime.now().date()
        
        birth_datetime = datetime(birth_date.year(),birth_date.month(),birth_date.day()).date()
        
        age = current_date.year - birth_datetime.year
        
        if(current_date.month,current_date.day) < (birth_datetime.month, birth_datetime.day):
            age -= 1
        
        return age

    def on_gender_changed(self, index):
        if index != self.lastIndex:
            
            gender_item = self.update_gender_comboBox.currentIndex()
            new_student_id = self.generate_studentId(gender_item)
            
            return new_student_id
        
        else:
            return self.student_id_info
            
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
    
    def show_updated_message(self):
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.student_name_info + " information updated successfully")
        msg_box.exec() 
        
        
        
        
        
        
        
        
        
        
        
        
        