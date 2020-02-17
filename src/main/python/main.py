from Windows.ProjectConfigWindow import ProjectConfigWindow
from Windows.GraphTableWindow import GraphTableWindow

from PyQt5.QtCore import *
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

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
    
    def on_newproj_button_clicked(self):
        self.hide()
        self.window = ProjectConfigWindow()
        self.window.show()

    def on_exisproj_button_clicked(self):
        self.hide()
        MainWindow = QMainWindow()
        ui = GraphTableWindow()
        ui.setupUi(MainWindow)
        self.window = MainWindow
        self.window.show()

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    app = MainApp()
    app.setGeometry(500, 300, 400, 150)
    app.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)