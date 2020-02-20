from PyQt5.QtWidgets import QDialog, QWidget, QVBoxLayout, QHBoxLayout, QCalendarWidget, QLabel, QPushButton
from PyQt5.QtCore import QDate, QCoreApplication

class CalendarDialog(QDialog):
    def __init__(self, parent = None):
        super(CalendarDialog, self).__init__()
        self.date_picked = ''
        self.setWindowTitle('Date Picker')
        self.setFixedSize(400, 300)
        mainlayout = QVBoxLayout()
        exitlayout = QHBoxLayout()

        my_calendar = QCalendarWidget(self)
        my_calendar.setGridVisible(True)
        my_calendar.clicked[QDate].connect(self.show_date)

        self.my_label = QLabel(self)
        date = my_calendar.selectedDate()
        self.my_label.setText(date.toString())
        confirmbutt = QPushButton('Confirm Date')
        confirmbutt.clicked.connect(self.on_confirm_button_clicked)

        exitlayout.addWidget(self.my_label)
        exitlayout.addWidget(confirmbutt)

        mainlayout.addWidget(my_calendar)
        mainlayout.addLayout(exitlayout)
        self.setLayout(mainlayout)

    def show_date(self, date):
        self.my_label.setText(date.toString())

    def on_confirm_button_clicked(self):
        self.date_picked = self.my_label.text()
        self.close()
    