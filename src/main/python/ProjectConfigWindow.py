from ValidationIngestionWindow import ValidationIngestionWindow

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class ProjectConfigWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.completed = 0
        self.setWindowTitle('Project Configuration')
        self.setFixedSize(500, 340)
        mainwidget = QWidget()
        self.setCentralWidget(mainwidget)
        mainlayout = QVBoxLayout()
        eventnamelayout = QHBoxLayout()
        eventdesclayout = QHBoxLayout()
        rootpathlayout = QHBoxLayout()
        path1layout = QHBoxLayout()
        path2layout = QHBoxLayout()
        path3layout = QHBoxLayout()
        datetitlelayout = QHBoxLayout()
        datecontainerlayout = QHBoxLayout()
        startcontainerlayout = QVBoxLayout()
        startdatelayout = QHBoxLayout()
        starttimelayout = QHBoxLayout()
        endcontainerlayout = QVBoxLayout()
        enddatelayout = QHBoxLayout()
        endtimelayout = QHBoxLayout()
        configcompletelayout = QHBoxLayout()

        eventnamelabel = QLabel('Event Name:')
        eventnameledit = QLineEdit('Event name goes here.')

        eventnamelayout.addWidget(eventnamelabel)
        eventnamelayout.addWidget(eventnameledit)

        eventdesclabel = QLabel('Event Description:')
        eventdescledit = QLineEdit('Event description goes here.')

        eventdesclayout.addWidget(eventdesclabel)
        eventdesclayout.addWidget(eventdescledit)

        rootpathlabel = QLabel('Root Path:')
        rootpathledit = QLineEdit('Root path goes here.')

        rootpathlayout.addWidget(rootpathlabel)
        rootpathlayout.addWidget(rootpathledit)

        path1label = QLabel('Name of folder inside root path:')
        path1ledit = QLineEdit('Name of folder 1 goes here.')

        path1layout.addWidget(path1label)
        path1layout.addWidget(path1ledit)

        path2label = QLabel('Name of folder inside root path:')
        path2ledit = QLineEdit('Name of folder 2 goes here.')

        path2layout.addWidget(path2label)
        path2layout.addWidget(path2ledit)

        path3label = QLabel('Name of folder inside root path:')
        path3ledit = QLineEdit('Name of folder 3 goes here.')

        path3layout.addWidget(path3label)
        path3layout.addWidget(path3ledit)

        eventdatelabel = QLabel('Event Date Range')

        datetitlelayout.addStretch()
        datetitlelayout.addWidget(eventdatelabel)
        datetitlelayout.addStretch()

        startdatelabel = QLabel('Start Date: ')
        startdateledit = QLineEdit()

        startdatelayout.addWidget(startdatelabel)
        startdatelayout.addWidget(startdateledit)

        starttimelabel = QLabel('Start Time: ')
        starttimeledit = QLineEdit()

        starttimelayout.addWidget(starttimelabel)
        starttimelayout.addWidget(starttimeledit)

        startcontainerlayout.addLayout(startdatelayout)
        startcontainerlayout.addLayout(starttimelayout)

        enddatelabel = QLabel('End Date: ')
        enddateledit = QLineEdit()

        enddatelayout.addWidget(enddatelabel)
        enddatelayout.addWidget(enddateledit)

        endtimelabel = QLabel('End Time: ')
        endtimeledit = QLineEdit()

        endtimelayout.addWidget(endtimelabel)
        endtimelayout.addWidget(endtimeledit)

        endcontainerlayout.addLayout(enddatelayout)
        endcontainerlayout.addLayout(endtimelayout)

        datecontainerlayout.addLayout(startcontainerlayout)
        datecontainerlayout.addLayout(endcontainerlayout)

        configcompletebutt = QPushButton('Configuration Complete')
        configcompletebutt.clicked.connect(self.on_config_button_clicked)

        configcompletelayout.addStretch()
        configcompletelayout.addWidget(configcompletebutt)
        configcompletelayout.addStretch()

        mainlayout.addLayout(eventnamelayout)
        mainlayout.addLayout(eventdesclayout)
        mainlayout.addLayout(rootpathlayout)
        mainlayout.addLayout(path1layout)
        mainlayout.addLayout(path2layout)
        mainlayout.addLayout(path3layout)
        mainlayout.addLayout(datetitlelayout)
        mainlayout.addLayout(datecontainerlayout)
        mainlayout.addLayout(configcompletelayout)
        mainlayout.addStretch()
        mainwidget.setLayout(mainlayout)

    def on_config_button_clicked(self):
        self.hide()
        self.window = ValidationIngestionWindow()
        self.window.show()



        