from PyQt5.QtWidgets import QPushButton, QLineEdit, QMessageBox, QTableWidget, QCheckBox, QTableWidgetItem
from PyQt5.QtCore import QDateTime, QModelIndex, Qt
from databse_interface import DatabaseInterface
#from vectorconfig_dialog import VectorConfigDialog
from pymongo.results import InsertOneResult, DeleteResult, InsertManyResult, UpdateResult


class VectorConfigInputInterface:
    #vectorconfig_dialog = VectorConfigDialog()

    vectorconfig_dialog = None
    delete_vectors: list = list()
    use_edit_vector_logic: bool = False

    @staticmethod
    def interface_setup(vectorconfig_dialog):
        VectorConfigInputInterface.vectorconfig_dialog = vectorconfig_dialog
        VectorConfigInputInterface.button_setup()
        VectorConfigInputInterface.refresh_tablewidget_vectors()

    @staticmethod
    def button_setup():
        VectorConfigInputInterface.vectorconfig_dialog.button_addvector_vc.clicked.connect(
            VectorConfigInputInterface.button_addvector_vc_clicked)
        VectorConfigInputInterface.vectorconfig_dialog.button_deletevector_vc.clicked.connect(
            VectorConfigInputInterface.button_deletevector_vc_clicked)
        VectorConfigInputInterface.vectorconfig_dialog.button_editvector_vc.clicked.connect(
            VectorConfigInputInterface.button_editvector_vc_clicked)
        VectorConfigInputInterface.vectorconfig_dialog.button_ok_vc.clicked.connect(
            VectorConfigInputInterface.button_ok_vc_clicked)

    @staticmethod
    def button_addvector_vc_clicked():
        button_addvector: QPushButton = VectorConfigInputInterface.vectorconfig_dialog.button_addvector_vc
        button_addvector.toggle()
        lineedit_vectorname: QLineEdit = VectorConfigInputInterface.vectorconfig_dialog.lineedit_vectorname_vc
        lineedit_vectordescription: QLineEdit = \
            VectorConfigInputInterface.vectorconfig_dialog.lineedit_vectordescription_vc

        lineedit_vectorname_text: str = lineedit_vectorname.text()
        lineedit_vectordescription_text: str = lineedit_vectordescription.text()
        if len(lineedit_vectorname_text) == 0 or len(lineedit_vectordescription_text) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Vector Name and Vector Description cannot be empty!')
            msg.setWindowTitle("Add Vector Error")
            msg.exec_()
            return

        vectors_item = DatabaseInterface.create_vectors_item(name=lineedit_vectorname_text,
                                                             description=lineedit_vectordescription_text)
        DatabaseInterface.insert_one_vectors(vectors_item)
        VectorConfigInputInterface.refresh_tablewidget_vectors()

    @staticmethod
    def button_deletevector_vc_clicked():
        button_deletevector: QPushButton = VectorConfigInputInterface.vectorconfig_dialog.button_deletevector_vc
        button_deletevector.toggle()
        tablewidget_vectors: QTableWidget = VectorConfigInputInterface.vectorconfig_dialog.tablewidget_vectors_vc

        tablewidget_vectors_count = tablewidget_vectors.rowCount()
        for index in range(tablewidget_vectors_count):
            item: QTableWidgetItem = tablewidget_vectors.item(index, 0)
            item_state: Qt.CheckState = item.checkState()
            if item_state == Qt.Checked:
                vector_id: str = tablewidget_vectors.item(index, 3).text()
                VectorConfigInputInterface.delete_vectors.append(vector_id)

        if len(VectorConfigInputInterface.delete_vectors) == 0:
            return

        for vector_id in VectorConfigInputInterface.delete_vectors:
            DatabaseInterface.delete_one_vectors_by_id(vector_id=vector_id)

        VectorConfigInputInterface.delete_vectors.clear()
        VectorConfigInputInterface.refresh_tablewidget_vectors()

    @staticmethod
    def button_editvector_vc_clicked():
        button_editvector: QPushButton = VectorConfigInputInterface.vectorconfig_dialog.button_editvector_vc
        button_editvector.toggle()
        tablewidget_vectors: QTableWidget = VectorConfigInputInterface.vectorconfig_dialog.tablewidget_vectors_vc
        tablewidget_vectors_count = tablewidget_vectors.rowCount()

        counter: int = 0
        for index in range(tablewidget_vectors_count):
            item: QTableWidgetItem = tablewidget_vectors.item(index, 0)
            item_state: Qt.CheckState = item.checkState()
            if item_state == Qt.Checked:
                counter += 1
                vector_id: str = tablewidget_vectors.item(index, 3).text()

        if counter != 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Can only edit 1 Vector at a time!')
            msg.setWindowTitle("Edit Vector Error")
            msg.exec_()
            return

    @staticmethod
    def button_ok_vc_clicked():
        button_ok: QPushButton = VectorConfigInputInterface.vectorconfig_dialog.button_ok_vc
        button_ok.toggle()
        VectorConfigInputInterface.vectorconfig_dialog.accept()

    @staticmethod
    def refresh_tablewidget_vectors():
        tablewidget_vectors: QTableWidget = VectorConfigInputInterface.vectorconfig_dialog.tablewidget_vectors_vc
        tablewidget_vectors.setSortingEnabled(False)
        vectors: list = DatabaseInterface.find_vectors_all()
        tablewidget_vectors.clearContents()

        counter: int = 0
        for vector in vectors:
            vector: dict
            tablewidget_vectors.insertRow(counter)
            checkbox_item = QTableWidgetItem()
            checkbox_item.setCheckState(False)
            vectorname_item = QTableWidgetItem(vector['name'])
            vectorname_item.setFlags(Qt.ItemIsEnabled)
            vectordescription_item = QTableWidgetItem(vector['description'])
            vectordescription_item.setFlags(Qt.ItemIsEnabled)
            vectorid_item = QTableWidgetItem(str(vector['_id']))
            vectorid_item.setFlags(Qt.ItemIsEnabled)
            tablewidget_vectors.setItem(counter, 0, checkbox_item)
            tablewidget_vectors.setItem(counter, 1, vectorname_item)
            tablewidget_vectors.setItem(counter, 2, vectordescription_item)  # log entry timestamp column
            tablewidget_vectors.setItem(counter, 3, vectorid_item)  # log entry event column
            counter += 1

        tablewidget_vectors.setRowCount(len(vectors))
        tablewidget_vectors.setSortingEnabled(True)
