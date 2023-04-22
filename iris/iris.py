from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from Irisui import Ui_Irisui
import sys
import main

class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()
        

    def Task_Gui(self):
        main.TaskExe()

startFunctions = MainThread() 

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.Iris_ui = Ui_Irisui()
        
        self.Iris_ui.setupUi(self)

        self.Iris_ui.pushButton.clicked.connect(self.startFunc)

        self.Iris_ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.Iris_ui.movie_1 = QtGui.QMovie("F:/code/VS code/Advance Iris/Earth_Template.gif")
        self.Iris_ui.label.setMovie(self.Iris_ui.movie_1)
        self.Iris_ui.movie_1.start()

        self.Iris_ui.movies_2 = QtGui.QMovie("F:/code/VS code/Advance Iris/initializing.gif")
        self.Iris_ui.initiating.setMovie(self.Iris_ui.movies_2)
        self.Iris_ui.movies_2.start()

        self.Iris_ui.movies_3 = QtGui.QMovie("F:/code/VS code/Advance Iris/voice recog.gif")
        self.Iris_ui.voicerecog.setMovie(self.Iris_ui.movies_3)
        self.Iris_ui.movies_3.start()

        self.Iris_ui.movies_4 = QtGui.QMovie("F:/code/VS code/Advance Iris/code bg.gif")
        self.Iris_ui.code.setMovie(self.Iris_ui.movies_4)
        self.Iris_ui.movies_4.start()

        self.Iris_ui.movies_5 = QtGui.QMovie("F:/code/VS code/Advance Iris/message.gif")
        self.Iris_ui.message.setMovie(self.Iris_ui.movies_5)
        self.Iris_ui.movies_5.start()

        startFunctions.start()

   #     timer = QTimer(self)

   #     timer.timeout.connect(self.showtime)

   #     timer.start(1000)

   #     startFunctions.start()

  #  def showtime(self):
        
     #   current_time = QTime.currentTime()

    #    label_time = current_time.toString("hh:mm:ss")

 #       labbel = " Time :  " + label_time 

 #       self.Iris_ui.Time.setText(labbel)

Gui_App = QApplication(sys.argv)

Gui_Iris = Gui_Start()

Gui_Iris.show()

exit(Gui_App.exec_())