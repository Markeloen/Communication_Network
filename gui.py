import os
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QMessageBox,
    QHBoxLayout,
    QLineEdit,
    QWidget,
    QComboBox,

)
from PyQt5.QtCore import Qt
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QIcon,QStandardItem,QColor
from main import *
from time import sleep
from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QTextStream
import breeze_resources


Form = uic.loadUiType(os.path.join(os.getcwd(), "gui_window.ui"))[0]

number_of_values = 3
value_names = ['population', 'modulation', 'aka']
colors = [(255,231,2,'yellow') , (247,109,2,'orange' ), (184,81,1,"dark_orange"), (30,189,24,"green"),\
    (134,246,64,"light_green"), (92,142,3,"dark_green"), (24,43,189,"blue"),\
    (3,121,215,"light_blue"), (15,0,164,"dark_blue"), (168,88,251,"light_purple"),\
        (141,39,247,"purple"), (116,5,56,"dark_red"), (255,12,12,"red"), (0,0,0,"black"),(0,0,0,"white"),\
            (141,138,138,"gray"), (101,67,33,"brown")]

class IntroWindow(QMainWindow, Form):
    def __init__(self):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QIcon("logo.png"))
        self.headers = fetch_headers("data.xlsx")
        for value in self.headers:
            self.comboBox.addItem(value)
        
            




        self.apply_btn.clicked.connect(self.apply)
        self.insert_btn.clicked.connect(self.insert)
            
    
    def apply(self):
        self.froms = []
        self.tos = []
        self.colors = []
        self.num_intervals = self.editor2.text()
        self.range = self.editor1.text()
        self.current_value = self.comboBox.currentText()
        for _ in range(int(self.num_intervals)):
            hbox = QHBoxLayout()
            mylabel_1 = QLabel()
            mylabel_1.setText("From:")
            myeditor_1 = QLineEdit()
            self.froms.append(myeditor_1)

            hbox.addWidget(mylabel_1)
            hbox.addWidget(myeditor_1)


            mylabel_2 = QLabel()
            mylabel_2.setText("to:")
            myeditor_2 = QLineEdit()
            self.tos.append(myeditor_2)

            hbox.addWidget(mylabel_2)
            hbox.addWidget(myeditor_2)



            mylabel_3 = QLabel()
            mylabel_3.setText("Color:")
            color_combobox = QComboBox()
            model = color_combobox.model()
            for a,b,c,color in colors:
                entry = QStandardItem(color)
                entry.setForeground(QColor(a,b,c))
                # color_combobox.addItem(color)
                model.appendRow(entry)
            self.colors.append(color_combobox)

            hbox.addWidget(mylabel_3)
            hbox.addWidget(color_combobox)

            self.v_lay.addLayout(hbox)



    def insert(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        from_list = []
        for i in self.froms:
            from_list.append(int(i.text()))
        to_list = []
        for i in self.tos:
            to_list.append(int(i.text()))
        color_list = []
        for i in self.colors:
            color_list.append(i.currentText())

        condition_list = list(zip(from_list, to_list, color_list))
        rng = float(self.editor1.text())
        header = self.comboBox.currentText()
        calculate(rng, "data.xlsx", condition_list, header)
        QApplication.restoreOverrideCursor()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"File : {header}.kml is created!")
        msg.exec_()
        QApplication.quit()

        





    


app = QApplication(sys.argv)


 # set stylesheet
file = QFile(":/dark.qss")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
app.setStyleSheet(stream.readAll())
w = IntroWindow()
w.show()
sys.exit(app.exec_())