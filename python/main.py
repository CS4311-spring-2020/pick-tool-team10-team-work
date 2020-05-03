from Windows.ProjectConfigWindow import ProjectConfigWindow
from Windows.mainwindow_vectortableview import Ui_mainwindow_vectortableview

from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

from os import path
import sys

class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setWindowTitle('PICK Autonomous Tool')
        mainwidget = QWidget()
        self.setCentralWidget(mainwidget)
        mainlayout = QVBoxLayout()
        newProjButtonLayout = QHBoxLayout()
        exisProjButtonLayout = QHBoxLayout()

        newProjLabel = QLabel('To start a new project click the button below.')
        newProjLabel.setAlignment(Qt.AlignCenter)
        newProjButton = QPushButton('Create New Project')
        newProjButton.clicked.connect(self.on_newproj_button_clicked)

        newProjButtonLayout.addStretch()
        newProjButtonLayout.addWidget(newProjButton)
        newProjButtonLayout.addStretch()

        exisProjLabel = QLabel('To resume a project click the button below.')
        exisProjLabel.setAlignment(Qt.AlignCenter)
        exisProjButton = QPushButton('Resume Project')
        exisProjButton.clicked.connect(self.on_exisproj_button_clicked)

        exisProjButtonLayout.addStretch()
        exisProjButtonLayout.addWidget(exisProjButton)
        exisProjButtonLayout.addStretch()

        mainlayout.addStretch()
        mainlayout.addWidget(newProjLabel)
        mainlayout.addLayout(newProjButtonLayout)
        mainlayout.addStretch()
        mainlayout.addWidget(exisProjLabel)
        mainlayout.addLayout(exisProjButtonLayout)
        mainlayout.addStretch()

        mainwidget.setLayout(mainlayout)
    
    def cleanse_data(self):
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "./Data", "ProjectConfigData.txt"))
        filepath2 = path.abspath(path.join(basepath, "./Data", "DateRange.txt"))
        filepath3 = path.abspath(path.join(basepath, "./Data", "ProjectDescription.txt"))

        #Clean file containing team folder log files
        file_descriptor = open(filepath, 'w')
        file_descriptor.write('\n\n\n\n')
        file_descriptor.close()

        #Clean file containing the date range for log files
        file_descriptor2 = open(filepath2, 'w')
        file_descriptor2.write('\n\n')
        file_descriptor2.close()

        #Clean file containing the project description
        file_descriptor3 = open(filepath3, 'w')
        file_descriptor3.write('\n\n')
        file_descriptor3.close()

    def on_newproj_button_clicked(self):
        self.cleanse_data()
        self.hide()
        self.window = ProjectConfigWindow()
        self.window.show()

    def on_exisproj_button_clicked(self):
        self.hide()
        MainWindow = QMainWindow()
        ui = Ui_mainwindow_vectortableview()
        ui.setupUi(MainWindow)
        self.window = MainWindow
        self.window.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainApp()
    ui.show()
    sys.exit(app.exec_())