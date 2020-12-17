# ai_interview_gui_opencv_qt

import numpy as np
import cv2
import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QMessageBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
# main.py에서 cam 영상을 처리한 ndarray 변수를 받아와서 qt에서 출력
# main.py에서 emotion 분류와 확률 변수를 받아오기 위한 import 필요


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        widget = MyWidget()
        self.setCentralWidget(widget)

        self.setWindowTitle('AI interview program')
        #self.setGeometry(300,300,400,300)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Do you want to quit AI interview?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        lbl_cam = QLabel()
        btn_start = QPushButton('Start AI interview', self)
        btn_stop = QPushButton('Pause AI interview', self)

        btn_start.clicked.connect(self.start_cam)
        btn_stop.clicked.connect(self.stop_cam)

        vbox.addWidget(lbl_cam)
        vbox.addWidget(btn_start)
        vbox.addWidget(btn_stop)

        self.setLayout(vbox)


    def start_cam(self):
        pass


    def stop_cam(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())