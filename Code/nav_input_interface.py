from PyQt5.QtCore import QDateTime, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import nav_mainwindow as nmw
from PyQt5.QtWidgets import QMainWindow, QStyleFactory, QAbstractItemView, QCheckBox, QErrorMessage, QMessageBox, \
    QListView, QDialog, QDateTimeEdit

import timefilter_dialog as td
from qstandarditem_datetime import QStandardItemDateTime


class NavInputInterface:
    nav_mainwindow = nmw.NavMainWindow

    @staticmethod
    def interface_setup(nav_mainwindow):
        NavInputInterface.nav_mainwindow = nav_mainwindow
        NavInputInterface.checkbox_setup()
        NavInputInterface.button_setup()
        NavInputInterface.listview_setup()

    @staticmethod
    def checkbox_setup():
        # show and hide checkboxes
        NavInputInterface.nav_mainwindow.checkbox_listnumber_navi.clicked.connect(
            NavInputInterface.checkbox_listnumber_navi_clicked)
        NavInputInterface.nav_mainwindow.checkbox_timestamp_navi.clicked.connect(
            NavInputInterface.checkbox_timestamp_navi_clicked)
        NavInputInterface.nav_mainwindow.checkbox_event_navi.clicked.connect(
            NavInputInterface.checkbox_event_navi_clicked)
        NavInputInterface.nav_mainwindow.checkbox_vector_navi.clicked.connect(
            NavInputInterface.checkbox_vector_navi_clicked)

        # significant checkbox
        NavInputInterface.nav_mainwindow.checkbox_significant_navi.clicked.connect(
            NavInputInterface.checkbox_significant_navi_clicked)

        # team checkboxes
        NavInputInterface.nav_mainwindow.checkbox_blue_navi.clicked.connect(
            NavInputInterface.checkbox_blue_navi_clicked)
        NavInputInterface.nav_mainwindow.checkbox_red_navi.clicked.connect(
            NavInputInterface.checkbox_red_navi_clicked)
        NavInputInterface.nav_mainwindow.checkbox_white_navi.clicked.connect(
            NavInputInterface.checkbox_white_navi_clicked)

    @staticmethod
    def button_setup():
        # for undo and redo buttons
        NavInputInterface.nav_mainwindow.button_undo_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_undo_navi.clicked.connect(
            NavInputInterface.button_undo_navi_clicked)
        NavInputInterface.nav_mainwindow.button_redo_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_redo_navi.clicked.connect(
            NavInputInterface.button_redo_navi_clicked)

        # time filter button
        NavInputInterface.nav_mainwindow.button_timefilter_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_timefilter_navi.clicked.connect(
            NavInputInterface.button_timefilter_navi_clicked)

        # for push and pull buttons
        NavInputInterface.nav_mainwindow.button_push_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_push_navi.clicked.connect(
            NavInputInterface.button_push_navi_clicked)
        NavInputInterface.nav_mainwindow.button_pull_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_pull_navi.clicked.connect(
            NavInputInterface.button_pull_navi_clicked)

        # for vector and table view button
        NavInputInterface.nav_mainwindow.button_vectortableview_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_vectortableview_navi.clicked.connect(
            NavInputInterface.button_vectortableview_navi_clicked)

    @staticmethod
    def listview_setup():
        NavInputInterface.nav_mainwindow.listview_location_navi.setEditTriggers(QAbstractItemView.DoubleClicked)
        model = QStandardItemModel()
        model.setItemPrototype(QStandardItem())
        model.itemChanged.connect(NavInputInterface.listview_location_navi_item_change)
        NavInputInterface.nav_mainwindow.listview_location_navi.setModel(model)
        NavInputInterface.listview_location_navi_add_items()

        NavInputInterface.nav_mainwindow.listview_timefilter_navi.doubleClicked.connect(
            NavInputInterface.listview_timefilter_navi_doubleclicked)
        model = QStandardItemModel()
        model.setItemPrototype(QStandardItemDateTime(str, str, str))
        model.itemChanged.connect(NavInputInterface.listview_timefilter_navi_item_change)
        NavInputInterface.nav_mainwindow.listview_timefilter_navi.setModel(model)

        NavInputInterface.nav_mainwindow.listview_vectors_navi.setEditTriggers(QAbstractItemView.DoubleClicked)
        model = QStandardItemModel()
        model.setItemPrototype(QStandardItem())
        model.itemChanged.connect(NavInputInterface.listview_vectors_navi_item_change)
        NavInputInterface.nav_mainwindow.listview_vectors_navi.setModel(model)
        NavInputInterface.listview_vectors_navi_add_items()

    @staticmethod
    def listview_timefilter_navi_doubleclicked(index: QModelIndex):
        datetime_item = index.model().itemFromIndex(index)
        timefilter_dialog = td.TimefilterDialog(datetime_item)
        if timefilter_dialog.exec() == QDialog.Accepted:
            index.model().itemFromIndex(index).start_datetime = timefilter_dialog.datetimeedit_starttime_tfil.dateTime()
            index.model().itemFromIndex(index).end_datetime = timefilter_dialog.datetimeedit_endtime_tfil.dateTime()
            index.model().itemFromIndex(index).setText(timefilter_dialog.linedit_timefiltername_tfil.text())
            print("Dialog accepted")
        else:
            print("rejected")

    @staticmethod
    def listview_location_navi_add_items():
        # where will locations be stored?
        for n in range(10):
            item = QStandardItem('Location %s' % n)
            item.setCheckable(True)
            item.setEditable(True)
            NavInputInterface.nav_mainwindow.listview_location_navi.model().appendRow(item)

    @staticmethod
    def listview_timefilter_navi_add_item(start_datetime: QDateTime, end_datetime: QDateTime):
        # if the time filter length is not equal to the db length, redo table
        item = QStandardItemDateTime('user_time_filter', start_datetime, end_datetime)
        item.setCheckable(True)
        item.setEditable(False)
        NavInputInterface.nav_mainwindow.listview_timefilter_navi.model().appendRow(item)
        # now add to database

    @staticmethod
    def listview_vectors_navi_add_items():
        # must get vector names from vector db table
        for n in range(10):
            item = QStandardItem('Vector %s' % n)
            item.setCheckable(True)
            item.setEditable(False)
            NavInputInterface.nav_mainwindow.listview_vectors_navi.model().appendRow(item)

    @staticmethod
    def listview_location_navi_item_change(item):
        print(item.text() + " " + str(item.checkState()))

    @staticmethod
    def listview_timefilter_navi_item_change(item):
        print(item.text() + " " + str(item.checkState()))

    @staticmethod
    def listview_vectors_navi_item_change(item):
        print(item.text() + " " + str(item.checkState()))

    @staticmethod
    def checkbox_listnumber_navi_clicked():
        print(NavInputInterface.nav_mainwindow.checkbox_listnumber_navi.text())
        checkbox_listnumber_state = NavInputInterface.nav_mainwindow.checkbox_listnumber_navi.isChecked()
        if checkbox_listnumber_state is True:  # checked state
            print('Checked State')
        elif checkbox_listnumber_state is False:  # unchecked state
            print('Unchecked State')
        else:
            print('Error State')

    @staticmethod
    def checkbox_timestamp_navi_clicked():
        print(NavInputInterface.nav_mainwindow.checkbox_timestamp_navi.text())
        checkbox_timestamp_state = NavInputInterface.nav_mainwindow.checkbox_timestamp_navi.isChecked()
        if checkbox_timestamp_state is True:  # checked state
            print('Checked State')
        elif checkbox_timestamp_state is False:  # unchecked state
            print('Checked State')
        else:
            print('Error State')

    @staticmethod
    def checkbox_event_navi_clicked():
        print(NavInputInterface.nav_mainwindow.checkbox_event_navi.text())
        checkbox_event_state = NavInputInterface.nav_mainwindow.checkbox_event_navi.isChecked()
        if checkbox_event_state is True:  # checked state
            print('Checked State')
        elif checkbox_event_state is False:  # unchecked state
            print('Unchecked State')
        else:
            print('Error State')

    @staticmethod
    def checkbox_vector_navi_clicked():
        print(NavInputInterface.nav_mainwindow.checkbox_vector_navi.text())
        checkbox_vector_state = NavInputInterface.nav_mainwindow.checkbox_vector_navi.isChecked()
        if checkbox_vector_state is True:  # checked state
            print('Checked State')
        elif checkbox_vector_state is False:  # unchecked state
            print('Unchecked State')
        else:
            print('Error State')

    @staticmethod
    def checkbox_significant_navi_clicked():
        print(NavInputInterface.nav_mainwindow.checkbox_significant_navi.text())
        checkbox_significant_state = NavInputInterface.nav_mainwindow.checkbox_significant_navi.isChecked()
        if checkbox_significant_state is True:  # checked state
            print('Checked State')
        elif checkbox_significant_state is False:  # unchecked state
            print('Unchecked State')
        else:
            print('Error State')

    @staticmethod
    def checkbox_blue_navi_clicked():
        print(NavInputInterface.nav_mainwindow.checkbox_blue_navi.text())
        checkbox_blue_state = NavInputInterface.nav_mainwindow.checkbox_blue_navi.isChecked()
        if checkbox_blue_state is True:  # checked state
            print('Checked State')
        elif checkbox_blue_state is False:  # unchecked state
            print('Unchecked State')
        else:
            print('Error State')

    @staticmethod
    def checkbox_red_navi_clicked():
        print(NavInputInterface.nav_mainwindow.checkbox_red_navi.text())
        checkbox_red_state = NavInputInterface.nav_mainwindow.checkbox_red_navi.isChecked()
        if checkbox_red_state is True:  # checked state
            print('Checked State')
        elif checkbox_red_state is False:  # unchecked state
            print('Unchecked State')
        else:
            print('Error State')

    @staticmethod
    def checkbox_white_navi_clicked():
        print(NavInputInterface.nav_mainwindow.checkbox_white_navi.text())
        checkbox_white_state = NavInputInterface.nav_mainwindow.checkbox_white_navi.isChecked()
        if checkbox_white_state is True:  # checked state
            print('Checked State')
        elif checkbox_white_state is False:  # unchecked state
            print('Unchecked State')
        else:
            print('Error State')

    @staticmethod
    def button_undo_navi_clicked():
        # TODO Call & Create undo functionality method(s0
        #   Complete Req = optional
        #   Author = Aaron
        print(NavInputInterface.nav_mainwindow.button_undo_navi.text())
        NavInputInterface.nav_mainwindow.button_undo_navi.toggle()

    @staticmethod
    def button_redo_navi_clicked():
        # TODO Call & Create redo functionality method(s)
        #   Complete Req = optional
        #   Author = Aaron
        print(NavInputInterface.nav_mainwindow.button_redo_navi.text())
        NavInputInterface.nav_mainwindow.button_redo_navi.toggle()

    @staticmethod
    def button_push_navi_clicked():
        # TODO Call & Create push functionality method(s)
        #   Complete Req = unknown (probably required)
        #   Author = Angelica
        print(NavInputInterface.nav_mainwindow.button_push_navi.text())
        NavInputInterface.nav_mainwindow.button_push_navi.toggle()

    @staticmethod
    def button_pull_navi_clicked():
        # TODO Call & Create pull functionality method(s)
        #   Complete Req = unknown (probably required)
        #   Author = Anglelica
        print(NavInputInterface.nav_mainwindow.button_pull_navi.text())
        NavInputInterface.nav_mainwindow.button_pull_navi.toggle()

    @staticmethod
    def button_timefilter_navi_clicked():
        print(NavInputInterface.nav_mainwindow.button_timefilter_navi.text())
        NavInputInterface.nav_mainwindow.button_timefilter_navi.toggle()
        start_datetime = NavInputInterface.nav_mainwindow.datetimeedit_starttime_navi.dateTime()
        end_datetime = NavInputInterface.nav_mainwindow.datetimeedit_endtime_navi.dateTime()
        start_datetime_info = start_datetime.toString('yyyyMMddhhmmss')
        end_datetime_info = end_datetime.toString('yyyyMMddhhmmss')
        if NavInputInterface.check_datetimes_values(int(start_datetime_info), int(end_datetime_info)) is False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('End time must be greater than start time.')
            msg.setWindowTitle("Time Filter Error")
            msg.exec_()
            return
        NavInputInterface.listview_timefilter_navi_add_item(start_datetime, end_datetime)

    @staticmethod
    def button_vectortableview_navi_clicked():
        # TODO Open up the vectortableview
        #   Complete Req = required
        #   Author = Aaron and Andy
        print(NavInputInterface.nav_mainwindow.button_vectortableview_navi.text())
        NavInputInterface.nav_mainwindow.button_vectortableview_navi.toggle()

    @staticmethod
    def check_datetimes_values(start_datetime_info: int, end_datetime_info: int) -> bool:
        return (start_datetime_info - end_datetime_info) < 0


"""
def button_vectortableview_navi_clicked(self):
    from mainwindow_vectortableview import Ui_mainwindow_vectortableview
    self.window = QtWidgets.QMainWindow()
    self.ui = Ui_mainwindow_vectortableview()
    self.ui.setupUi(self.window)
    mainwindow_navigation.hide()
    self.window.show()


self.button_setup()
"""
