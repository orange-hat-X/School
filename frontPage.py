from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow,QMenu, QWidget,QPushButton,QTableWidgetItem,QHBoxLayout,QVBoxLayout,QMessageBox
from PySide6.QtGui import QAction,QIcon
from ui_index import Ui_MainWindow

import mysql.connector
from UpdateStudentDialog import UpdateStuentsDialog

class MySideBar(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        
        self.icon_only_widget_2.setHidden(True)
        self.students_dropdown_2.setHidden(True)
        self.finances_dropdown.setHidden(True)
        
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)
        
        self.instituiton_1.clicked.connect(self.switch_to_instution_page)
        self.institution_2.clicked.connect(self.switch_to_instution_page)
        
        self.student_info.clicked.connect(self.switch_to_studentInfo_page)
        self.student_payment.clicked.connect(self.switch_to_studentPayment_page)
        self.student_trans.clicked.connect(self.switch_to_studentTransactions_page)
       
        self.teachers_info.clicked.connect(self.switch_to_teacherInfo_page)
        self.teachers_payment.clicked.connect(self.switch_to_teacherSalaries_page)
        self.teachers_tranc.clicked.connect(self.switch_to_teacherTransactions_page)    
        
        
        self.budgets.clicked.connect(self.switch_to_budgetsInfo_page)
        self.expences.clicked.connect(self.switch_to_expensesInfo_page)
        self.business_overview.clicked.connect(self.switch_to_bussinessOverview_page)   
        
        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)
        
        self.students_1.clicked.connect(self.students_context_menu)
        self.teachers_1.clicked.connect(self.teachers_context_menu)
        self.finances_1.clicked.connect(self.finances_context_menu)
        
        #mysql server bağlanma 
        self.create_connection()
        
        #students tavble oluşturma
        self.create_student_table()
        
        self.load_students_info()
        self.select_class.currentIndexChanged.connect(self.reload_Studentstable_data)
        self.select_gender.currentIndexChanged.connect(self.reload_Studentstable_data)
        
        self.search_student.textChanged.connect(self.search_students)
        
        self.studentinfo_table.setColumnWidth(0,120)
        self.studentinfo_table.setColumnWidth(1,80)
        self.studentinfo_table.setColumnWidth(2,60)
        self.studentinfo_table.setColumnWidth(3,70)
        self.studentinfo_table.setColumnWidth(4,70)
        self.studentinfo_table.setColumnWidth(5,50)
        self.studentinfo_table.setColumnWidth(6,70)
        self.studentinfo_table.setColumnWidth(7,80)
        self.studentinfo_table.setColumnWidth(8,120)
        self.studentinfo_table.setColumnWidth(9,150)
        
        self.saveStudent_btn.clicked.connect(self.open_addStudent_dialog)
        
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_instution_page(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_studentInfo_page(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def switch_to_studentPayment_page(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def switch_to_studentTransactions_page(self):
        self.stackedWidget.setCurrentIndex(4)    
        
    def switch_to_teacherInfo_page(self):
        self.stackedWidget.setCurrentIndex(5)
    
    def switch_to_teacherSalaries_page(self):
        self.stackedWidget.setCurrentIndex(6)
        
    def switch_to_teacherTransactions_page(self):
        self.stackedWidget.setCurrentIndex(7)
    
    def switch_to_budgetsInfo_page(self):
        self.stackedWidget.setCurrentIndex(8)
    
    def switch_to_expensesInfo_page(self):
        self.stackedWidget.setCurrentIndex(9)
        
    def switch_to_bussinessOverview_page(self):
        self.stackedWidget.setCurrentIndex(10)
    
    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(11)
        
    def students_context_menu(self):
        self.show_custom_context_menu(self.students_1,["Student İnformation","Student Payments","Student Transactions"])
    
    def teachers_context_menu(self):
        self.show_custom_context_menu(self.teachers_1,["Teacher İnformation","Teacher Salaries","Teacher Transactions"])
        
    def finances_context_menu(self):
        self.show_custom_context_menu(self.finances_1,["Budgets","Expenses","Business Overview"])
    
    def show_custom_context_menu(self, button, menu_items):
        
        menu = QMenu(self)
        menu.setStyleSheet("""
                           QMENU{
                               background-color: black;
                               color: white;
                           }
                           
                           QMenu:selected{
                               background-color: white;
                               color: #12B298
                           }
            
        """)
    
        for item_text in menu_items:
            action=QAction(item_text,self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)
            
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()
    
    def handle_menu_item_click(self):
        text = self.sender().text()
        
        if text == "Student İnformation":
            self.switch_to_studentInfo_page()
        elif text == "Student Payments":
            self.switch_to_studentPayment_page()
        elif text == "Student Transactions":
            self.switch_to_studentTransactions_page()
        elif text == "Teacher İnformation":
            self.switch_to_teacherInfo_page()
        elif text == "Teacher Salaries":
            self.switch_to_teacherSalaries_page()
        elif text == "Teacher Transactions":
            self.switch_to_teacherTransactions_page()
        elif text == "Budgets":
            self.switch_to_budgetsInfo_page()
        elif text == "Expenses":
            self.switch_to_expensesInfo_page()
        elif text == "Business Overview":
            self.switch_to_bussinessOverview_page()
        
        
        
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
    
    # student tablo oluşturma
    def create_student_table(self):
        cursor = self.create_connection().cursor()
        
        create_students_table_query = f"""
            CREATE TABLE IF NOT EXISTS students_table(
                names TEXT,
                student_id VARCHAR(15) PRIMARY KEY,
                gender TEXT,
                class TEXT,
                birthday TEXT,
                age INT,
                address TEXT,
                phone_number VARCHAR(15),
                email VARCHAR(15)
            )"""
        cursor.execute(create_students_table_query)
        
        self.mydb.commit()
        self.mydb.close()
    
    def open_addStudent_dialog(self):
        from StudentDialog import Ui_StuentsDialog
        
        addStudent_dialog = Ui_StuentsDialog(self)
        
        result = addStudent_dialog.exec()
        
        if result == Ui_StuentsDialog.Accepted:
            self.reload_Studentstable_data()
        
    def reload_Studentstable_data(self):
        self.load_students_info()
    
    def load_students_info(self):
        #clear existing data in table
        self.studentinfo_table.setRowCount(0)

        selected_class = self.select_class.currentText()
        selected_gender = self.select_gender.currentText()
        
        data = self.get_data_from_table(selected_class, selected_gender)
        
        for row_index, row_data in enumerate(data):
            self.studentinfo_table.insertRow(row_index)
            for col_index,cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.studentinfo_table.setItem(row_index,col_index, item)
                
                double_button_widget = DoubleButtonWidgetStudents(row_index,row_data,self)
                
                self.studentinfo_table.setCellWidget(row_index, 9, double_button_widget)
                self.studentinfo_table.setRowHeight(row_index, 50)

    
    def get_data_from_table(self, class_filter, gender_filter):
        cursor = self.create_connection().cursor()
        
        query = f""" SELECT names, student_id, gender, class, birthday, age, address, phone_number, email FROM students_table WHERE
                ('{class_filter}' = 'SELECT CLASS' OR class = '{class_filter}') AND
                ('{gender_filter}' = 'SELECT GENDER' OR gender = '{gender_filter}')"""
        
        cursor.execute(query)
        data = cursor.fetchall()
        
        return data 
    
    def search_students(self):
        self.studentinfo_table.setRowCount(0)
        
        search_query = self.search_student.text()
        
        cursor = self.create_connection().cursor()
        
        sql_query = f""" SELECT names, student_id, gender, class, birthday, age, address, phone_number, email FROM students_table WHERE
                names LIKE '& {search_query}'"""
                
        cursor.execute(sql_query)
        results = cursor.fetchall()
        
        for row_index, row_data in enumerate(results):
            self.studentinfo_table.insertRow(row_index)
            for col_index,cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.studentinfo_table.setItem(row_index,col_index, item)
                
                double_button_widget = DoubleButtonWidgetStudents(row_index,row_data,self)
                
                self.studentinfo_table.setCellWidget(row_index, 9, double_button_widget)
                self.studentinfo_table.setRowHeight(row_index, 50)
        
    #DoubleButton
    
class DoubleButtonWidgetStudents(QWidget):
    def __init__(self, row_index, row_data, sideBar):
        super().__init__()
        
        self.row_index = row_index
        self.row_data = row_data
        self.sidebar = sideBar
        
        self.student_name = self.row_data[0]
        self.student_id = self.row_data[1]
        
        layout = QHBoxLayout(self)
        
        self.edit_button = QPushButton("", self)
        self.edit_button.setStyleSheet("background-color:blue")
        self.edit_button.setFixedSize(61,31)    
        self.edit_button.clicked.connect(self.edit_clicked)
        
        
        self.delete_button = QPushButton("", self)
        self.delete_button.setStyleSheet("background-color:red")
        self.delete_button.setFixedSize(61,31)
        self.delete_button.clicked.connect(self.delete_clicked)  
        
        icon = QIcon(":/icons/edit.png")
        self.edit_button.setIcon(icon)
            
        icon2 = QIcon(":/icons/delete.png")
        self.delete_button.setIcon(icon2)
            
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

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
    
    def edit_clicked(self):
        self.update_dialog = UpdateStuentsDialog(self.row_index, self.row_data)
        
        self.update_dialog.data_updated.connect(self.sidebar.reload_Studentstable_data)

        self.update_dialog.exec()
    
    def delete_clicked(self):
        cursor = self.create_connection().cursor()
        
        message = QMessageBox.question(
            self, 'Confirmation',
            'Are you sure you want to delete' + self.student_name + '?', 
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if message == QMessageBox.StandardButton.Yes:
            delete_query = "DELETE FROM students_table WHERE student_id=%s"
            cursor.execute(delete_query,(self.student_id,))
            self.mydb.commit()
            self.mydb.close()
            
            self.sidebar.reload_Studentstable_data()