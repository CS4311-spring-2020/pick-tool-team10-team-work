from PyQt5.QtCore import QDateTime, QModelIndex, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QCheckBox, QMessageBox, QListView, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, \
    QComboBox
from Database.databse_interface import DatabaseInterface
from Dialogs.timefilter_dialog import TimefilterDialog
from Windows.mainwindow_vectortableview import Ui_mainwindow_vectortableview
from Windows.nav_interface_style import UiStyle
#from Windows.nav_mainwindow import NavMainWindow
from Dialogs.vectorconfig_dialog import VectorConfigDialog


class NavInputInterface:
    #nav_mainwindow: NavMainWindow
    nav_mainwindow: None
    static_checkboxes = list()
    log_entries_conditions = list()
    log_entries_regex = ''
    set_enable_flag: bool = False

    @staticmethod
    def interface_setup(nav_mainwindow):
        NavInputInterface.nav_mainwindow = nav_mainwindow
        NavInputInterface.checkbox_setup()
        NavInputInterface.button_setup()
        NavInputInterface.listview_setup()
        NavInputInterface.refresh_logentries_table(search_type='condition')

    @staticmethod
    def checkbox_setup():
        # apply filter
        NavInputInterface.nav_mainwindow.checkbox_applyfilter_navi.clicked.connect(
            NavInputInterface.checkbox_applyfilter_navi_clicked)

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
        NavInputInterface.static_checkboxes.append(NavInputInterface.nav_mainwindow.checkbox_significant_navi)

        # creator checkboxes
        NavInputInterface.nav_mainwindow.checkbox_creator_blue_navi.clicked.connect(
            NavInputInterface.checkbox_creator_blue_navi_clicked)
        NavInputInterface.static_checkboxes.append(NavInputInterface.nav_mainwindow.checkbox_creator_blue_navi)
        NavInputInterface.nav_mainwindow.checkbox_creator_red_navi.clicked.connect(
            NavInputInterface.checkbox_creator_red_navi_clicked)
        NavInputInterface.static_checkboxes.append(NavInputInterface.nav_mainwindow.checkbox_creator_red_navi)
        NavInputInterface.nav_mainwindow.checkbox_creator_white_navi.clicked.connect(
            NavInputInterface.checkbox_creator_white_navi_clicked)
        NavInputInterface.static_checkboxes.append(NavInputInterface.nav_mainwindow.checkbox_creator_white_navi)

        # event type checkboxes
        NavInputInterface.nav_mainwindow.checkbox_eventtype_blue_navi.clicked.connect(
            NavInputInterface.checkbox_eventtype_blue_navi_clicked)
        NavInputInterface.static_checkboxes.append(NavInputInterface.nav_mainwindow.checkbox_eventtype_blue_navi)
        NavInputInterface.nav_mainwindow.checkbox_eventtype_red_navi.clicked.connect(
            NavInputInterface.checkbox_eventtype_red_navi_clicked)
        NavInputInterface.static_checkboxes.append(NavInputInterface.nav_mainwindow.checkbox_eventtype_red_navi)
        NavInputInterface.nav_mainwindow.checkbox_eventtype_white_navi.clicked.connect(
            NavInputInterface.checkbox_eventtype_white_navi_clicked)
        NavInputInterface.static_checkboxes.append(NavInputInterface.nav_mainwindow.checkbox_eventtype_white_navi)

    @staticmethod
    def button_setup():
        # undo and redo buttons
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

        # push and pull buttons
        NavInputInterface.nav_mainwindow.button_push_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_push_navi.clicked.connect(
            NavInputInterface.button_push_navi_clicked)
        NavInputInterface.nav_mainwindow.button_pull_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_pull_navi.clicked.connect(
            NavInputInterface.button_pull_navi_clicked)

        # regex search button
        NavInputInterface.nav_mainwindow.button_search_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_search_navi.clicked.connect(
            NavInputInterface.button_search_navi_clicked)

        # node table view button
        NavInputInterface.nav_mainwindow.button_vectortableview_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_vectortableview_navi.clicked.connect(
            NavInputInterface.button_vectortableview_navi_clicked)

        # vector configuration button
        NavInputInterface.nav_mainwindow.button_vectorconfig_navi.setCheckable(True)
        NavInputInterface.nav_mainwindow.button_vectorconfig_navi.clicked.connect(
            NavInputInterface.button_vectorconfig_navi_clicked)

    @staticmethod
    def listview_setup():
        model = QStandardItemModel()
        model.itemChanged.connect(NavInputInterface.listview_location_navi_item_change)
        NavInputInterface.nav_mainwindow.listview_location_navi.setModel(model)
        NavInputInterface.refresh_listview_locations_navi()

        NavInputInterface.nav_mainwindow.listview_timefilter_navi.doubleClicked.connect(
            NavInputInterface.listview_timefilter_navi_doubleclicked)
        model = QStandardItemModel()
        model.itemChanged.connect(NavInputInterface.listview_timefilter_navi_item_change)
        NavInputInterface.nav_mainwindow.listview_timefilter_navi.setModel(model)
        NavInputInterface.refresh_listview_timefilters_navi()

        model = QStandardItemModel()
        model.itemChanged.connect(NavInputInterface.listview_vectors_navi_item_change)
        NavInputInterface.nav_mainwindow.listview_vectors_navi.setModel(model)
        NavInputInterface.refresh_listview_vectors_navi()

    @staticmethod
    def listview_timefilter_navi_doubleclicked(index: QModelIndex):
        timefilter_listitem: QStandardItem = index.model().itemFromIndex(index)
        timefilter_item: dict = DatabaseInterface.find_one_time_filters_by_id(timefilter_listitem.time_filter_id)
        timefilter_dialog = TimefilterDialog(str(timefilter_item['_id']))
        timefilter_dialog.exec()
        NavInputInterface.refresh_listview_timefilters_navi()

    @staticmethod  # COMPLETE
    def listview_location_navi_item_change(item: QStandardItem):
        if NavInputInterface.set_enable_flag is True:
            return
        location: str = item.text()
        condition: dict = {'location': location}
        item_state: Qt.CheckState = item.checkState()
        if item_state == Qt.Checked:
            NavInputInterface.log_entries_conditions.append(condition)
        elif item_state == Qt.Unchecked:
            NavInputInterface.log_entries_conditions.remove(condition)

    @staticmethod
    def listview_timefilter_navi_item_change(item):
        print(item.text() + " " + str(item.checkState()))

    @staticmethod  # COMPLETE
    def listview_vectors_navi_item_change(item: QStandardItem):
        if NavInputInterface.set_enable_flag is True:
            return
        vector: str = item.text()
        condition: dict = {'vector': vector}
        item_state: Qt.CheckState = item.checkState()
        if item_state == Qt.Checked:  # checked state
            NavInputInterface.log_entries_conditions.append(condition)
        elif item_state == Qt.Unchecked:  # unchecked state
            NavInputInterface.log_entries_conditions.remove(condition)

    @staticmethod
    def checkbox_applyfilter_navi_clicked():
        checkbox_applyfilter: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_applyfilter_navi
        checkbox_applyfilter_state: bool = checkbox_applyfilter.isChecked()
        if checkbox_applyfilter_state is True:  # checked state
            checkbox_applyfilter.setPalette(UiStyle.checkbox_palettes['dark_green'])
            NavInputInterface.set_enable_flag = True
            NavInputInterface.set_enable_filter_checkboxes(False)
            NavInputInterface.refresh_logentries_table(search_type='condition')
        elif checkbox_applyfilter_state is False:  # unchecked state
            checkbox_applyfilter.setPalette(UiStyle.checkbox_palettes['black'])
            NavInputInterface.set_enable_filter_checkboxes(True)
            NavInputInterface.set_enable_flag = False
            NavInputInterface.refresh_logentries_table()

    @staticmethod  # COMPLETE
    def checkbox_listnumber_navi_clicked():
        checkbox_listnumber: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_listnumber_navi
        checkbox_listnumber_state: bool = checkbox_listnumber.isChecked()
        if checkbox_listnumber_state is True:  # checked state
            NavInputInterface.hide_logentries_column(column=1, hide=True)
            checkbox_listnumber.setPalette(UiStyle.checkbox_palettes['dark_grey'])
        elif checkbox_listnumber_state is False:  # unchecked state
            NavInputInterface.hide_logentries_column(column=1, hide=False)
            checkbox_listnumber.setPalette(UiStyle.checkbox_palettes['black'])

    @staticmethod  # COMPLETE
    def checkbox_timestamp_navi_clicked():
        checkbox_timestamp: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_timestamp_navi
        checkbox_timestamp_state: bool = checkbox_timestamp.isChecked()
        if checkbox_timestamp_state is True:  # checked state
            NavInputInterface.hide_logentries_column(column=2, hide=True)
            checkbox_timestamp.setPalette(UiStyle.checkbox_palettes['dark_grey'])
        elif checkbox_timestamp_state is False:  # unchecked state
            NavInputInterface.hide_logentries_column(column=2, hide=False)
            checkbox_timestamp.setPalette(UiStyle.checkbox_palettes['black'])

    @staticmethod  # COMPLETE
    def checkbox_event_navi_clicked():
        checkbox_event: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_event_navi
        checkbox_event_state: bool = checkbox_event.isChecked()
        if checkbox_event_state is True:  # checked state
            NavInputInterface.hide_logentries_column(column=3, hide=True)
            checkbox_event.setPalette(UiStyle.checkbox_palettes['dark_grey'])
        elif checkbox_event_state is False:  # unchecked state
            NavInputInterface.hide_logentries_column(column=3, hide=False)
            checkbox_event.setPalette(UiStyle.checkbox_palettes['black'])

    @staticmethod  # COMPLETE
    def checkbox_vector_navi_clicked():
        checkbox_vector: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_vector_navi
        checkbox_vector_state: bool = checkbox_vector.isChecked()
        if checkbox_vector_state is True:  # checked state
            NavInputInterface.hide_logentries_column(column=4, hide=True)
            checkbox_vector.setPalette(UiStyle.checkbox_palettes['dark_grey'])
        elif checkbox_vector_state is False:  # unchecked state
            NavInputInterface.hide_logentries_column(column=4, hide=False)
            checkbox_vector.setPalette(UiStyle.checkbox_palettes['black'])

    @staticmethod
    def checkbox_significant_navi_clicked():
        checkbox_significant: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_significant_navi
        checkbox_significant_state: bool = checkbox_significant.isChecked()
        if checkbox_significant_state is True:  # checked state
            print('Checked State')
        elif checkbox_significant_state is False:  # unchecked state
            print('Unchecked State')

    @staticmethod  # COMPLETE
    def checkbox_creator_blue_navi_clicked():
        checkbox_blue: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_creator_blue_navi
        checkbox_blue_state: bool = checkbox_blue.isChecked()
        condition: dict = {'creator': 'blue'}
        if checkbox_blue_state is True:  # checked state
            NavInputInterface.log_entries_conditions.append(condition)
        elif checkbox_blue_state is False:  # unchecked state
            NavInputInterface.log_entries_conditions.remove(condition)

    @staticmethod  # COMPLETE
    def checkbox_creator_red_navi_clicked():
        checkbox_red: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_creator_red_navi
        checkbox_red_state: bool = checkbox_red.isChecked()
        condition: dict = {'creator': 'red'}
        if checkbox_red_state is True:  # checked state
            NavInputInterface.log_entries_conditions.append(condition)
        elif checkbox_red_state is False:  # unchecked state
            NavInputInterface.log_entries_conditions.remove(condition)

    @staticmethod  # COMPLETE
    def checkbox_creator_white_navi_clicked():
        checkbox_white: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_creator_white_navi
        checkbox_white_state: bool = checkbox_white.isChecked()
        condition: dict = {'creator': 'white'}
        if checkbox_white_state is True:  # checked state
            NavInputInterface.log_entries_conditions.append(condition)
        elif checkbox_white_state is False:  # unchecked state
            NavInputInterface.log_entries_conditions.remove(condition)

    @staticmethod  # COMPLETE
    def checkbox_eventtype_blue_navi_clicked():
        checkbox_blue: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_eventtype_blue_navi
        checkbox_blue_state: bool = checkbox_blue.isChecked()
        condition: dict = {'eventtype': 'blue'}
        if checkbox_blue_state is True:  # checked state
            NavInputInterface.log_entries_conditions.append(condition)
        elif checkbox_blue_state is False:  # unchecked state
            NavInputInterface.log_entries_conditions.remove(condition)

    @staticmethod  # COMPLETE
    def checkbox_eventtype_red_navi_clicked():
        checkbox_red: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_eventtype_red_navi
        checkbox_red_state: bool = checkbox_red.isChecked()
        condition: dict = {'eventtype': 'red'}
        if checkbox_red_state is True:  # checked state
            NavInputInterface.log_entries_conditions.append(condition)
        elif checkbox_red_state is False:  # unchecked state
            NavInputInterface.log_entries_conditions.remove(condition)

    @staticmethod  # COMPLETE
    def checkbox_eventtype_white_navi_clicked():
        checkbox_white: QCheckBox = NavInputInterface.nav_mainwindow.checkbox_eventtype_white_navi
        checkbox_white_state: bool = checkbox_white.isChecked()
        condition: dict = {'eventtype': 'white'}
        if checkbox_white_state is True:  # checked state
            NavInputInterface.log_entries_conditions.append(condition)
        elif checkbox_white_state is False:  # unchecked state
            NavInputInterface.log_entries_conditions.remove(condition)

    # Not implemented
    @staticmethod
    def button_undo_navi_clicked():
        button_undo: QPushButton = NavInputInterface.nav_mainwindow.button_undo_navi
        print(button_undo.text() + ' clicked')
        button_undo.toggle()

    # Not implemented
    @staticmethod
    def button_redo_navi_clicked():
        button_redo: QPushButton = NavInputInterface.nav_mainwindow.button_redo_navi
        print(button_redo.text() + ' clicked')
        button_redo.toggle()

    # Not implemented
    @staticmethod
    def button_push_navi_clicked():
        button_push: QPushButton = NavInputInterface.nav_mainwindow.button_push_navi
        print(button_push.text() + ' clicked')
        button_push.toggle()

    # Not implemented
    @staticmethod
    def button_pull_navi_clicked():
        button_pull: QPushButton = NavInputInterface.nav_mainwindow.button_pull_navi
        print(button_pull.text() + ' clicked')
        button_pull.toggle()

    @staticmethod
    def button_search_navi_clicked():
        button_search: QPushButton = NavInputInterface.nav_mainwindow.button_search_navi
        regex_search_lineedit: QLineEdit = NavInputInterface.nav_mainwindow.linedit_regex_navi
        NavInputInterface.log_entries_regex = regex_search_lineedit.text()
        button_search.toggle()
        NavInputInterface.refresh_logentries_table(search_type='regex')

    @staticmethod
    def button_timefilter_navi_clicked():
        button_timefilter: QPushButton = NavInputInterface.nav_mainwindow.button_timefilter_navi
        print(button_timefilter.text() + ' clicked')
        button_timefilter.toggle()
        start_datetime: QDateTime = NavInputInterface.nav_mainwindow.datetimeedit_starttime_navi.dateTime()
        end_datetime: QDateTime = NavInputInterface.nav_mainwindow.datetimeedit_endtime_navi.dateTime()
        start_datetime_info: str = start_datetime.toString('yyyyMMddhhmmss')
        end_datetime_info: str = end_datetime.toString('yyyyMMddhhmmss')
        if NavInputInterface.check_datetimes_values(int(start_datetime_info), int(end_datetime_info)) is False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('End time must be greater than start time.')
            msg.setWindowTitle("Time Filter Error")
            msg.exec_()
            return
        time_filters_item = DatabaseInterface.create_time_filters_item(name='user_time_filter',
                                                                       starttime=start_datetime_info,
                                                                       endtime=end_datetime_info)
        DatabaseInterface.insert_one_time_filters(time_filters_item)
        NavInputInterface.refresh_listview_timefilters_navi()

    @staticmethod
    def button_vectorconfig_navi_clicked():
        button_vectorconfig: QPushButton = NavInputInterface.nav_mainwindow.button_vectorconfig_navi
        button_vectorconfig.toggle()
        vectorconfig_dialog = VectorConfigDialog()
        vectorconfig_dialog.exec()
        NavInputInterface.refresh_listview_vectors_navi()
        NavInputInterface.refresh_logentries_table()

    @staticmethod
    def button_vectortableview_navi_clicked():
        button_vectortableview: QPushButton = NavInputInterface.nav_mainwindow.button_vectortableview_navi
        print(button_vectortableview.text() + ' clicked')
        button_vectortableview.toggle()
        NavInputInterface.nav_mainwindow.hide()
        NavInputInterface.nav_mainwindow.window = Ui_mainwindow_vectortableview()
        NavInputInterface.nav_mainwindow.window.show()
        #file_name = os.path.dirname(os.path.abspath(__file__)) + r"/QGraphViewer.py"
        #subprocess.run(['python3', file_name])

    @staticmethod
    def refresh_listview_timefilters_navi():
        time_filters: list = DatabaseInterface.find_time_filters_all()
        listview_timefilters: QListView = NavInputInterface.nav_mainwindow.listview_timefilter_navi
        listview_timefilters_model: QStandardItemModel = listview_timefilters.model()
        listview_timefilters_model.clear()
        for time_filter in time_filters:
            time_filter: dict
            time_filter_item = QStandardItem(time_filter['name'])
            time_filter_item.time_filter_id = str(time_filter['_id'])
            print(time_filter['name'], str(time_filter['_id']))
            time_filter_item.setCheckable(True)
            time_filter_item.setEditable(False)
            listview_timefilters_model.appendRow(time_filter_item)

    @staticmethod
    def refresh_listview_vectors_navi():
        vectors: list = DatabaseInterface.find_vectors_all()
        listview_vectors: QListView = NavInputInterface.nav_mainwindow.listview_vectors_navi
        listview_vectors_model: QStandardItemModel = listview_vectors.model()
        listview_vectors_model.clear()
        for vector in vectors:
            vector: dict
            vector_item = QStandardItem(vector['name'])
            vector_item.setCheckable(True)
            vector_item.setEditable(False)
            listview_vectors_model.appendRow(vector_item)

    @staticmethod # Complete
    def refresh_listview_locations_navi():
        log_entries: list = DatabaseInterface.find_log_entries_all()
        listview_locations: QListView = NavInputInterface.nav_mainwindow.listview_location_navi
        listview_locations_model: QStandardItemModel = listview_locations.model()
        listview_locations_model.clear()
        locations_set: set = set()
        for log_entry in log_entries:
            log_entry: dict
            if log_entry['location'] not in locations_set:
                locations_set.add(log_entry['location'])
                location_item = QStandardItem(log_entry['location'])
                location_item.setCheckable(True)
                location_item.setEditable(False)
                listview_locations_model.appendRow(location_item)

    @staticmethod
    def check_datetimes_values(start_datetime_info: int, end_datetime_info: int) -> bool:
        return (start_datetime_info - end_datetime_info) < 0

    @staticmethod  # COMPLETE
    def set_enable_filter_checkboxes(enabled: bool):
        for checkbox in NavInputInterface.static_checkboxes:
            checkbox: QCheckBox
            checkbox.setEnabled(enabled)
        listview_locations: QListView = NavInputInterface.nav_mainwindow.listview_location_navi
        listview_locations_model: QStandardItemModel = listview_locations.model()
        listview_locations_count: int = listview_locations_model.rowCount()
        for index in range(listview_locations_count):
            item_location: QStandardItem = listview_locations_model.item(index)
            item_location.setEnabled(enabled)
        listview_vectors: QListView = NavInputInterface.nav_mainwindow.listview_vectors_navi
        listview_vectors_model: QStandardItemModel = listview_vectors.model()
        listview_vectors_count: int = listview_vectors_model.rowCount()
        for index in range(listview_vectors_count):
            item_vector: QStandardItem = listview_vectors_model.item(index)
            item_vector.setEnabled(enabled)
        listview_timefilters: QListView = NavInputInterface.nav_mainwindow.listview_timefilter_navi
        listview_timefilters_model: QStandardItemModel = listview_timefilters.model()
        listview_timefilters_count: int = listview_timefilters_model.rowCount()
        for index in range(listview_timefilters_count):
            item_timefilter: QStandardItem = listview_timefilters_model.item(index)
            item_timefilter.setEnabled(enabled)
        button_vectorconfig = NavInputInterface.nav_mainwindow.button_vectorconfig_navi
        button_vectorconfig.setEnabled(enabled)
        button_search = NavInputInterface.nav_mainwindow.button_search_navi
        button_search.setEnabled(enabled)
        button_addtimefilter = NavInputInterface.nav_mainwindow.button_timefilter_navi
        button_addtimefilter.setEnabled(enabled)

    @staticmethod
    def logentries_vector_combobox_changed(vector_index: int):
        combobox: QComboBox = NavInputInterface.nav_mainwindow.sender()
        logentry_id: str = combobox.property("logentry_id")
        vector_name: str = combobox.itemText(vector_index)
        vector_id: str = '0'
        if vector_name == 'None':
            update_fields: dict = {'vector': vector_name, 'vector_id': vector_id}
            DatabaseInterface.update_one_log_entries_by_id(log_entries_item_id=logentry_id, update_fields=update_fields)
            return
        vectors: list = DatabaseInterface.find_vectors_all()
        for vector in vectors:
            vector: dict
            if vector['name'] == vector_name:
                vector_id: str = str(vector['_id'])
                break
        update_fields: dict = {'vector': vector_name, 'vector_id': vector_id}
        DatabaseInterface.update_one_log_entries_by_id(log_entries_item_id=logentry_id, update_fields=update_fields)

    @staticmethod
    def refresh_logentries_table(search_type: str = None):
        tablewidget_logentries: QTableWidget = NavInputInterface.nav_mainwindow.tablewidget_navi
        tablewidget_logentries.setSortingEnabled(False)

        if search_type == 'condition':
            log_entries: list = DatabaseInterface.find_log_entries_condition(
                NavInputInterface.log_entries_conditions)
        elif search_type == 'regex':
            log_entries: list = DatabaseInterface.find_log_entries_regex(NavInputInterface.log_entries_regex)
        else:
            log_entries: list = DatabaseInterface.find_log_entries_all()

        tablewidget_logentries.clearContents()
        vectors: list = DatabaseInterface.find_vectors_all()
        vectors_names_dict: dict = dict()
        vector_names_list: list = list()
        vector_names_list.append('None')
        for vector in vectors:
            vector: dict
            vector_name = str(vector['name'])
            vector_id = str(vector['_id'])
            vectors_names_dict[vector_id] = vector_name
            vector_names_list.append(vector_name)

        print(vectors_names_dict)
        print(vector_names_list)
        counter: int = 0
        for log_entry in log_entries:
            tablewidget_logentries.insertRow(counter)
            checkbox_item = QTableWidgetItem()
            checkbox_item.setCheckState(False)
            list_number_item = QTableWidgetItem(str(log_entry['list_number']))
            list_number_item.setFlags(Qt.ItemIsEnabled)
            timestamp_item = QTableWidgetItem(log_entry['timestamp'])
            timestamp_item.setFlags(Qt.ItemIsEnabled)
            event_item = QTableWidgetItem(log_entry['event'])
            event_item.setFlags(Qt.ItemIsEnabled)
            vector_item = QComboBox()
            vector_item.setProperty('logentry_id', str(log_entry['_id']))
            vector_item.currentIndexChanged.connect(NavInputInterface.logentries_vector_combobox_changed)
            log_entry_vector: str = log_entry['vector']
            log_entry_vector_id: str = str(log_entry['vector_id'])
            vector_item.addItems(vector_names_list)
            if log_entry_vector == 'None':
                vector_item.setCurrentIndex(0)
            elif log_entry_vector_id in vectors_names_dict.keys():
                vector_item.setCurrentIndex(vector_names_list.index(vectors_names_dict[log_entry_vector_id]))
            else:
                vector_item.setCurrentIndex(0)
            logentryid_item = QTableWidgetItem(str(log_entry['_id']))
            logentryid_item.setFlags(Qt.ItemIsEnabled)

            tablewidget_logentries.setItem(counter, 0, checkbox_item)
            tablewidget_logentries.setItem(counter, 1, list_number_item)
            tablewidget_logentries.setItem(counter, 2, timestamp_item)  # log entry timestamp column
            tablewidget_logentries.setItem(counter, 3, event_item)  # log entry event column
            tablewidget_logentries.setCellWidget(counter, 4, vector_item)  # vector column
            tablewidget_logentries.setItem(counter, 5, logentryid_item)
            counter += 1

        tablewidget_logentries.setRowCount(len(log_entries))
        tablewidget_logentries.setSortingEnabled(True)

    @staticmethod
    def hide_logentries_column(column: int, hide: bool):
        table_widget: QTableWidget = NavInputInterface.nav_mainwindow.tablewidget_navi
        table_widget.setColumnHidden(column, hide)
