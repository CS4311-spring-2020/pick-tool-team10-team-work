from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from Dialogs.vectorconfig_input_interface import VectorConfigInputInterface


class VectorConfigDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("vectorconfiguration_dialog")
        self.resize(504, 320)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.vl_all_vc = QtWidgets.QVBoxLayout()
        self.vl_all_vc.setObjectName("vl_all_vc")

        self.hl_top_vc = QtWidgets.QHBoxLayout()
        self.hl_top_vc.setObjectName("hl_top_vc")

        self.label_vectorconfiguration_vc = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_vectorconfiguration_vc.sizePolicy().hasHeightForWidth())
        self.label_vectorconfiguration_vc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_vectorconfiguration_vc.setFont(font)
        self.label_vectorconfiguration_vc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_vectorconfiguration_vc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vectorconfiguration_vc.setObjectName("label_vectorconfiguration_vc")
        self.hl_top_vc.addWidget(self.label_vectorconfiguration_vc)

        self.vl_all_vc.addLayout(self.hl_top_vc)

        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vl_all_vc.addItem(spacerItem)

        self.hl_add_vc = QtWidgets.QHBoxLayout()
        self.hl_add_vc.setObjectName("hl_add_vc")

        self.button_addvector_vc = QtWidgets.QPushButton(self)
        self.button_addvector_vc.setAutoDefault(False)
        self.button_addvector_vc.setObjectName("button_addvector_vc")
        self.hl_add_vc.addWidget(self.button_addvector_vc)

        self.lineedit_vectorname_vc = QtWidgets.QLineEdit(self)
        self.lineedit_vectorname_vc.setObjectName("lineedit_vectorname_vc")
        self.hl_add_vc.addWidget(self.lineedit_vectorname_vc)

        self.lineedit_vectordescription_vc = QtWidgets.QLineEdit(self)
        self.lineedit_vectordescription_vc.setObjectName("lineedit_vectordescription_vc")
        self.hl_add_vc.addWidget(self.lineedit_vectordescription_vc)

        self.vl_all_vc.addLayout(self.hl_add_vc)

        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vl_all_vc.addItem(spacerItem3)

        self.hl_confirmcancel_vc = QtWidgets.QHBoxLayout()
        self.hl_confirmcancel_vc.setObjectName("hl_confirmcancel_vc")

        self.button_confirm_vc = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_confirm_vc.sizePolicy().hasHeightForWidth())
        self.button_confirm_vc.setSizePolicy(sizePolicy)
        self.button_confirm_vc.setAutoDefault(False)
        self.button_confirm_vc.setObjectName("button_confirm_vc")
        self.hl_confirmcancel_vc.addWidget(self.button_confirm_vc)

        self.button_cancel_vc = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cancel_vc.sizePolicy().hasHeightForWidth())
        self.button_cancel_vc.setSizePolicy(sizePolicy)
        self.button_cancel_vc.setAutoDefault(False)
        self.button_cancel_vc.setObjectName("button_cancel_vc")
        self.hl_confirmcancel_vc.addWidget(self.button_cancel_vc)

        self.vl_all_vc.addLayout(self.hl_confirmcancel_vc)

        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vl_all_vc.addItem(spacerItem1)

        self.hl_deleteedit_vc = QtWidgets.QHBoxLayout()
        self.hl_deleteedit_vc.setObjectName("hl_deleteedit_vc")

        self.button_deletevector_vc = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_deletevector_vc.sizePolicy().hasHeightForWidth())
        self.button_deletevector_vc.setSizePolicy(sizePolicy)
        self.button_deletevector_vc.setAutoDefault(False)
        self.button_deletevector_vc.setObjectName("button_deletevector_vc")
        self.hl_deleteedit_vc.addWidget(self.button_deletevector_vc)

        self.button_editvector_vc = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_editvector_vc.sizePolicy().hasHeightForWidth())
        self.button_editvector_vc.setSizePolicy(sizePolicy)
        self.button_editvector_vc.setAutoDefault(False)
        self.button_editvector_vc.setObjectName("button_editvector_vc")
        self.hl_deleteedit_vc.addWidget(self.button_editvector_vc)

        self.button_ok_vc = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ok_vc.sizePolicy().hasHeightForWidth())
        self.button_ok_vc.setSizePolicy(sizePolicy)
        self.button_ok_vc.setAutoDefault(False)
        self.button_ok_vc.setObjectName("button_ok_vc")
        self.hl_deleteedit_vc.addWidget(self.button_ok_vc)

        self.vl_all_vc.addLayout(self.hl_deleteedit_vc)

        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vl_all_vc.addItem(spacerItem2)

        self.hl_vectortable_vc = QtWidgets.QHBoxLayout()
        self.hl_vectortable_vc.setObjectName("hl_vectortable_vc")

        self.tablewidget_vectors_vc = QtWidgets.QTableWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.tablewidget_vectors_vc.sizePolicy().hasHeightForWidth())
        self.tablewidget_vectors_vc.setSizePolicy(sizePolicy)
        self.tablewidget_vectors_vc.setObjectName("tablewidget_vectors_vc")
        self.tablewidget_vectors_vc.setColumnCount(4)
        self.tablewidget_vectors_vc.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_vectors_vc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_vectors_vc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_vectors_vc.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_vectors_vc.setHorizontalHeaderItem(3, item)
        self.tablewidget_vectors_vc.horizontalHeader().setDefaultSectionSize(150)
        self.tablewidget_vectors_vc.horizontalHeader().setSortIndicatorShown(True)
        self.tablewidget_vectors_vc.horizontalHeader().setStretchLastSection(True)
        self.tablewidget_vectors_vc.verticalHeader().setVisible(False)
        self.tablewidget_vectors_vc.verticalHeader().setStretchLastSection(True)
        self.hl_vectortable_vc.addWidget(self.tablewidget_vectors_vc)

        self.vl_all_vc.addLayout(self.hl_vectortable_vc)

        self.gridLayout.addLayout(self.vl_all_vc, 0, 0, 1, 1)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        VectorConfigInputInterface.interface_setup(self)

    def retranslateUi(self, vectorconfiguration_dialog):
        _translate = QtCore.QCoreApplication.translate
        vectorconfiguration_dialog.setWindowTitle(_translate("vectorconfiguration_dialog", "Dialog"))
        self.label_vectorconfiguration_vc.setText(_translate("vectorconfiguration_dialog", "Vector Configuration"))
        self.button_addvector_vc.setText(_translate("vectorconfiguration_dialog", "Add Vector"))
        self.lineedit_vectorname_vc.setPlaceholderText(_translate("vectorconfiguration_dialog", "Vector Name"))
        self.lineedit_vectordescription_vc.setPlaceholderText(_translate("vectorconfiguration_dialog", "Vector Description"))
        self.button_deletevector_vc.setText(_translate("vectorconfiguration_dialog", "Delete Vector"))
        self.button_editvector_vc.setText(_translate("vectorconfiguration_dialog", "Edit Vector"))
        self.button_ok_vc.setText(_translate("vectorconfiguration_dialog", "Ok"))
        self.button_confirm_vc.setText(_translate("vectorconfiguration_dialog", "Confirm"))
        self.button_cancel_vc.setText(_translate("vectorconfiguration_dialog", "Cancel"))
        item = self.tablewidget_vectors_vc.horizontalHeaderItem(0)
        item.setText(_translate("vectorconfiguration_dialog", ""))
        item = self.tablewidget_vectors_vc.horizontalHeaderItem(1)
        item.setText(_translate("vectorconfiguration_dialog", "Vector Name"))
        item = self.tablewidget_vectors_vc.horizontalHeaderItem(2)
        item.setText(_translate("vectorconfiguration_dialog", "Vector Description"))
        item = self.tablewidget_vectors_vc.horizontalHeaderItem(3)
        item.setText(_translate("vectorconfiguration_dialog", "ID"))
        self.tablewidget_vectors_vc.setColumnHidden(3, True)