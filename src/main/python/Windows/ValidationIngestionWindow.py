from .mainwindow_nav import Ui_mainwindow_navigation
from Splunk.SplunkDataSearch import SplunkDataSearch
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
                            QHeaderView, QFrame, QTreeWidget, QTreeWidgetItem, QPlainTextEdit, QDialog)

import subprocess
import os

class ValidationIngestionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.completed = 0
        self.setWindowTitle('Validation and Ingestion Process')
        self.setFixedSize(1000, 800)
        mainwidget = QWidget()
        self.setCentralWidget(mainwidget)
        mainlayout = QVBoxLayout()
        cleansetitlelayout = QHBoxLayout()
        cleansecontainergrid = QGridLayout()
        cleansecontainergrid.setColumnStretch(1,4)
        cleansecontainerlayout = QVBoxLayout()
        cleanseinfolayout = QHBoxLayout()
        cleansebuttlayout = QHBoxLayout()
        cleansestatuslayout = QHBoxLayout()
        validationtitlelayout = QHBoxLayout()
        validationcontainergrid = QGridLayout()
        validationcontainergrid.setColumnStretch(1,4)
        validationcontainerlayout = QVBoxLayout()
        validationinfolayout = QHBoxLayout()
        validationbuttlayout = QHBoxLayout()
        validationstatuslayout = QHBoxLayout()
        logtitlelayout = QHBoxLayout()
        logcontainergrid = QGridLayout()
        ingestioncontainerlayout = QHBoxLayout()
        ingestiblecontainerlayout = QVBoxLayout()
        ingestibletitlelayout = QHBoxLayout()
        ingestibletreelayout = QHBoxLayout()
        noningestiblecontainerlayout = QVBoxLayout()
        noningestibletitlelayout = QHBoxLayout()
        noningestibletreelayout = QHBoxLayout()
        logentrycontainerlayout = QVBoxLayout()
        logentryinfolayout = QHBoxLayout()
        logentrynamelayout = QHBoxLayout()
        logentryteamlayout = QHBoxLayout()
        logentrytimelayout = QHBoxLayout()
        logentrypathlayout = QHBoxLayout()
        logentryboxlayout = QHBoxLayout()
        logentrybuttlayout = QHBoxLayout()
        preingestionlayout = QHBoxLayout()

        hline1 = QFrame()
        hline1.setFrameShape(QFrame.HLine)
        hline2 = QFrame()
        hline2.setFrameShape(QFrame.HLine)
        hline3 = QFrame()
        hline3.setFrameShape(QFrame.HLine)

        vline1 = QFrame()
        vline1.setFrameShape(QFrame.VLine)
        vline2 = QFrame()
        vline2.setFrameShape(QFrame.VLine)

        cleansetitlelabel = QLabel('Cleansing Overview')

        cleansetitlelayout.addStretch()
        cleansetitlelayout.addWidget(cleansetitlelabel)
        cleansetitlelayout.addStretch()

        cleanseinfolabel = QLabel('Cleanse Un-Cleansed Log Files')

        cleanseinfolayout.addStretch()
        cleanseinfolayout.addWidget(cleanseinfolabel)
        cleanseinfolayout.addStretch()

        cleansebutt = QPushButton('Cleanse')

        cleansebuttlayout.addStretch()
        cleansebuttlayout.addWidget(cleansebutt)
        cleansebuttlayout.addStretch()

        cleansestatuslabel = QLabel('Status: All log files are cleansed.')

        cleansestatuslayout.addStretch()
        cleansestatuslayout.addWidget(cleansestatuslabel)
        cleansestatuslayout.addStretch()

        cleansecontainerlayout.addStretch()
        cleansecontainerlayout.addLayout(cleanseinfolayout)
        cleansecontainerlayout.addLayout(cleansebuttlayout)
        cleansecontainerlayout.addLayout(cleansestatuslayout)
        cleansecontainerlayout.addStretch()

        self.cleansetable = QTableWidget()
        cleanseheaderlabels = ['Location/Name', 'Cleansed']
        self.create_table_cleanse(self.cleansetable, cleanseheaderlabels)

        cleansecontainergrid.addLayout(cleansecontainerlayout, 0, 0)
        cleansecontainergrid.addWidget(self.cleansetable, 0, 1)

        validationtitlelabel = QLabel('Validation Overview')

        validationtitlelayout.addStretch()
        validationtitlelayout.addWidget(validationtitlelabel)
        validationtitlelayout.addStretch()

        validationinfolabel = QLabel('Validate Un-Validated Log Files')

        validationinfolayout.addStretch()
        validationinfolayout.addWidget(validationinfolabel)
        validationinfolayout.addStretch()

        validatebutt = QPushButton('Validate')
        validatebutt.clicked.connect(self.on_validate_button_clicked)

        validationbuttlayout.addStretch()
        validationbuttlayout.addWidget(validatebutt)
        validationbuttlayout.addStretch()

        validatestatuslabel = QLabel('Status: All log files are validated.')

        validationstatuslayout.addStretch()
        validationstatuslayout.addWidget(validatestatuslabel)
        validationstatuslayout.addStretch()

        validationcontainerlayout.addStretch()
        validationcontainerlayout.addLayout(validationinfolayout)
        validationcontainerlayout.addLayout(validationbuttlayout)
        validationcontainerlayout.addLayout(validationstatuslayout)
        validationcontainerlayout.addStretch()

        self.validatetable = QTableWidget()
        validateheaderlabels = ['Location/Name', 'Validated']
        self.create_table_validate(self.validatetable, validateheaderlabels)

        validationcontainergrid.addLayout(validationcontainerlayout, 0, 0)
        validationcontainergrid.addWidget(self.validatetable, 0, 1)

        logtitlelabel = QLabel('Log Overview')

        logtitlelayout.addStretch()
        logtitlelayout.addWidget(logtitlelabel)
        logtitlelayout.addStretch()

        ingestibletitlelabel = QLabel('Ingestible Log Entries')

        ingestibletitlelayout.addStretch()
        ingestibletitlelayout.addWidget(ingestibletitlelabel)
        ingestibletitlelayout.addStretch()

        self.ingestibletree = QTreeWidget()
        data = ['Log Entry ####', 'Log Entry ####+1', 'Log Entry ####+2', 'Log Entry ####+3', 'Log Entry ####+4', 'Log Entry ####+5', 'Log Entry ####+6', 'Log Entry ####+7', 'Log Entry ####+8']
        self.create_treelist(self.ingestibletree, data)
        self.ingestibletree.itemSelectionChanged.connect(self.on_ingestitem_selected)

        ingestibletreelayout.addStretch()
        ingestibletreelayout.addWidget(self.ingestibletree)
        ingestibletreelayout.addStretch()

        ingestiblecontainerlayout.addLayout(ingestibletitlelayout)
        ingestiblecontainerlayout.addLayout(ingestibletreelayout)

        noningestibletitlelabel = QLabel('Non-Ingestible Log Entries')

        noningestibletitlelayout.addStretch()
        noningestibletitlelayout.addWidget(noningestibletitlelabel)
        noningestibletitlelayout.addStretch()

        self.noningestibletree = QTreeWidget()
        nondata = ['Log Entry ####+9', 'Log Entry ####+10', 'Log Entry ####+11', 'Log Entry ####+12', 'Log Entry ####+13', 'Log Entry ####+14', 'Log Entry ####+15', 'Log Entry ####+16', 'Log Entry ####+17']
        self.create_treelist(self.noningestibletree, nondata)
        self.noningestibletree.itemSelectionChanged.connect(self.on_noningestitem_selected)

        noningestibletreelayout.addStretch()
        noningestibletreelayout.addWidget(self.noningestibletree)
        noningestibletreelayout.addStretch()

        noningestiblecontainerlayout.addLayout(noningestibletitlelayout)
        noningestiblecontainerlayout.addLayout(noningestibletreelayout)

        ingestioncontainerlayout.addLayout(ingestiblecontainerlayout)
        ingestioncontainerlayout.addWidget(vline1)
        ingestioncontainerlayout.addLayout(noningestiblecontainerlayout)
        ingestioncontainerlayout.addWidget(vline2)

        logentryinfolabel = QLabel('Selected Log Entry Information')

        logentryinfolayout.addStretch()
        logentryinfolayout.addWidget(logentryinfolabel)
        logentryinfolayout.addStretch()

        self.logentrynamelabel = QLabel('Name: Log Entry ####')

        logentrynamelayout.addStretch()
        logentrynamelayout.addWidget(self.logentrynamelabel)
        logentrynamelayout.addStretch()

        logentryteamlabel = QLabel('Team: R|B|W')

        logentryteamlayout.addStretch()
        logentryteamlayout.addWidget(logentryteamlabel)
        logentryteamlayout.addStretch()

        logentrytimelabel = QLabel('Timestamp: Time of the Log Entry')

        logentrytimelayout.addStretch()
        logentrytimelayout.addWidget(logentrytimelabel)
        logentrytimelayout.addStretch()

        logentrypathlabel = QLabel('File Path: File path of file that created the Log Entry')

        logentrypathlayout.addStretch()
        logentrypathlayout.addWidget(logentrypathlabel)
        logentrypathlayout.addStretch()

        logentrydatalabel = QLabel('Data:    ')
        logentrydataptedit = QPlainTextEdit('Any data corresponding to this log entry will go here.')

        logentryboxlayout.addStretch()
        logentryboxlayout.addWidget(logentrydatalabel)
        logentryboxlayout.addWidget(logentrydataptedit)
        logentryboxlayout.addStretch()

        logentrydelbutt = QPushButton('Delete Log Entry')

        logentrybuttlayout.addStretch()
        logentrybuttlayout.addWidget(logentrydelbutt)
        logentrybuttlayout.addStretch()

        logentrycontainerlayout.addLayout(logentryinfolayout)
        logentrycontainerlayout.addLayout(logentrynamelayout)
        logentrycontainerlayout.addLayout(logentryteamlayout)
        logentrycontainerlayout.addLayout(logentrytimelayout)
        logentrycontainerlayout.addLayout(logentrypathlayout)
        logentrycontainerlayout.addLayout(logentryboxlayout)
        logentrycontainerlayout.addLayout(logentrybuttlayout)

        logcontainergrid.addLayout(ingestioncontainerlayout, 0, 0)
        logcontainergrid.addLayout(logentrycontainerlayout, 0, 1)

        nontoingestbutt = QPushButton('Move all Non-Ingestible Log Entries into Ingestible')
        discardbutt = QPushButton('Discard All Non-Ingestible Log Entries')
        ingestbutt = QPushButton('Ingest Log Entries and Continue to Navigator')
        ingestbutt.clicked.connect(self.on_ingest_button_clicked)

        preingestionlayout.addStretch()
        preingestionlayout.addWidget(nontoingestbutt)
        preingestionlayout.addStretch()
        preingestionlayout.addWidget(discardbutt)
        preingestionlayout.addStretch()
        preingestionlayout.addWidget(ingestbutt)
        preingestionlayout.addStretch()

        mainlayout.addLayout(cleansetitlelayout)
        mainlayout.addLayout(cleansecontainergrid)
        mainlayout.addWidget(hline1)
        mainlayout.addLayout(validationtitlelayout)
        mainlayout.addLayout(validationcontainergrid)
        mainlayout.addWidget(hline2)
        mainlayout.addLayout(logtitlelayout)
        mainlayout.addLayout(logcontainergrid)
        mainlayout.addWidget(hline3)
        mainlayout.addLayout(preingestionlayout)
        mainwidget.setLayout(mainlayout)

    #Create a table widget and populating it with cleansed files
    def create_table_cleanse(self, tablewidget, headerlabels):
        filelist = []
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../Data/CleansedFiles", ""))
        
        #iterate through the files in the cleansed folder
        for r, d, f in os.walk(filepath):
            for file in f:
                filelist.append(os.path.join(r, file))

        tablewidget.setRowCount(len(filelist))
        tablewidget.setColumnCount(2)
        tablewidget.setHorizontalHeaderLabels(headerlabels)
        tablewidget.verticalHeader().setVisible(False)
        header = tablewidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        #Populate table
        for x in range(tablewidget.rowCount()):
            for y in range(tablewidget.columnCount()):
                if y == 0:
                    path = filelist[x]
                    item = QTableWidgetItem(path)
                    item.setTextAlignment(Qt.AlignCenter)
                    tablewidget.setItem(x,y, item)
                else:
                    item = QTableWidgetItem('yes')
                    item.setTextAlignment(Qt.AlignCenter)
                    tablewidget.setItem(x,y, item)

    #Create a table widget and populating it with validated files
    def create_table_validate(self, tablewidget, headerlabels):
        dirlist = []
        filelist = []
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../Data", "ProjectConfigData.txt"))
        
        #read a list of lines into data
        with open(filepath, 'r') as file:
            data = file.readlines()

        #remove the root dir for the project
        del data[0]

        #create list for directories
        for directory in data:
            dirlist.append(directory.rstrip())

        #iterate through the list of directories
        for directory in dirlist:
            for r, d, f in os.walk(directory):
                for file in f:
                    filelist.append(os.path.join(r, file))

        tablewidget.setRowCount(len(filelist))
        tablewidget.setColumnCount(2)
        tablewidget.setHorizontalHeaderLabels(headerlabels)
        tablewidget.verticalHeader().setVisible(False)
        header = tablewidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        #Populate table
        for x in range(tablewidget.rowCount()):
            for y in range(tablewidget.columnCount()):
                if y == 0:
                    path = filelist[x]
                    item = QTableWidgetItem(path)
                    item.setTextAlignment(Qt.AlignCenter)
                    tablewidget.setItem(x,y, item)
                else:
                    item = QTableWidgetItem('yes')
                    item.setTextAlignment(Qt.AlignCenter)
                    tablewidget.setItem(x,y, item)

    #Splunk method to upload to local splunk server
    def push_to_splunk(self, tablewidget):
        for row in range(tablewidget.rowCount()):
            twi0 = tablewidget.item(row,0)
            splunkcmd = subprocess.run(["/opt/splunk/bin/splunk", "add", "oneshot", twi0.text()])
            print("The exit code was: %d" % splunkcmd.returncode)
            print(twi0.text())
        test = SplunkDataSearch()

    #Creates a tree widget
    def create_treelist(self, treewidget, data):
        treewidget.setHeaderHidden(True)
        for x in data:
            list_item = QTreeWidgetItem([x])
            treewidget.addTopLevelItem(list_item)

    #Selection of item on ingestibletree widget
    def on_ingestitem_selected(self):
        getSelected = self.ingestibletree.selectedItems()
        getChildNode = None
        if getSelected:
            baseNode = getSelected[0]
            getChildNode = baseNode.text(0)
        self.ingestibletree.clearSelection()
        self.change_logentry_display(getChildNode)

    #Selection of item on noningestibletree widget
    def on_noningestitem_selected(self):
        getSelected = self.noningestibletree.selectedItems()
        getChildNode = None
        if getSelected:
            baseNode = getSelected[0]
            getChildNode = baseNode.text(0)
        self.noningestibletree.clearSelection()
        self.change_logentry_display(getChildNode)

    #Change log entry information
    def change_logentry_display(self, name):
        self.logentrynamelabel.setText(name)

    #On validate button click call splunk method
    def on_validate_button_clicked(self):
        self.push_to_splunk(self.validatetable)

    #Move on to the next window[Ui_mainwindow_navigation] on ingest button click
    def on_ingest_button_clicked(self):
        self.hide()
        self.window = Ui_mainwindow_navigation()
        self.window.show()
