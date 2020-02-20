from .mainwindow_nav import Ui_mainwindow_navigation
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
                            QHeaderView, QFrame, QTreeWidget, QTreeWidgetItem, QPlainTextEdit, QDialog)

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

        cleansetable = QTableWidget()
        cleanseheaderlabels = ['Location/Name', 'Cleansed']
        self.create_table(cleansetable, cleanseheaderlabels)

        cleansecontainergrid.addLayout(cleansecontainerlayout, 0, 0)
        cleansecontainergrid.addWidget(cleansetable, 0, 1)

        validationtitlelabel = QLabel('Validation Overview')

        validationtitlelayout.addStretch()
        validationtitlelayout.addWidget(validationtitlelabel)
        validationtitlelayout.addStretch()

        validationinfolabel = QLabel('Validate Un-Validated Log Files')

        validationinfolayout.addStretch()
        validationinfolayout.addWidget(validationinfolabel)
        validationinfolayout.addStretch()

        validatebutt = QPushButton('Validate')

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

        validatetable = QTableWidget()
        validateheaderlabels = ['Location/Name', 'Validated']
        self.create_table(validatetable, validateheaderlabels)

        validationcontainergrid.addLayout(validationcontainerlayout, 0, 0)
        validationcontainergrid.addWidget(validatetable, 0, 1)

        logtitlelabel = QLabel('Log Overview')

        logtitlelayout.addStretch()
        logtitlelayout.addWidget(logtitlelabel)
        logtitlelayout.addStretch()

        ingestibletitlelabel = QLabel('Ingestible Log Entries')

        ingestibletitlelayout.addStretch()
        ingestibletitlelayout.addWidget(ingestibletitlelabel)
        ingestibletitlelayout.addStretch()

        ingestibletree = QTreeWidget()
        data = ['Log Entry ####', 'Log Entry ####+1', 'Log Entry ####+2', 'Log Entry ####+3', 'Log Entry ####+4', 'Log Entry ####+5', 'Log Entry ####+6', 'Log Entry ####+7', 'Log Entry ####+8']
        self.create_treelist(ingestibletree, data)

        ingestibletreelayout.addStretch()
        ingestibletreelayout.addWidget(ingestibletree)
        ingestibletreelayout.addStretch()

        ingestiblecontainerlayout.addLayout(ingestibletitlelayout)
        ingestiblecontainerlayout.addLayout(ingestibletreelayout)

        noningestibletitlelabel = QLabel('Non-Ingestible Log Entries')

        noningestibletitlelayout.addStretch()
        noningestibletitlelayout.addWidget(noningestibletitlelabel)
        noningestibletitlelayout.addStretch()

        noningestibletree = QTreeWidget()
        nondata = ['Log Entry ####', 'Log Entry ####+1', 'Log Entry ####+2', 'Log Entry ####+3', 'Log Entry ####+4', 'Log Entry ####+5', 'Log Entry ####+6', 'Log Entry ####+7', 'Log Entry ####+8']
        self.create_treelist(noningestibletree, nondata)

        noningestibletreelayout.addStretch()
        noningestibletreelayout.addWidget(noningestibletree)
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

        logentrynamelabel = QLabel('Name: Log Entry ####')

        logentrynamelayout.addStretch()
        logentrynamelayout.addWidget(logentrynamelabel)
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

    def on_ingest_button_clicked(self):
        self.hide()
        #Due to mainwindow_nav being created through designer I had to call the window as follows
        MainWindow = QMainWindow()
        ui = Ui_mainwindow_navigation()
        ui.setupUi(MainWindow)
        self.window = MainWindow
        self.window.show()


    def create_table(self, tablewidget, headerlabels):
        tablewidget.setRowCount(10)
        tablewidget.setColumnCount(2)
        tablewidget.setHorizontalHeaderLabels(headerlabels)
        tablewidget.verticalHeader().setVisible(False)
        header = tablewidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        for x in range(tablewidget.rowCount()):
            for y in range(tablewidget.columnCount()):
                if y == 0:
                    path = '/root/Users/Test/Desktop/Example'+str(x+1)
                    item = QTableWidgetItem(path)
                    item.setTextAlignment(Qt.AlignCenter)
                    tablewidget.setItem(x,y, item)
                else:
                    item = QTableWidgetItem('yes')
                    item.setTextAlignment(Qt.AlignCenter)
                    tablewidget.setItem(x,y, item)

    def create_treelist(self, treewidget, data):
        treewidget.setHeaderHidden(True)
        for x in data:
            list_item = QTreeWidgetItem([x])
            treewidget.addTopLevelItem(list_item)
