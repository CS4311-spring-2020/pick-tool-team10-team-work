from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QDateTimeEdit, QLineEdit, QMessageBox

#import Dialogs.timefilter_dialog as td
#from timefilter_dialog import TimefilterDialog


class TimefilterInputInterface:

    #timefilter_dialog = TimefilterDialog
    timefilter_dialog = None

    @staticmethod
    def interface_setup(timefilter_dialog):
        TimefilterInputInterface.timefilter_dialog = timefilter_dialog
        TimefilterInputInterface.button_setup()
        TimefilterInputInterface.datetimeedit_setup()
        TimefilterInputInterface.lineedit_setup()

    @staticmethod
    def button_setup():
        TimefilterInputInterface.timefilter_dialog.button_cancel_tfil.clicked.connect(
            TimefilterInputInterface.button_cancel_tfil_clicked)
        TimefilterInputInterface.timefilter_dialog.button_ok_tfil.clicked.connect(
            TimefilterInputInterface.button_ok_tfil_clicked)

    @staticmethod
    def datetimeedit_setup():
        start_datetime = TimefilterInputInterface.timefilter_dialog.datetime_item.start_datetime
        end_datetime = TimefilterInputInterface.timefilter_dialog.datetime_item.end_datetime
        TimefilterInputInterface.timefilter_dialog.datetimeedit_starttime_tfil.setDateTime(start_datetime)
        TimefilterInputInterface.timefilter_dialog.datetimeedit_endtime_tfil.setDateTime(end_datetime)

    @staticmethod
    def lineedit_setup():
        datetime_edit_text = TimefilterInputInterface.timefilter_dialog.datetime_item.text()
        TimefilterInputInterface.timefilter_dialog.linedit_timefiltername_tfil.setText(datetime_edit_text)

    @staticmethod
    def button_cancel_tfil_clicked():
        TimefilterInputInterface.timefilter_dialog.reject()

    @staticmethod
    def button_ok_tfil_clicked():
        start_datetime = TimefilterInputInterface.timefilter_dialog.datetimeedit_starttime_tfil.dateTime()
        end_datetime = TimefilterInputInterface.timefilter_dialog.datetimeedit_endtime_tfil.dateTime()
        start_datetime_info = start_datetime.toString('yyyyMMddhhmmss')
        end_datetime_info = end_datetime.toString('yyyyMMddhhmmss')
        if TimefilterInputInterface.check_datetimes_values(int(start_datetime_info), int(end_datetime_info)) is False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('End time must be greater than start time.')
            msg.setWindowTitle("Time Filter Error")
            msg.exec_()
            return
        TimefilterInputInterface.timefilter_dialog.accept()

    @staticmethod
    def check_datetimes_values(start_datetime_info: int, end_datetime_info: int) -> bool:
        return (start_datetime_info - end_datetime_info) < 0
