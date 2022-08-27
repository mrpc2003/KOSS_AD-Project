import sys
from turtle import color
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QColor, QPainter
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar





class Button(QWidget):
    def __init__(self):
        super().__init__()
        self.UIinit()

        
    def UIinit(self):
    
        
        label1 = QLabel("OFF", self)
        label1.move(330, 100)
        font1 = label1.font()
        font1.setPointSize(50)
        font1.setFamily('Bodoni MT Black')
        font1.setBold(True)
        label1.setFont(font1)
        
        label2 = QLabel("택배 아저씨 버튼 눌러 주세요~", self)
        label2.move(3, 5)
        font2 = label2.font()
        font2.setPointSize(15)
        label2.setFont(font2)
       
        
        btn1 = QPushButton('택배/배달', self)
        btn2 = QPushButton('도둑', self)
        btn3 = QPushButton('풀기', self)
        btn1.move(50, 300)
        btn2.move(300, 300)
        btn3.move(550, 300)
        btn1.setFixedSize(210, 100)
        btn2.setFixedSize(210, 100)
        btn3.setFixedSize(210, 100)
        
        btn1.setFont(QtGui.QFont("한컴 훈민정음 세로쓰기", 30))
        btn2.setFont(QtGui.QFont("한컴 훈민정음 세로쓰기", 30))
        btn3.setFont(QtGui.QFont("한컴 훈민정음 세로쓰기", 30))
        
        

        
        
        
        
        
        
        
        


        
        
        self.setGeometry(500, 300, 800, 700)
        self.setWindowTitle('Main Door')
        self.show()
   
   
   
        
        
app = QApplication(sys.argv)
ex = Button()
app.exec_()


