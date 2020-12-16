# ai_interview_gui.py

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
from randompkg.operation import calc


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        widget = MyWidget()
        self.setCentralWidget(widget)

        self.setWindowTitle('AI 면접 프로그램')
        self.setGeometry(300,300,400,300)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '종료', 'AI 면접 프로그램을 종료합니까?',
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

        btn_start = QPushButton('Start', self)
        btn_start.clicked.connect(self.refresh)

        vbox.addWidget(btn_start)

    def refresh(self):
        vbox = QVBoxLayout()

        btn_refresh = QPushButton('refresh', self)
        btn_refresh.clicked.connect(self.refresh)

        vbox.addWidget(btn_refresh)


        '''self.num_list = calc()

        lbl_list = []
        for i in range(len(self.num_list)):
            lbl_list.append(QLabel())
            lbl_list[i].setText(str(self.num_list[i]))
            
            vbox.addWidget(lbl_list[i])'''



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())