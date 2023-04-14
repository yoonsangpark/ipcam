import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5 import QtCore

from  ooPlayer import ooPlayer

class Ui_Form(object):
    def setupUi(self, Form):
       
        # Form 
        Form.setObjectName("Jupiter")
        Form.resize(1280, 800)
        self.frame = QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 640, 480))
        self.frame.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        self.player = ooPlayer("--network-caching=0")
        self.player.set_window(self.frame.winId())
        
	# Play
        self.pushButton_area_show = QPushButton(Form)
        self.pushButton_area_show.setText("Play")
        self.pushButton_area_show.setGeometry(QtCore.QRect(660, 10 , 100, 30))
        self.pushButton_area_show.clicked.connect(self.play)

	# Stop
        self.pushButton_area_show = QPushButton(Form)
        self.pushButton_area_show.setText("Stop")
        self.pushButton_area_show.setGeometry(QtCore.QRect(660, 50, 100, 30))
        self.pushButton_area_show.clicked.connect(self.stop)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def play(self):
        self.player.play("rtsp://192.168.10.104:8554/test")

    def stop(self):
        self.player.stop()


class App(QWidget,Ui_Form):
    def __init__(self):
        super(App,self).__init__()
        self.setupUi(self)

if "__main__" == __name__:
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
