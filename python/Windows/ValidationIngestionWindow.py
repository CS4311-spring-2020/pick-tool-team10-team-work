import pprint

from Database.databse_interface import DatabaseInterface
from Splunk.SplunkDataSearch import SplunkDataSearch
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
                            QHeaderView, QFrame, QTreeWidget, QTreeWidgetItem, QPlainTextEdit, QDialog)

import subprocess
import time
import os

from .nav_mainwindow import NavMainWindow


class ValidationIngestionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.completed = 0
        self.setWindowTitle('Validation and Ingestion Process')
        self.setFixedSize(1000, 600)
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
        cleansebutt.clicked.connect(self.on_cleanse_button_clicked)

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
        self.cleansefilelist = []
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
        self.searched_list = []
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
        self.ingestibletree.setHeaderHidden(True)
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
        self.noningestibletree.setHeaderHidden(True)
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

        self.logentryteamlabel = QLabel('Team: R|B|W')

        logentryteamlayout.addStretch()
        logentryteamlayout.addWidget(self.logentryteamlabel)
        logentryteamlayout.addStretch()

        self.logentrytimelabel = QLabel('Timestamp: Time of the Log Entry')

        logentrytimelayout.addStretch()
        logentrytimelayout.addWidget(self.logentrytimelabel)
        logentrytimelayout.addStretch()

        self.logentrypathlabel = QLabel('File Path: File path of file that created the Log Entry')

        logentrypathlayout.addStretch()
        logentrypathlayout.addWidget(self.logentrypathlabel)
        logentrypathlayout.addStretch()

        logentrydatalabel = QLabel('Data:    ')
        self.logentrydataptedit = QPlainTextEdit('Any data corresponding to this log entry will go here.')

        logentryboxlayout.addStretch()
        logentryboxlayout.addWidget(logentrydatalabel)
        logentryboxlayout.addWidget(self.logentrydataptedit)
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

    #On cleanse button click, start the text cleansing process for all files
    def on_cleanse_button_clicked(self):
        data = []
        #For every file in the list
        for index1 in range(0, len(self.cleansefilelist)):
            #Read the file first
            with open(self.cleansefilelist[index1], 'r') as file:
                # read a list of lines into data
                data = file.readlines()

            #For every string in the list
            for index2 in range(0, len(data)):
                clean_string = ''
                new_line = False
                #Check for new line at the end of string, make note of it to add it once the string is clean
                if '\n' in data[index2]:
                    new_line = True
                    data[index2] = data[index2][:-1]
                #Iterate through the string
                for character in data[index2]:
                    #Remove any unnecessary characters not within range from [space] to ~ in ASCII
                    if (ord(character) >= 32) and (ord(character) <= 126):
                        clean_string += character
                if new_line:
                    data[index2] = clean_string + '\n'
                else:
                    data[index2] = clean_string

            #Write the cleaned version back into the file
            with open(self.cleansefilelist[index1], 'w') as file:
                file.writelines(data)

            #Change the cleanse table to mark it as cleansed
            cleanse_item = QTableWidgetItem('yes')
            cleanse_item.setTextAlignment(Qt.AlignCenter)
            self.cleansetable.setItem(index1, 1, cleanse_item)
            #Add the item to validate table
            validate_status_item = QTableWidgetItem('no')
            validate_status_item.setTextAlignment(Qt.AlignCenter)
            validate_name_item = QTableWidgetItem(self.cleansefilelist[index1])
            validate_name_item.setTextAlignment(Qt.AlignCenter)
            self.validatetable.setItem(index1, 0, validate_name_item)
            self.validatetable.setItem(index1, 1, validate_status_item)

    #Create a table widget and populating it with cleansed files
    def create_table_cleanse(self, tablewidget, headerlabels):
        dirlist = []
        start_date_list = []
        end_date_list = []
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "../Data", "ProjectConfigData.txt"))
        filepath2 = os.path.abspath(os.path.join(basepath, "../Data", "DateRange.txt"))
        
        #read a list of lines into data
        with open(filepath, 'r') as file:
            data = file.readlines()

        #remove the root path as it is not needed here
        del data[0]

        #create list for directories
        for directory in data:
            dirlist.append(directory.rstrip())

        #retrieve date range for the project
        with open(filepath2, 'r') as file:
            data2 = file.readlines()
        #year, month, day
        start_date_list = data2[0].split('.')
        start_date_list = [int(i) for i in start_date_list]
        end_date_list = data2[1].split('.')
        end_date_list = [int(i) for i in end_date_list]

        #iterate through the list of directories
        for directory in dirlist:
            for r, d, f in os.walk(directory):
                for file in f:
                    #retrieve the time of the file
                    stat = os.stat(os.path.join(r, file))
                    file_time = (time.strftime('%Y.%m.%d', time.localtime(stat.st_mtime))).split('.')
                    file_time = [int(i) for i in file_time]
                    #check if the file is within the date range; if not, ignore it
                    #year
                    if (start_date_list[0] < file_time[0]) and (file_time[0] < end_date_list[0]):
                        self.cleansefilelist.append(os.path.join(r, file))
                    elif (start_date_list[0] == file_time[0]) and (file_time[0] < end_date_list[0]):
                        #month
                        if (start_date_list[1] < file_time[1]) and (file_time[1] < 12):
                            self.cleansefilelist.append(os.path.join(r, file))
                        elif (start_date_list[1] == file_time[1]):
                            #day
                            if (start_date_list[2] <= file_time[2]) and (file_time[2] <= 31):
                                self.cleansefilelist.append(os.path.join(r, file))
                    elif (start_date_list[0] < file_time[0]) and (file_time[0] == end_date_list[0]):
                        #month
                        if (1 < file_time[1]) and (file_time[1] < end_date_list[1]):
                            self.cleansefilelist.append(os.path.join(r, file))
                        elif (file_time[1] == end_date_list[1]):
                            #day
                            if (1 <= file_time[2]) and (file_time[2] <= end_date_list[2]):
                                self.cleansefilelist.append(os.path.join(r, file))
                    elif (start_date_list[0] == file_time[0]) and (file_time[0] == end_date_list[0]):
                        #month
                        if (start_date_list[1] < file_time[1]) and (file_time[1] < end_date_list[1]):
                            self.cleansefilelist.append(os.path.join(r, file))
                        elif (start_date_list[1] == file_time[1]) and (file_time[1] == end_date_list[1]):
                            #day
                            if (start_date_list[2] <= file_time[2]) and (file_time[2] <= end_date_list[2]):
                                self.cleansefilelist.append(os.path.join(r, file))
                        elif (start_date_list[1] == file_time[1]):
                            #day
                            if (start_date_list[2] <= file_time[2]) and (file_time[2] <= 31):
                                self.cleansefilelist.append(os.path.join(r, file))
                        elif (file_time[1] == end_date_list[1]):
                            #day
                            if (1 <= file_time[2]) and (file_time[2] <= end_date_list[2]):
                                self.cleansefilelist.append(os.path.join(r, file))

        tablewidget.setRowCount(len(self.cleansefilelist))
        tablewidget.setColumnCount(2)
        tablewidget.setHorizontalHeaderLabels(headerlabels)
        tablewidget.verticalHeader().setVisible(False)
        header = tablewidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

        #Populate table
        for x in range(tablewidget.rowCount()):
            for y in range(tablewidget.columnCount()):
                if y == 0:
                    path = self.cleansefilelist[x]
                    item = QTableWidgetItem(path)
                    item.setTextAlignment(Qt.AlignCenter)
                    tablewidget.setItem(x,y, item)
                else:
                    item = QTableWidgetItem('no')
                    item.setTextAlignment(Qt.AlignCenter)
                    tablewidget.setItem(x,y, item)

    #Create a table widget and populating it with validated files
    def create_table_validate(self, tablewidget, headerlabels):
        tablewidget.setRowCount(len(self.cleansefilelist))
        tablewidget.setColumnCount(2)
        tablewidget.setHorizontalHeaderLabels(headerlabels)
        tablewidget.verticalHeader().setVisible(False)
        header = tablewidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)

    #Create database list
    def create_dblist(self):
        dblist = []
        for index in range(len(self.searched_list)):
            dblist.append([])
        #First remove unnecessary items
        for index in range(len(self.searched_list)):
            #The number of the log entry
            dblist[index].append(int((self.searched_list[index][0].split()[3:])[0])) #int
            #The team for the log file
            dblist[index].append(self.searched_list[index][3]) #string
            #Timestamp of log entry
            dblist[index].append(self.searched_list[index][2].split()[1]) #string, format YYYY.M.D
            #Filepath of log file responsible for log entry
            dblist[index].append(self.searched_list[index][4]) #string
            #Location specified in the log entry
            dblist[index].append(self.searched_list[index][2].split()[3]) #string
            #Event type
            dblist[index].append(self.searched_list[index][2].split()[5]) #string
            #Event description
            event_desc_index = self.searched_list[index][2].find('Description:')
            event_desc_index += 13
            dblist[index].append(self.searched_list[index][2][event_desc_index:]) #string
        #print(dblist)
        return dblist

    #Splunk method to upload to local splunk server
    def push_to_splunk(self, tablewidget):
        for row in range(tablewidget.rowCount()):
            twi0 = tablewidget.item(row,0)
            splunkcmd = subprocess.run(["/Applications/Splunk/bin/splunk", "add", "oneshot", twi0.text()])
            #print("The exit code was: %d" % splunkcmd.returncode)
            print(twi0.text())
        test = SplunkDataSearch()
        #The list will be inverted
        self.searched_list = test.item_return
        self.database_list = self.create_dblist()

        log_entry_items: list = list()
        for item in self.database_list:
            logentry_item: dict = DatabaseInterface.create_log_entries_item(
                list_number=str(item[0]),
                timestamp=str(item[2]),
                event=str(item[6]),
                vector='None',
                location=str(item[4]),
                creator=str(item[1]),
                filepath=str(item[3]),
                eventtype=str(item[5]),
                vector_id='')
            log_entry_items.append(logentry_item)

        DatabaseInterface.insert_many_log_entries(log_entries_items=log_entry_items)
        templist: list = DatabaseInterface.find_log_entries_all()
        pprint.pprint(templist)

        #print(self.searched_list)
        #Change the validate table to mark it as validated
        for index in range(0, len(self.searched_list)):
            validate_item = QTableWidgetItem('yes')
            validate_item.setTextAlignment(Qt.AlignCenter)
            self.validatetable.setItem(index, 1, validate_item)
        self.add_ingestable_entries()

    #Add validated log entries to the ingestable tree list
    def add_ingestable_entries(self):
        for list_elem in self.searched_list:
            list_item = QTreeWidgetItem([list_elem][0])
            self.ingestibletree.addTopLevelItem(list_item)

    #Selection of item on ingestibletree widget
    def on_ingestitem_selected(self):
        getSelected = self.ingestibletree.selectedItems()
        getChildNode = None
        if getSelected:
            baseNode = getSelected[0]
            getChildNode = baseNode.text(0)
        self.change_logentry_display(getChildNode)

    #Selection of item on noningestibletree widget
    def on_noningestitem_selected(self):
        getSelected = self.noningestibletree.selectedItems()
        getChildNode = None
        if getSelected:
            baseNode = getSelected[0]
            getChildNode = baseNode.text(0)
        self.change_logentry_display(getChildNode)

    #Change log entry information
    def change_logentry_display(self, name):
        self.logentrynamelabel.setText(name)

        #Retrieving information of that item
        num = int(name.split()[3]) - 1
        self.logentrytimelabel.setText(self.searched_list[num][2].split()[0] + ' ' + self.searched_list[num][2].split()[1])
        self.logentrydataptedit.setPlainText(self.searched_list[num][2])
        self.logentryteamlabel.setText('Team: ' + self.searched_list[num][3])
        self.logentrypathlabel.setText('File Path: ' + self.searched_list[num][4])

    #On validate button click call splunk method
    def on_validate_button_clicked(self):
        self.push_to_splunk(self.validatetable)

    #Move on to the next window[Ui_mainwindow_navigation] on ingest button click
    def on_ingest_button_clicked(self):
        self.hide()
        self.window = NavMainWindow()
        self.window.show()
