# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nav_timefilter.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from qstandarditem_datetime import QStandardItemDateTime
from timefilter_input_interface import TimefilterInputInterface


class TimefilterDialog(QDialog):
    def __init__(self, datetime_item: QStandardItemDateTime):
        super().__init__()
        self.datetime_item = datetime_item

        self.setObjectName("timefilter_dialog")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(639, 425)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.vl_allhls_tfil = QtWidgets.QVBoxLayout()
        self.vl_allhls_tfil.setObjectName("vl_allhls_tfil")

        self.hl_timefiltername_tfil = QtWidgets.QHBoxLayout()
        self.hl_timefiltername_tfil.setObjectName("hl_timefiltername_tfil")

        self.label_timefiltername_tfil = QtWidgets.QLabel(self)
        self.label_timefiltername_tfil.setObjectName("label_timefiltername_tfil")
        self.hl_timefiltername_tfil.addWidget(self.label_timefiltername_tfil)

        self.linedit_timefiltername_tfil = QtWidgets.QLineEdit(self)
        self.linedit_timefiltername_tfil.setObjectName("linedit_timefiltername_tfil")
        self.hl_timefiltername_tfil.addWidget(self.linedit_timefiltername_tfil)

        self.vl_allhls_tfil.addLayout(self.hl_timefiltername_tfil)

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vl_allhls_tfil.addItem(spacerItem)

        self.hl_starttime_tfil = QtWidgets.QHBoxLayout()
        self.hl_starttime_tfil.setObjectName("hl_starttime_tfil")

        self.label_starttime_tfil = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_starttime_tfil.sizePolicy().hasHeightForWidth())
        self.label_starttime_tfil.setSizePolicy(sizePolicy)
        self.label_starttime_tfil.setObjectName("label_starttime_tfil")
        self.hl_starttime_tfil.addWidget(self.label_starttime_tfil)

        self.datetimeedit_starttime_tfil = QtWidgets.QDateTimeEdit(self)
        self.datetimeedit_starttime_tfil.setObjectName("datetimeedit_starttime_tfil")
        self.hl_starttime_tfil.addWidget(self.datetimeedit_starttime_tfil)

        self.vl_allhls_tfil.addLayout(self.hl_starttime_tfil)

        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vl_allhls_tfil.addItem(spacerItem1)

        self.hl_endtime_tfil = QtWidgets.QHBoxLayout()
        self.hl_endtime_tfil.setObjectName("hl_endtime_tfil")

        self.label_endtime_tfil = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_endtime_tfil.sizePolicy().hasHeightForWidth())
        self.label_endtime_tfil.setSizePolicy(sizePolicy)
        self.label_endtime_tfil.setObjectName("label_endtime_tfil")
        self.hl_endtime_tfil.addWidget(self.label_endtime_tfil)

        self.datetimeedit_endtime_tfil = QtWidgets.QDateTimeEdit(self)
        self.datetimeedit_endtime_tfil.setObjectName("datetimeedit_endtime_tfil")
        self.hl_endtime_tfil.addWidget(self.datetimeedit_endtime_tfil)

        self.vl_allhls_tfil.addLayout(self.hl_endtime_tfil)

        spacerItem2 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vl_allhls_tfil.addItem(spacerItem2)

        self.hl_returnbuttons_tfil = QtWidgets.QHBoxLayout()
        self.hl_returnbuttons_tfil.setObjectName("hl_returnbuttons_tfil")

        self.button_cancel_tfil = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancel_tfil.sizePolicy().hasHeightForWidth())
        self.button_cancel_tfil.setSizePolicy(sizePolicy)
        self.button_cancel_tfil.setMinimumWidth(100)
        self.button_cancel_tfil.setAutoDefault(False)
        self.button_cancel_tfil.setObjectName("button_cancel_tfil")
        self.hl_returnbuttons_tfil.addWidget(self.button_cancel_tfil)

        self.button_ok_tfil = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ok_tfil.sizePolicy().hasHeightForWidth())
        self.button_ok_tfil.setSizePolicy(sizePolicy)
        self.button_ok_tfil.setMinimumWidth(100)
        self.button_ok_tfil.setAutoDefault(False)
        self.button_ok_tfil.setObjectName("button_ok_tfil")
        self.hl_returnbuttons_tfil.addWidget(self.button_ok_tfil)

        self.vl_allhls_tfil.addLayout(self.hl_returnbuttons_tfil)
        self.gridLayout_2.addLayout(self.vl_allhls_tfil, 0, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        TimefilterInputInterface.interface_setup(self)

    def retranslateUi(self, timefilter_dialog):
        _translate = QtCore.QCoreApplication.translate
        timefilter_dialog.setWindowTitle(_translate("timefilter_dialog", "Dialog"))
        self.label_timefiltername_tfil.setText(_translate("timefilter_dialog", "Time Filter Name"))
        self.label_starttime_tfil.setText(_translate("timefilter_dialog", "Start Time"))
        self.label_endtime_tfil.setText(_translate("timefilter_dialog", "End Time"))
        self.button_cancel_tfil.setText(_translate("timefilter_dialog", "Cancel"))
        self.button_ok_tfil.setText(_translate("timefilter_dialog", "Ok"))

