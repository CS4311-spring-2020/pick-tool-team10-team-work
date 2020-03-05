from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QCalendarWidget, QLabel, QPushButton
from PyQt5.QtCore import QDate, QCoreApplication
from datetime import datetime

class CalendarDialog(QDialog):
    def __init__(self, calendarList = None, parent = None):
        super(CalendarDialog, self).__init__()
        self.date_picked = ''
        self.setWindowTitle('Date Picker')
        self.setFixedSize(400, 300)
        mainlayout = QVBoxLayout()
        exitlayout = QHBoxLayout()

        self.my_calendar = QCalendarWidget(self)
        self.my_calendar.setGridVisible(True)
        self.calendarList = calendarList
        if self.calendarList is not None:
            self.my_calendar.setMinimumDate(QDate(self.calendarList[0], self.calendarList[1], self.calendarList[2]))
        self.my_calendar.clicked[QDate].connect(self.show_date)

        self.my_label = QLabel(self)
        date = self.my_calendar.selectedDate()
        self.my_label.setText(date.toString())
        confirmbutt = QPushButton('Confirm Date')
        confirmbutt.clicked.connect(self.on_confirm_button_clicked)

        exitlayout.addWidget(self.my_label)
        exitlayout.addWidget(confirmbutt)

        mainlayout.addWidget(my_calendar)
        mainlayout.addLayout(exitlayout)
        self.setLayout(mainlayout)

    def setCalType(self, caltype):
        self.calendarType = caltype

    def setMinimumConv(self, date):
        month = {	
        'Jan':1,
		'Feb':2,
		'Mar':3,
		'Apr':4,
		'May':5,
		'Jun':6,
		'Jul':7,
		'Aug':8,
		'Sep':9,
		'Oct':10,
		'Nov':11,
		'Dec':12}
        minimumdateconversionlist = date.toString().split()
        self.minimumdatelist = [month.get(minimumdateconversionlist[1]), minimumdateconversionlist[2], minimumdateconversionlist[3]]

    def show_date(self, date):
        self.my_label.setText(date.toString())
        if self.calendarList is None:
            setMinimumConv(date)

    def on_confirm_button_clicked(self):
        self.date_picked = self.my_label.text()
        self.close()
    