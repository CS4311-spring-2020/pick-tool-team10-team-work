# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_nav.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QStyleFactory, QAbstractItemView, QMainWindow


class Ui_mainwindow_navigation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("mainwindow_navigation")
        self.resize(787, 582)
        self.centralwidget_allwindow_nav = QtWidgets.QWidget(self)
        self.centralwidget_allwindow_nav.setObjectName("centralwidget_allwindow_nav")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget_allwindow_nav)
        self.gridLayout.setObjectName("gridLayout")
        self.vl_allwindow_navi = QtWidgets.QVBoxLayout()
        self.vl_allwindow_navi.setSpacing(0)
        self.vl_allwindow_navi.setObjectName("vl_allwindow_navi")
        self.hl_top_navi = QtWidgets.QHBoxLayout()
        self.hl_top_navi.setObjectName("hl_top_navi")
        self.button_undo_navi = QtWidgets.QPushButton(self.centralwidget_allwindow_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_undo_navi.sizePolicy().hasHeightForWidth())
        self.button_undo_navi.setSizePolicy(sizePolicy)
        self.button_undo_navi.setAutoDefault(False)
        self.button_undo_navi.setObjectName("button_undo_navi")
        self.hl_top_navi.addWidget(self.button_undo_navi)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_top_navi.addItem(spacerItem)
        self.button_redo_navi = QtWidgets.QPushButton(self.centralwidget_allwindow_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_redo_navi.sizePolicy().hasHeightForWidth())
        self.button_redo_navi.setSizePolicy(sizePolicy)
        self.button_redo_navi.setChecked(False)
        self.button_redo_navi.setAutoDefault(False)
        self.button_redo_navi.setObjectName("button_redo_navi")
        self.hl_top_navi.addWidget(self.button_redo_navi)
        self.label_navigation_navi = QtWidgets.QLabel(self.centralwidget_allwindow_nav)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_navigation_navi.setFont(font)
        self.label_navigation_navi.setAlignment(QtCore.Qt.AlignCenter)
        self.label_navigation_navi.setObjectName("label_navigation_navi")
        self.hl_top_navi.addWidget(self.label_navigation_navi)
        self.vl_allwindow_navi.addLayout(self.hl_top_navi)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vl_allwindow_navi.addItem(spacerItem1)
        self.hl_vcandsearch_navi = QtWidgets.QHBoxLayout()
        self.hl_vcandsearch_navi.setObjectName("hl_vcandsearch_navi")
        self.button_push_navi = QtWidgets.QPushButton(self.centralwidget_allwindow_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_push_navi.sizePolicy().hasHeightForWidth())
        self.button_push_navi.setSizePolicy(sizePolicy)
        self.button_push_navi.setAutoDefault(False)
        self.button_push_navi.setObjectName("button_push_navi")
        self.hl_vcandsearch_navi.addWidget(self.button_push_navi)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_vcandsearch_navi.addItem(spacerItem2)
        self.button_pull_navi = QtWidgets.QPushButton(self.centralwidget_allwindow_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pull_navi.sizePolicy().hasHeightForWidth())
        self.button_pull_navi.setSizePolicy(sizePolicy)
        self.button_pull_navi.setAutoDefault(False)
        self.button_pull_navi.setObjectName("button_pull_navi")
        self.hl_vcandsearch_navi.addWidget(self.button_pull_navi)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_vcandsearch_navi.addItem(spacerItem3)
        self.linedit_regex_navi = QtWidgets.QLineEdit(self.centralwidget_allwindow_nav)
        self.linedit_regex_navi.setObjectName("linedit_regex_navi")
        self.hl_vcandsearch_navi.addWidget(self.linedit_regex_navi)
        spacerItem4 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_vcandsearch_navi.addItem(spacerItem4)
        self.button_vectortableview_navi = QtWidgets.QPushButton(self.centralwidget_allwindow_nav)
        self.button_vectortableview_navi.setObjectName("button_vectortableview_navi")
        self.hl_vcandsearch_navi.addWidget(self.button_vectortableview_navi)
        self.vl_allwindow_navi.addLayout(self.hl_vcandsearch_navi)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vl_allwindow_navi.addItem(spacerItem5)
        self.hl_bottom_navi = QtWidgets.QHBoxLayout()
        self.hl_bottom_navi.setObjectName("hl_bottom_navi")
        self.scrollarea01_hl_bottom_navi = QtWidgets.QScrollArea(self.centralwidget_allwindow_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollarea01_hl_bottom_navi.sizePolicy().hasHeightForWidth())
        self.scrollarea01_hl_bottom_navi.setSizePolicy(sizePolicy)
        self.scrollarea01_hl_bottom_navi.setMinimumSize(QtCore.QSize(200, 0))
        self.scrollarea01_hl_bottom_navi.setWidgetResizable(True)
        self.scrollarea01_hl_bottom_navi.setObjectName("scrollarea01_hl_bottom_navi")
        self.scrollareacontentwidgets_hl_bottom_navi = QtWidgets.QWidget()
        self.scrollareacontentwidgets_hl_bottom_navi.setGeometry(QtCore.QRect(0, 0, 209, 773))
        self.scrollareacontentwidgets_hl_bottom_navi.setObjectName("scrollareacontentwidgets_hl_bottom_navi")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollareacontentwidgets_hl_bottom_navi)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.vl_allfilters_navi = QtWidgets.QVBoxLayout()
        self.vl_allfilters_navi.setObjectName("vl_allfilters_navi")
        self.vl_locationfilter_navi = QtWidgets.QVBoxLayout()
        self.vl_locationfilter_navi.setObjectName("vl_locationfilter_navi")
        self.label_location_navi = QtWidgets.QLabel(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_location_navi.sizePolicy().hasHeightForWidth())
        self.label_location_navi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_location_navi.setFont(font)
        self.label_location_navi.setObjectName("label_location_navi")
        self.vl_locationfilter_navi.addWidget(self.label_location_navi)
        self.listview_location_navi = QtWidgets.QListView(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listview_location_navi.sizePolicy().hasHeightForWidth())
        self.listview_location_navi.setSizePolicy(sizePolicy)
        self.listview_location_navi.setMinimumSize(QtCore.QSize(0, 75))
        self.listview_location_navi.setObjectName("listview_location_navi")

        self.listview_location_navi.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.model = QStandardItemModel()
        self.model.itemChanged.connect(self.set_items)
        for n in range(10):
            item = QStandardItem('Item %s' % n)
            item.setCheckable(True)
            item.setEditable(True)
            self.model.appendRow(item)
        self.listview_location_navi.setModel(self.model)


        self.vl_locationfilter_navi.addWidget(self.listview_location_navi)
        self.vl_allfilters_navi.addLayout(self.vl_locationfilter_navi)
        self.line05_hl_bottom_navi = QtWidgets.QFrame(self.scrollareacontentwidgets_hl_bottom_navi)
        self.line05_hl_bottom_navi.setFrameShape(QtWidgets.QFrame.HLine)
        self.line05_hl_bottom_navi.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line05_hl_bottom_navi.setObjectName("line05_hl_bottom_navi")
        self.vl_allfilters_navi.addWidget(self.line05_hl_bottom_navi)
        self.vl_showhidefilter_navi = QtWidgets.QVBoxLayout()
        self.vl_showhidefilter_navi.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vl_showhidefilter_navi.setSpacing(6)
        self.vl_showhidefilter_navi.setObjectName("vl_showhidefilter_navi")
        self.label_showhide_navi = QtWidgets.QLabel(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_showhide_navi.sizePolicy().hasHeightForWidth())
        self.label_showhide_navi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_showhide_navi.setFont(font)
        self.label_showhide_navi.setObjectName("label_showhide_navi")
        self.vl_showhidefilter_navi.addWidget(self.label_showhide_navi)
        self.checkbox_listnumber_navi = QtWidgets.QCheckBox(self.scrollareacontentwidgets_hl_bottom_navi)
        self.checkbox_listnumber_navi.setObjectName("checkbox_listnumber_navi")
        self.vl_showhidefilter_navi.addWidget(self.checkbox_listnumber_navi)
        self.checkbox_timestamp_navi = QtWidgets.QCheckBox(self.scrollareacontentwidgets_hl_bottom_navi)
        self.checkbox_timestamp_navi.setObjectName("checkbox_timestamp_navi")
        self.vl_showhidefilter_navi.addWidget(self.checkbox_timestamp_navi)
        self.checkbox_event_navi = QtWidgets.QCheckBox(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_event_navi.sizePolicy().hasHeightForWidth())
        self.checkbox_event_navi.setSizePolicy(sizePolicy)
        self.checkbox_event_navi.setObjectName("checkbox_event_navi")
        self.vl_showhidefilter_navi.addWidget(self.checkbox_event_navi)
        self.checkbox_vector_navi = QtWidgets.QCheckBox(self.scrollareacontentwidgets_hl_bottom_navi)
        self.checkbox_vector_navi.setObjectName("checkbox_vector_navi")
        self.vl_showhidefilter_navi.addWidget(self.checkbox_vector_navi)
        self.vl_allfilters_navi.addLayout(self.vl_showhidefilter_navi)
        self.line01_hl_bottom_navi = QtWidgets.QFrame(self.scrollareacontentwidgets_hl_bottom_navi)
        self.line01_hl_bottom_navi.setFrameShape(QtWidgets.QFrame.HLine)
        self.line01_hl_bottom_navi.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line01_hl_bottom_navi.setObjectName("line01_hl_bottom_navi")
        self.vl_allfilters_navi.addWidget(self.line01_hl_bottom_navi)
        self.vl_timefilter_navi = QtWidgets.QVBoxLayout()
        self.vl_timefilter_navi.setObjectName("vl_timefilter_navi")
        self.label_time_navi = QtWidgets.QLabel(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_time_navi.sizePolicy().hasHeightForWidth())
        self.label_time_navi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_navi.setFont(font)
        self.label_time_navi.setObjectName("label_time_navi")
        self.vl_timefilter_navi.addWidget(self.label_time_navi)
        self.hl_timefilter_starttime_navi = QtWidgets.QHBoxLayout()
        self.hl_timefilter_starttime_navi.setObjectName("hl_timefilter_starttime_navi")
        self.label_starttime_navi = QtWidgets.QLabel(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_starttime_navi.sizePolicy().hasHeightForWidth())
        self.label_starttime_navi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_starttime_navi.setFont(font)
        self.label_starttime_navi.setObjectName("label_starttime_navi")
        self.hl_timefilter_starttime_navi.addWidget(self.label_starttime_navi)
        self.datetimeedit_starttime_navi = QtWidgets.QDateTimeEdit(self.scrollareacontentwidgets_hl_bottom_navi)
        self.datetimeedit_starttime_navi.setObjectName("datetimeedit_starttime_navi")
        self.hl_timefilter_starttime_navi.addWidget(self.datetimeedit_starttime_navi)
        self.vl_timefilter_navi.addLayout(self.hl_timefilter_starttime_navi)
        self.hl_timefilter_endtime_navi = QtWidgets.QHBoxLayout()
        self.hl_timefilter_endtime_navi.setObjectName("hl_timefilter_endtime_navi")
        self.label_endtime_navi = QtWidgets.QLabel(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_endtime_navi.sizePolicy().hasHeightForWidth())
        self.label_endtime_navi.setSizePolicy(sizePolicy)
        self.label_endtime_navi.setObjectName("label_endtime_navi")
        self.hl_timefilter_endtime_navi.addWidget(self.label_endtime_navi)
        self.datetimeedit_endtime_navi = QtWidgets.QDateTimeEdit(self.scrollareacontentwidgets_hl_bottom_navi)
        self.datetimeedit_endtime_navi.setObjectName("datetimeedit_endtime_navi")
        self.hl_timefilter_endtime_navi.addWidget(self.datetimeedit_endtime_navi)
        self.vl_timefilter_navi.addLayout(self.hl_timefilter_endtime_navi)
        self.button_timefilter_navi = QtWidgets.QPushButton(self.scrollareacontentwidgets_hl_bottom_navi)
        self.button_timefilter_navi.setObjectName("button_timefilter_navi")
        self.vl_timefilter_navi.addWidget(self.button_timefilter_navi)
        self.listview_timefilter_navi = QtWidgets.QListView(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listview_timefilter_navi.sizePolicy().hasHeightForWidth())
        self.listview_timefilter_navi.setSizePolicy(sizePolicy)
        self.listview_timefilter_navi.setMinimumSize(QtCore.QSize(0, 75))
        self.listview_timefilter_navi.setObjectName("listview_timefilter_navi")
        self.vl_timefilter_navi.addWidget(self.listview_timefilter_navi)
        self.vl_allfilters_navi.addLayout(self.vl_timefilter_navi)
        self.line02_hl_bottom_navi = QtWidgets.QFrame(self.scrollareacontentwidgets_hl_bottom_navi)
        self.line02_hl_bottom_navi.setFrameShape(QtWidgets.QFrame.HLine)
        self.line02_hl_bottom_navi.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line02_hl_bottom_navi.setObjectName("line02_hl_bottom_navi")
        self.vl_allfilters_navi.addWidget(self.line02_hl_bottom_navi)
        self.vl_significantfilter_navi = QtWidgets.QVBoxLayout()
        self.vl_significantfilter_navi.setObjectName("vl_significantfilter_navi")
        self.checkbox_significant_navi = QtWidgets.QCheckBox(self.scrollareacontentwidgets_hl_bottom_navi)
        self.checkbox_significant_navi.setObjectName("checkbox_significant_navi")
        self.vl_significantfilter_navi.addWidget(self.checkbox_significant_navi)
        self.vl_allfilters_navi.addLayout(self.vl_significantfilter_navi)
        self.line03_hl_bottom_navi = QtWidgets.QFrame(self.scrollareacontentwidgets_hl_bottom_navi)
        self.line03_hl_bottom_navi.setFrameShape(QtWidgets.QFrame.HLine)
        self.line03_hl_bottom_navi.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line03_hl_bottom_navi.setObjectName("line03_hl_bottom_navi")
        self.vl_allfilters_navi.addWidget(self.line03_hl_bottom_navi)
        self.vl_teamfilter_navi = QtWidgets.QVBoxLayout()
        self.vl_teamfilter_navi.setObjectName("vl_teamfilter_navi")
        self.label_team_navi = QtWidgets.QLabel(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_team_navi.sizePolicy().hasHeightForWidth())
        self.label_team_navi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_team_navi.setFont(font)
        self.label_team_navi.setObjectName("label_team_navi")
        self.vl_teamfilter_navi.addWidget(self.label_team_navi)
        self.checkbox_red_navi = QtWidgets.QCheckBox(self.scrollareacontentwidgets_hl_bottom_navi)
        self.checkbox_red_navi.setObjectName("checkbox_red_navi")
        self.vl_teamfilter_navi.addWidget(self.checkbox_red_navi)
        self.checkbox_blue_navi = QtWidgets.QCheckBox(self.scrollareacontentwidgets_hl_bottom_navi)
        self.checkbox_blue_navi.setObjectName("checkbox_blue_navi")
        self.vl_teamfilter_navi.addWidget(self.checkbox_blue_navi)
        self.checkbox_white_navi = QtWidgets.QCheckBox(self.scrollareacontentwidgets_hl_bottom_navi)
        self.checkbox_white_navi.setObjectName("checkbox_white_navi")
        self.vl_teamfilter_navi.addWidget(self.checkbox_white_navi)
        self.vl_allfilters_navi.addLayout(self.vl_teamfilter_navi)
        self.line04_hl_bottom_navi = QtWidgets.QFrame(self.scrollareacontentwidgets_hl_bottom_navi)
        self.line04_hl_bottom_navi.setFrameShape(QtWidgets.QFrame.HLine)
        self.line04_hl_bottom_navi.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line04_hl_bottom_navi.setObjectName("line04_hl_bottom_navi")
        self.vl_allfilters_navi.addWidget(self.line04_hl_bottom_navi)
        self.vl_vectorsfilter_navi = QtWidgets.QVBoxLayout()
        self.vl_vectorsfilter_navi.setObjectName("vl_vectorsfilter_navi")
        self.label_vectors_navi = QtWidgets.QLabel(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_vectors_navi.sizePolicy().hasHeightForWidth())
        self.label_vectors_navi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_vectors_navi.setFont(font)
        self.label_vectors_navi.setObjectName("label_vectors_navi")
        self.vl_vectorsfilter_navi.addWidget(self.label_vectors_navi)
        self.listview_vectors_navi = QtWidgets.QListView(self.scrollareacontentwidgets_hl_bottom_navi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listview_vectors_navi.sizePolicy().hasHeightForWidth())
        self.listview_vectors_navi.setSizePolicy(sizePolicy)
        self.listview_vectors_navi.setMinimumSize(QtCore.QSize(0, 75))
        self.listview_vectors_navi.setObjectName("listview_vectors_navi")
        self.vl_vectorsfilter_navi.addWidget(self.listview_vectors_navi)
        self.vl_allfilters_navi.addLayout(self.vl_vectorsfilter_navi)
        self.gridLayout_8.addLayout(self.vl_allfilters_navi, 0, 0, 1, 1)
        self.scrollarea01_hl_bottom_navi.setWidget(self.scrollareacontentwidgets_hl_bottom_navi)
        self.hl_bottom_navi.addWidget(self.scrollarea01_hl_bottom_navi)
        spacerItem6 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hl_bottom_navi.addItem(spacerItem6)
        self.tablewidget_navi = QtWidgets.QTableWidget(self.centralwidget_allwindow_nav)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablewidget_navi.sizePolicy().hasHeightForWidth())
        self.tablewidget_navi.setSizePolicy(sizePolicy)
        self.tablewidget_navi.setObjectName("tablewidget_navi")
        self.tablewidget_navi.setColumnCount(4)
        self.tablewidget_navi.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_navi.setHorizontalHeaderItem(3, item)
        self.tablewidget_navi.horizontalHeader().setVisible(True)
        self.tablewidget_navi.horizontalHeader().setCascadingSectionResizes(False)
        self.tablewidget_navi.horizontalHeader().setDefaultSectionSize(150)
        self.tablewidget_navi.horizontalHeader().setHighlightSections(True)
        self.tablewidget_navi.horizontalHeader().setSortIndicatorShown(True)
        self.tablewidget_navi.horizontalHeader().setStretchLastSection(True)
        self.tablewidget_navi.verticalHeader().setVisible(False)
        self.tablewidget_navi.verticalHeader().setHighlightSections(True)
        self.tablewidget_navi.verticalHeader().setSortIndicatorShown(True)
        self.tablewidget_navi.verticalHeader().setStretchLastSection(True)
        self.hl_bottom_navi.addWidget(self.tablewidget_navi)
        self.vl_allwindow_navi.addLayout(self.hl_bottom_navi)
        self.gridLayout.addLayout(self.vl_allwindow_navi, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget_allwindow_nav)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, mainwindow_navigation):
        _translate = QtCore.QCoreApplication.translate
        mainwindow_navigation.setWindowTitle(_translate("mainwindow_navigation", "Navigation"))
        self.button_undo_navi.setText(_translate("mainwindow_navigation", "Undo"))
        self.button_redo_navi.setText(_translate("mainwindow_navigation", "Redo"))
        self.label_navigation_navi.setText(_translate("mainwindow_navigation", "Navigation"))
        self.button_push_navi.setText(_translate("mainwindow_navigation", "Push"))
        self.button_pull_navi.setText(_translate("mainwindow_navigation", "Pull"))
        self.button_vectortableview_navi.setText(_translate("mainwindow_navigation", "Vector Table View"))
        self.label_location_navi.setText(_translate("mainwindow_navigation", "Location"))
        self.label_showhide_navi.setText(_translate("mainwindow_navigation", "Show/Hide"))
        self.checkbox_listnumber_navi.setText(_translate("mainwindow_navigation", "List Number"))
        self.checkbox_timestamp_navi.setText(_translate("mainwindow_navigation", "Log Entry Timestamp"))
        self.checkbox_event_navi.setText(_translate("mainwindow_navigation", "Log Entry Event"))
        self.checkbox_vector_navi.setText(_translate("mainwindow_navigation", "Vector"))
        self.label_time_navi.setText(_translate("mainwindow_navigation", "Time"))
        self.label_starttime_navi.setText(_translate("mainwindow_navigation", "Start Time"))
        self.label_endtime_navi.setText(_translate("mainwindow_navigation", "End Time"))
        self.button_timefilter_navi.setText(_translate("mainwindow_navigation", "+ add time filter +"))
        self.checkbox_significant_navi.setText(_translate("mainwindow_navigation", "Significant"))
        self.label_team_navi.setText(_translate("mainwindow_navigation", "Team"))
        self.checkbox_red_navi.setText(_translate("mainwindow_navigation", "Red"))
        self.checkbox_blue_navi.setText(_translate("mainwindow_navigation", "Blue"))
        self.checkbox_white_navi.setText(_translate("mainwindow_navigation", "White"))
        self.label_vectors_navi.setText(_translate("mainwindow_navigation", "Vectors"))
        item = self.tablewidget_navi.verticalHeaderItem(0)
        item.setText(_translate("mainwindow_navigation", "01"))
        item = self.tablewidget_navi.verticalHeaderItem(1)
        item.setText(_translate("mainwindow_navigation", "02"))
        item = self.tablewidget_navi.verticalHeaderItem(2)
        item.setText(_translate("mainwindow_navigation", "03"))
        item = self.tablewidget_navi.verticalHeaderItem(3)
        item.setText(_translate("mainwindow_navigation", "04"))
        item = self.tablewidget_navi.verticalHeaderItem(4)
        item.setText(_translate("mainwindow_navigation", "05"))
        item = self.tablewidget_navi.verticalHeaderItem(5)
        item.setText(_translate("mainwindow_navigation", "06"))
        item = self.tablewidget_navi.verticalHeaderItem(6)
        item.setText(_translate("mainwindow_navigation", "07"))
        item = self.tablewidget_navi.verticalHeaderItem(7)
        item.setText(_translate("mainwindow_navigation", "08"))
        item = self.tablewidget_navi.verticalHeaderItem(8)
        item.setText(_translate("mainwindow_navigation", "09"))
        item = self.tablewidget_navi.verticalHeaderItem(9)
        item.setText(_translate("mainwindow_navigation", "10"))
        item = self.tablewidget_navi.verticalHeaderItem(10)
        item.setText(_translate("mainwindow_navigation", "11"))
        item = self.tablewidget_navi.verticalHeaderItem(11)
        item.setText(_translate("mainwindow_navigation", "12"))
        item = self.tablewidget_navi.verticalHeaderItem(12)
        item.setText(_translate("mainwindow_navigation", "13"))
        item = self.tablewidget_navi.verticalHeaderItem(13)
        item.setText(_translate("mainwindow_navigation", "14"))
        item = self.tablewidget_navi.verticalHeaderItem(14)
        item.setText(_translate("mainwindow_navigation", "15"))
        item = self.tablewidget_navi.verticalHeaderItem(15)
        item.setText(_translate("mainwindow_navigation", "16"))
        item = self.tablewidget_navi.horizontalHeaderItem(0)
        item.setText(_translate("mainwindow_navigation", "List Number"))
        item = self.tablewidget_navi.horizontalHeaderItem(1)
        item.setText(_translate("mainwindow_navigation", "Log Entry Timestamp"))
        item = self.tablewidget_navi.horizontalHeaderItem(2)
        item.setText(_translate("mainwindow_navigation", "Log Entry Event"))
        item = self.tablewidget_navi.horizontalHeaderItem(3)
        item.setText(_translate("mainwindow_navigation", "Vector"))


    def set_items(self, item):
        print(item.text() + " " + str(item.checkState()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app.setStyle(QStyleFactory.create('Fusion'))
    ui = Ui_mainwindow_navigation()
    ui.show()
    sys.exit(app.exec_())
