from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QStandardItem
import uuid


class QStandardItemDateTime(QStandardItem):

    def __init__(self, text_info: str, start_datetime: QDateTime, end_datetime: QDateTime) -> object:
        """
        Parameters:
        :param text_info: the text QStandardItem will use as the initial name of the item
        :param start_datetime_info: the start date time the user selected as a string
        :param end_datetime_info: the end date time the user selected as a string
        """
        self.ItemType = 1001
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.uid = uuid.uuid1()
        super().__init__(str(text_info))
