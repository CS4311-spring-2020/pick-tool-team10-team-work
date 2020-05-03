from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
import sys

from nav_databse_interface import NavDatabaseInterface
import pymongo
import pprint

locations = {
    0: 'El Paso',
    1: 'Santa Fe',
    2: 'New York City',
    3: 'Los Angeles',
    4: 'Dallas',
    5: 'Houston',
    6: 'Phoenix',
    7: 'Chicago',
    8: 'San Diego',
    9: 'San Fransisco'
}

three_counter = 0
insert_items = list()

for i in range(100):
    list_number = i
    timestamp = 'timestamp'
    event = 'event' + str(i)
    vector = 'vector' + str(i%10)
    location = locations[i%10]
    if three_counter == 0:
        creator = 'red'
    elif three_counter == 1:
        creator = 'white'
    elif three_counter == 2:
        creator = 'blue'
        three_counter = -1
    three_counter += 1
    insert_items.append(NavDatabaseInterface.create_log_entries_item(list_number=list_number, timestamp=timestamp,
                                                                     event=event, vector=vector,
                                                                     location=location, creator=creator))

pprint.pprint(insert_items)
NavDatabaseInterface.insert_many_log_entries(insert_items)
#NavDatabaseInterface.delete_all_items_log_entries()
#NavDatabaseInterface.delete_log_entries_collection()


#return_item = NavDatabaseInterface.create_logentry_item(list_number=1, timestamp='123.21',
                                                        #event='event01', vector='vector1',
                                                        #location='El Paso', team='Red')

#NavDatabaseInterface.insert_one_logentry(return_item)


'''
self.listview_location_navi.setEditTriggers(QAbstractItemView.DoubleClicked)
self.listview_location_navi.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
self.listview_location_navi.customContextMenuRequested.connect(self.contextMenuEventM)
self.model = QStandardItemModel()
#self.model.itemChanged.connect(nii.set_items)
for n in range(10):
    item = QStandardItem('Item %s' % n)
    item.setCheckable(True)
    item.setEditable(True)
    self.model.appendRow(item)
self.listview_location_navi.setModel(self.model)

self.setup_interace()


def contextMenuEventM(self, position):
    print(position)
    contextMenu = QMenu(self)
    newAct = contextMenu.addAction("New")
    openAct = contextMenu.addAction("Open")
    quitAct = contextMenu.addAction("Quit")
    action = contextMenu.exec_(self.mapToGlobal(position))
    if action == quitAct:
        self.close()
'''
