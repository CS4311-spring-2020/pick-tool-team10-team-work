from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QDateTimeEdit, QLineEdit, QMessageBox
from Database.databse_interface import DatabaseInterface
#from Dialogs.timefilter_dialog import TimefilterDialog


class TimefilterInputInterface:
    #timefilter_dialog = TimefilterDialog()
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
        TimefilterInputInterface.timefilter_dialog.button_delete_tfil.clicked.connect(
            TimefilterInputInterface.button_delete_tfil_clicked)

    @staticmethod
    def datetimeedit_setup():
        start_datetimeedit: QDateTimeEdit = TimefilterInputInterface.timefilter_dialog.datetimeedit_starttime_tfil
        end_datetimeedit: QDateTimeEdit = TimefilterInputInterface.timefilter_dialog.datetimeedit_endtime_tfil
        start_datetime: QDateTime
        end_datetime: QDateTime
        timefilters_item_id = TimefilterInputInterface.timefilter_dialog.timefilter_id
        timefilters_item = DatabaseInterface.find_one_time_filters_by_id(timefilters_item_id)
        start_datetime = QDateTime.fromString(timefilters_item['starttime'], 'yyyyMMddhhmmss')
        end_datetime = QDateTime.fromString(timefilters_item['endtime'], 'yyyyMMddhhmmss')
        start_datetimeedit.setDateTime(start_datetime)
        end_datetimeedit.setDateTime(end_datetime)

    @staticmethod
    def lineedit_setup():
        lineedit_timefilter: QLineEdit = TimefilterInputInterface.timefilter_dialog.linedit_timefiltername_tfil
        timefilters_item_id: str = TimefilterInputInterface.timefilter_dialog.timefilter_id
        timefilters_item: dict = DatabaseInterface.find_one_time_filters_by_id(timefilters_item_id)
        lineedit_timefilter.setText(timefilters_item['name'])

    @staticmethod
    def button_cancel_tfil_clicked():
        TimefilterInputInterface.timefilter_dialog.reject()

    @staticmethod
    def button_delete_tfil_clicked():
        timefilters_item_id: str = TimefilterInputInterface.timefilter_dialog.timefilter_id
        DatabaseInterface.delete_one_time_filters_by_id(timefilter_id=timefilters_item_id)
        TimefilterInputInterface.timefilter_dialog.accept()

    @staticmethod
    def button_ok_tfil_clicked():
        start_datetime: QDateTime = TimefilterInputInterface.timefilter_dialog.datetimeedit_starttime_tfil.dateTime()
        end_datetime: QDateTime = TimefilterInputInterface.timefilter_dialog.datetimeedit_endtime_tfil.dateTime()
        start_datetime_info: str = start_datetime.toString('yyyyMMddhhmmss')
        end_datetime_info: str = end_datetime.toString('yyyyMMddhhmmss')
        if TimefilterInputInterface.check_datetimes_values(int(start_datetime_info), int(end_datetime_info)) is False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('End time must be greater than start time.')
            msg.setWindowTitle("Time Filter Error")
            msg.exec_()
            return

        lineedit_timefilter: QLineEdit = TimefilterInputInterface.timefilter_dialog.linedit_timefiltername_tfil
        lineedit_timefilter_text = lineedit_timefilter.text()
        if len(lineedit_timefilter_text) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Time filter name cannot be blank!')
            msg.setWindowTitle("Time Filter Error")
            msg.exec_()
            return

        timefilters_item_id: str = TimefilterInputInterface.timefilter_dialog.timefilter_id
        update_fields: dict = {'name': lineedit_timefilter_text,
                               'starttime': start_datetime_info,
                               'endtime': end_datetime_info }
        DatabaseInterface.update_one_time_filters_by_id(timefilter_id=timefilters_item_id,
                                                        update_fields=update_fields)
        TimefilterInputInterface.timefilter_dialog.accept()

    @staticmethod
    def check_datetimes_values(start_datetime_info: int, end_datetime_info: int) -> bool:
        return (start_datetime_info - end_datetime_info) < 0
