from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QCalendarWidget, QLabel, QPushButton
from PyQt5.QtCore import QDate, QCoreApplication
from datetime import datetime

class CalendarDialog(QDialog):
    def __init__(self, projectconfigwindow_classobject): #Multiple inheritance, see documentation on super().__init__()
        super(CalendarDialog, self).__init__()
        self.start_calendar = projectconfigwindow_classobject.start_date_calendar
        self.end_calendar = projectconfigwindow_classobject.end_date_calendar
        self.date_picked = ''
        self.setWindowTitle('Date Picker')
        self.setFixedSize(400, 300)
        mainlayout = QVBoxLayout()
        exitlayout = QHBoxLayout()

        self.my_calendar = QCalendarWidget(self)
        self.my_calendar.setGridVisible(True)
        if self.end_calendar == True:
            self.my_calendar.setMinimumDate(QDate(projectconfigwindow_classobject.minimumdate[2], projectconfigwindow_classobject.minimumdate[0], projectconfigwindow_classobject.minimumdate[1]))
        self.my_calendar.clicked[QDate].connect(self.show_date)

        self.date_label = QLabel(self)
        date = self.my_calendar.selectedDate()
        self.date_label.setText(date.toString())
        confirmbutt = QPushButton('Confirm Date')
        confirmbutt.clicked.connect(self.on_confirm_button_clicked)

        exitlayout.addWidget(self.date_label)
        exitlayout.addWidget(confirmbutt)

        mainlayout.addWidget(self.my_calendar)
        mainlayout.addLayout(exitlayout)
        self.setLayout(mainlayout)

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
        self.date_label.setText(date.toString())
        if self.start_calendar == True:
            self.setMinimumConv(date)

    def on_confirm_button_clicked(self):
        self.date_picked = self.date_label.text()
        self.close()
    