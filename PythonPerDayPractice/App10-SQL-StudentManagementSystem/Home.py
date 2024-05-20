from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, \
    QWidget, QGridLayout, QLineEdit, QPushButton, QMainWindow, \
    QTableWidget
from PyQt6.QtGui import QAction
import sys
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        table = QTableWidget()


app = QApplication(sys.argv)
st_management = MainWindow()
st_management.show()
sys.exit(app.exec())



