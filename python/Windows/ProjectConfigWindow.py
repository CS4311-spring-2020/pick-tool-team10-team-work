from .ValidationIngestionWindow import ValidationIngestionWindow
from Dialogs.DirDialog import DirDialog
from Dialogs.CalendarDialog import CalendarDialog
from os import path
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStyle

class ProjectConfigWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.completed = 0
        self.setWindowTitle('Project Configuration')
        self.setFixedSize(550, 340)
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

        eventnamelabel = QLabel('Project Name:')
        self.eventnameledit = QLineEdit('Project name goes here.')

        eventnamelayout.addWidget(eventnamelabel)
        eventnamelayout.addWidget(self.eventnameledit)

        eventdesclabel = QLabel('Project Description:')
        self.eventdescledit = QLineEdit('Project description goes here.')

        eventdesclayout.addWidget(eventdesclabel)
        eventdesclayout.addWidget(self.eventdescledit)

        rootpathlabel = QLabel('Root Path:')
        self.rootpathledit = QLineEdit('Root path goes here.')
        rootpathbutt = QPushButton()
        rootpathbutt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirOpenIcon')))
        rootpathbutt.clicked.connect(self.on_rootdir_button_clicked)

        rootpathlayout.addWidget(rootpathlabel)
        rootpathlayout.addWidget(self.rootpathledit)
        rootpathlayout.addWidget(rootpathbutt)

        path1label = QLabel('Name of folder inside root path:')
        self.path1ledit = QLineEdit('Directory path of folder 1 goes here.')
        path1butt = QPushButton()
        path1butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirOpenIcon')))
        path1butt.clicked.connect(self.on_path1dir_button_clicked)

        path1layout.addWidget(path1label)
        path1layout.addWidget(self.path1ledit)
        path1layout.addWidget(path1butt)

        path2label = QLabel('Name of folder inside root path:')
        self.path2ledit = QLineEdit('Directory path of folder 2 goes here.')
        path2butt = QPushButton()
        path2butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirOpenIcon')))
        path2butt.clicked.connect(self.on_path2dir_button_clicked)

        path2layout.addWidget(path2label)
        path2layout.addWidget(self.path2ledit)
        path2layout.addWidget(path2butt)

        path3label = QLabel('Name of folder inside root path:')
        self.path3ledit = QLineEdit('Directory path of folder 3 goes here.')
        path3butt = QPushButton()
        path3butt.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DirOpenIcon')))
        path3butt.clicked.connect(self.on_path3dir_button_clicked)

        path3layout.addWidget(path3label)
        path3layout.addWidget(self.path3ledit)
        path3layout.addWidget(path3butt)

        eventdatelabel = QLabel('Event Date Range')

        datetitlelayout.addStretch()
        datetitlelayout.addWidget(eventdatelabel)
        datetitlelayout.addStretch()

        startdatebutt = QPushButton('Select a start date.')
        startdatebutt.clicked.connect(self.on_startdate_button_clicked)
        self.selectstartdatelabel = QLabel('No Start Date Selected')

        startdatelayout.addStretch()
        startdatelayout.addWidget(startdatebutt)
        startdatelayout.addStretch()

        starttimelayout.addStretch()
        starttimelayout.addWidget(self.selectstartdatelabel)
        starttimelayout.addStretch()

        startcontainerlayout.addLayout(startdatelayout)
        startcontainerlayout.addLayout(starttimelayout)

        self.enddatebutt = QPushButton('Select a end date.')
        self.enddatebutt.clicked.connect(self.on_enddate_button_clicked)
        self.selectenddatelabel = QLabel('No End Date Selected')
        self.enddatebutt.setEnabled(False)

        enddatelayout.addStretch()
        enddatelayout.addWidget(self.enddatebutt)
        enddatelayout.addStretch()

        endtimelayout.addStretch()
        endtimelayout.addWidget(self.selectenddatelabel)
        endtimelayout.addStretch()

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

    def writedata(self, location, dir_chosen):
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "../Data", "ProjectConfigData.txt"))
        with open(filepath, 'r') as file:
            # read a list of lines into data
            data = file.readlines()

        if location == 0:
            data[0] = dir_chosen + '\n'
            #print("root path: " + data[0])
        elif location == 1:
            data[1] = dir_chosen + '\n'
            #print("dir1 path: " + data[1])
        elif location == 2:
            data[2] = dir_chosen + '\n'
            #print("dir2 path: " + data[2])
        elif location == 3:
            data[3] = dir_chosen + '\n'
            #print("dir3 path: " + data[3])

        # and write everything back
        with open(filepath, 'w') as file:
            file.writelines( data )

    def on_rootdir_button_clicked(self):
        dir_chosen = DirDialog().dir_dialog('Choose the root path:')
        self.rootpathledit.setText(dir_chosen)
        self.writedata(0, dir_chosen)

    def on_path1dir_button_clicked(self):
        dir_chosen = DirDialog().dir_dialog('Choose the path of folder 1')
        self.path1ledit.setText(dir_chosen)
        self.writedata(1, dir_chosen)

    def on_path2dir_button_clicked(self):
        dir_chosen = DirDialog().dir_dialog('Choose the path of folder 2')
        self.path2ledit.setText(dir_chosen)
        self.writedata(2, dir_chosen)

    def on_path3dir_button_clicked(self):
        dir_chosen = DirDialog().dir_dialog('Choose the path of folder 3')
        self.path3ledit.setText(dir_chosen)
        self.writedata(3, dir_chosen)

    def on_startdate_button_clicked(self):
        self.start_date_calendar = True
        self.end_date_calendar = False
        calwindow = CalendarDialog(self)
        calwindow.exec_()
        datechosen =  calwindow.date_picked
        self.minimumdate = [calwindow.minimumdatelist[0], int(calwindow.minimumdatelist[1]), int(calwindow.minimumdatelist[2])] #[month, day, year]
        self.selectstartdatelabel.setText('Start Date Selected: ' + datechosen)

        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "../Data", "DateRange.txt"))
        with open(filepath, 'r') as file:
            data = file.readlines()
        if not data:
            data.append(str(self.minimumdate[2]) + '.' + str(self.minimumdate[0]) + '.' + str(self.minimumdate[1]) + '\n') #year.month.day
        else:
            data[0] = str(self.minimumdate[2]) + '.' + str(self.minimumdate[0]) + '.' + str(self.minimumdate[1]) + '\n' #year.month.day
        with open(filepath, 'w') as file:
            file.writelines( data )

        self.enddatebutt.setEnabled(True)
        
        """ #For debugging purposes
        print(self.minimumdate[0])
        print(self.minimumdate[1])
        print(self.minimumdate[2]) """
       

    def on_enddate_button_clicked(self):
        self.end_date_calendar = True
        self.start_date_calendar = False
        calwindow = CalendarDialog(self)
        calwindow.exec_()
        datechosen =  calwindow.date_picked
        self.maximumdate = [calwindow.maximumdatelist[0], int(calwindow.maximumdatelist[1]), int(calwindow.maximumdatelist[2])] #[month, day, year]
        self.selectenddatelabel.setText('End Date Selected: ' + datechosen)

        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "../Data", "DateRange.txt"))
        with open(filepath, 'r') as file:
            data = file.readlines()
        try:
            data[1] = str(self.maximumdate[2]) + '.' + str(self.maximumdate[0]) + '.' + str(self.maximumdate[1]) + '\n' #year.month.day
        except:
            data.append(str(self.maximumdate[2]) + '.' + str(self.maximumdate[0]) + '.' + str(self.maximumdate[1]) + '\n') #year.month.day
        with open(filepath, 'w') as file:
            file.writelines( data )

    def on_config_button_clicked(self):
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "../Data", "ProjectDescription.txt"))
        file_descriptor = open(filepath, 'w')
        file_descriptor.write(self.eventnameledit.text()+'\n'+self.eventdescledit.text()+'\n')
        file_descriptor.close()

        self.hide()
        self.window = ValidationIngestionWindow()
        self.window.show()



        