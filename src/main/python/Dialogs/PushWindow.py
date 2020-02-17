from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class PushWindow(QMainWindow):
    def __init__(self, bar_length):
        super().__init__()
        self.setWindowTitle('Pushing Changes')
        self.setFixedSize(300, 100)
        mainwidget = QWidget()
        self.setCentralWidget(mainwidget)
        mainlayout = QVBoxLayout()
        pushlabellayout = QHBoxLayout()
        pushbuttlayout = QHBoxLayout()

        pushlabel = QLabel('You are attempting to merge changes to the database, master<-host')

        pushlabellayout.addStretch()
        pushlabellayout.addWidget(pushlabel)
        pushlabellayout.addStretch()

        acceptbutt = QPushButton('Accept')
        cancelbutt = QPushButton('Cancel')
        cancelbutt.clicked.connect(self.on_cancel_button_clicked)

        pushbuttlayout.addStretch()
        pushbuttlayout.addWidget(acceptbutt)
        pushbuttlayout.addStretch()
        pushbuttlayout.addWidget(cancelbutt)
        pushbuttlayout.addStretch()
        
        mainlayout.addLayout(pushlabellayout)
        mainlayout.addLayout(pushbuttlayout)
        mainwidget.setLayout(mainlayout)

    def on_cancel_button_clicked(self):
        self.hide()