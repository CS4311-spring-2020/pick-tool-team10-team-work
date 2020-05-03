#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Saifeddine ALOUI
Description:
A simple graphviz graphs viewer that enables creating graphs visually,
manipulate them and save them
"""
from PyQt5.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, \
    QFormLayout, QComboBox, QPushButton, QInputDialog, QLineEdit, QLabel
import sys
import os
import time

print(sys.path)
from QGraphViz import QGraphViz, QGraphVizManipulationMode
from DotParser import Graph, GraphType
from Engines import Dot

if __name__ == "__main__":
    # Create QT application
    app = QApplication(sys.argv)

    # Events

    def node_selected(node):
        if (qgv.manipulation_mode == QGraphVizManipulationMode.Node_remove_Mode):
            print("Node {} removed".format(node))
        else:
            print("Node selected {}".format(node))


    def edge_selected(edge):
        if (qgv.manipulation_mode == QGraphVizManipulationMode.Edge_remove_Mode):
            print("Edge {} removed".format(edge))
        else:
            print("Edge selected {}".format(edge))


    def node_invoked(node):
        print("Node double clicked")


    def edge_invoked(node):
        print("Edge double clicked")


    def node_removed(node):
        print("Node removed")


    def edge_removed(node):
        print("Edge removed")


    # Create QGraphViz widget
    show_subgraphs = True
    qgv = QGraphViz(
        show_subgraphs=show_subgraphs,
        auto_freeze=True,  # show autofreeze capability
        node_selected_callback=node_selected,
        edge_selected_callback=edge_selected,
        node_invoked_callback=node_invoked,
        edge_invoked_callback=edge_invoked,
        node_removed_callback=node_removed,
        edge_removed_callback=edge_removed,

        hilight_Nodes=True,
        hilight_Edges=True
    )

    redTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"/icon/redTeam.png"
    whiteTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"/icon/whiteTeam.png"
    blueTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"/icon/blueTeam.png"

    #For Windows(change to backslash)
    #redTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"\icon\redTeam.png"
    #whiteTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"\icon\whiteTeam.png"
    #blueTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"\icon\blueTeam.png"

    qgv.setStyleSheet("background-color:white;")
    # Create A new Graph using Dot layout engine
    qgv.new(Dot(Graph("Main_Graph"), show_subgraphs=show_subgraphs))
    # Define a graph

    #Visual toggles for node attributes
    showNodeID = False
    showNodeName = True
    showNodeTime = True
    showNodeDesc = True

    # Example Node Dicitonary of Node ID's with their Node name, team, time-stamp, and node discripiton
    nodeDic = {
        "001": {
            "name":"Node1",
            "team":"red",
            "time":"2020-3-3 13:09:40",
            "description":"SQL Injection",
        },
        "002": {
            "name":"Node2",
            "team": "blue",
            "time": "2020-3-3 13:09:42",
            "description": "Windows SQL Server Log\nShows Red Team Query"
        },
        "003": {
            "name": "Node3",
            "team": "blue",
            "time": "2020-3-3 13:09:46",
            "description": "Blue Team is aware of breach"
        },
        "004": {
            "name": "Node4",
            "team": "blue",
            "time": "2020-3-3 13:09:52",
            "description": "Windows Log Shows Admin Login"
        },
        "005": {
            "name": "Node5",
            "team": "white",
            "time": "2020-3-3 13:09:56",
            "description": "White Team records action"
        },
        "006": {
            "name": "Node6",
            "team": "blue",
            "time": "2020-3-3 13:10:35",
            "description": "Windows Log Server Config Change"
        }
    }
    # Example relationships, Parent node ID's with their children node ID's and label text
    edgeDic = {
        "001":{
            "002":"[Relationship label text]"
        },
        "002":{
            "003":"[Relationship label text]"
        },
        "003":{
            "004":"[Relationship label text]",
            "005":"[Relationship label text]"
        },
        "005":{
            "006":"[Relationship label text]"
        }
    }

    # Adds all the nodes in the node dicitonary to the graph
    for nodeID, nodeInfo in nodeDic.items():
        nodeText = ""
        if(showNodeID and nodeID != ""):
            nodeText += nodeID
        if (showNodeName and nodeInfo["name"] != ""):
            nodeText += "\n"+nodeInfo["name"]
        if (showNodeTime and nodeInfo["time"] != ""):
            nodeText += "\n"+nodeInfo["time"]
        if (showNodeDesc and nodeInfo["description"] != ""):
            nodeText += "\n"+nodeInfo["description"]
        team = redTeamIcon
        if(nodeInfo["team"]=="blue"):
            team = blueTeamIcon
        elif(nodeInfo["team"]=="white"):
            team = whiteTeamIcon

        nodeDic[nodeID]["node"] = qgv.addNode(qgv.engine.graph, nodeID, label=" ", text = nodeText, shape = team)


    # Adds all the edges(relationships) in the edge dictionary to the graph
    for parent, children in edgeDic.items():
        if parent in nodeDic:
            for child in children:
                if child in nodeDic:
                    qgv.addEdge(nodeDic[parent]["node"], nodeDic[child]["node"], {})
                else:
                    print("The childe with ID: "+ child +" not found")
        else:
            print("The parent node with ID: "+ parent + " not found")

    # n1 = qgv.addNode(qgv.engine.graph, "Node1", label=" ", text = "Sample Node Name\nNew line\nSomething else", shape= redTeamIcon)
    # n2 = qgv.addNode(qgv.engine.graph, "Node2", label=" ", shape = blueTeamIcon)
    # n3 = qgv.addNode(qgv.engine.graph, "Node3", label=" ", shape = blueTeamIcon)
    # n4 = qgv.addNode(qgv.engine.graph, "Node4", label=" ", shape = blueTeamIcon)
    # n5 = qgv.addNode(qgv.engine.graph, "Node5", label=" ", shape = whiteTeamIcon)
    # n6 = qgv.addNode(qgv.engine.graph, "Node3", label=" ", shape = blueTeamIcon)
    #
    # qgv.addEdge(n1, n2, {})
    # qgv.addEdge(n2, n3, {})
    # qgv.addEdge(n3, n4, {})
    # qgv.addEdge(n3, n5, {})
    # qgv.addEdge(n5, n6, {})


    # Build the graph (the layout engine organizes where the nodes and connections are)
    qgv.build()
    # Save it to a file to be loaded by Graphviz if needed
    qgv.save("test.gv")
    # Create a Main window
    w = QMainWindow()
    w.setWindowTitle('Graph View')
    # Create a central widget to handle the QGraphViz object
    wi = QWidget()
    wi.setLayout(QVBoxLayout())
    w.setCentralWidget(wi)
    # Add the QGraphViz object to the layout
    wi.layout().addWidget(qgv)
    # Add a horizontal layout (a pannel to select what to do)
    hpanel = QHBoxLayout()
    wi.layout().addLayout(hpanel)


    # Add few buttons to the panel
    def manipulate():
        qgv.manipulation_mode = QGraphVizManipulationMode.Nodes_Move_Mode


    def save():
        fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.json")
        if (fname[0] != ""):
            qgv.saveAsJson(fname[0])

        # fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.gv")
        # if(fname[0]!=""):
        #    qgv.save(fname[0])


    def new():
        qgv.engine.graph = Graph("MainGraph")
        qgv.build()
        qgv.repaint()


    def load():
        fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.json")
        if (fname[0] != ""):
            qgv.loadAJson(fname[0])

        # fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.gv")
        # if(fname[0]!=""):
        #    qgv.load_file(fname[0])


    def add_node():
        dlg = QDialog()
        dlg.ok = False
        dlg.node_name = ""
        dlg.node_label = ""
        dlg.node_type = "None"
        # Layouts
        main_layout = QVBoxLayout()
        l = QFormLayout()
        buttons_layout = QHBoxLayout()

        main_layout.addLayout(l)
        main_layout.addLayout(buttons_layout)
        dlg.setLayout(main_layout)

        leNodeName = QLineEdit()
        leNodeLabel = QLineEdit()
        cbxNodeType = QComboBox()
        leImagePath = QLineEdit()

        pbOK = QPushButton()
        pbCancel = QPushButton()

        cbxNodeType.addItems(["None", "circle", "box"])
        pbOK.setText("&OK")
        pbCancel.setText("&Cancel")

        l.setWidget(0, QFormLayout.LabelRole, QLabel("Node Name"))
        l.setWidget(0, QFormLayout.FieldRole, leNodeName)
        l.setWidget(1, QFormLayout.LabelRole, QLabel("Node Label"))
        l.setWidget(1, QFormLayout.FieldRole, leNodeLabel)
        l.setWidget(2, QFormLayout.LabelRole, QLabel("Node Type"))
        l.setWidget(2, QFormLayout.FieldRole, cbxNodeType)
        l.setWidget(3, QFormLayout.LabelRole, QLabel("Node Image"))
        l.setWidget(3, QFormLayout.FieldRole, leImagePath)

        def ok():
            dlg.OK = True
            dlg.node_name = leNodeName.text()
            dlg.node_label = leNodeLabel.text()
            if (leImagePath.text()):
                dlg.node_type = leImagePath.text()
            else:
                dlg.node_type = cbxNodeType.currentText()
            dlg.close()

        def cancel():
            dlg.OK = False
            dlg.close()

        pbOK.clicked.connect(ok)
        pbCancel.clicked.connect(cancel)

        buttons_layout.addWidget(pbOK)
        buttons_layout.addWidget(pbCancel)
        dlg.exec_()

        # node_name, okPressed = QInputDialog.getText(wi, "Node name","Node name:", QLineEdit.Normal, "")
        if dlg.OK and dlg.node_name != '':
            qgv.addNode(qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_type)
            qgv.build()


    def rem_node():
        qgv.manipulation_mode = QGraphVizManipulationMode.Node_remove_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnRemNode.setChecked(True)


    def rem_edge():
        qgv.manipulation_mode = QGraphVizManipulationMode.Edge_remove_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnRemEdge.setChecked(True)


    def add_edge():
        qgv.manipulation_mode = QGraphVizManipulationMode.Edges_Connect_Mode
        for btn in buttons_list:
            btn.setChecked(False)
        btnAddEdge.setChecked(True)


    # def add_subgraph():
    #     dlg = QDialog()
    #     dlg.ok = False
    #     dlg.subgraph_name = ""
    #     dlg.subgraph_label = ""
    #     dlg.subgraph_type = "None"
    #     # Layouts
    #     main_layout = QVBoxLayout()
    #     l = QFormLayout()
    #     buttons_layout = QHBoxLayout()
    #
    #     main_layout.addLayout(l)
    #     main_layout.addLayout(buttons_layout)
    #     dlg.setLayout(main_layout)
    #
    #     leSubgraphName = QLineEdit()
    #     leSubgraphLabel = QLineEdit()
    #
    #     pbOK = QPushButton()
    #     pbCancel = QPushButton()
    #
    #     pbOK.setText("&OK")
    #     pbCancel.setText("&Cancel")
    #
    #     l.setWidget(0, QFormLayout.LabelRole, QLabel("Subgraph Name"))
    #     l.setWidget(0, QFormLayout.FieldRole, leSubgraphName)
    #     l.setWidget(1, QFormLayout.LabelRole, QLabel("Subgraph Label"))
    #     l.setWidget(1, QFormLayout.FieldRole, leSubgraphLabel)
    #
    #     def ok():
    #         dlg.OK = True
    #         dlg.subgraph_name = leSubgraphName.text()
    #         dlg.subgraph_label = leSubgraphLabel.text()
    #         dlg.close()
    #
    #     def cancel():
    #         dlg.OK = False
    #         dlg.close()
    #
    #     pbOK.clicked.connect(ok)
    #     pbCancel.clicked.connect(cancel)
    #
    #     buttons_layout.addWidget(pbOK)
    #     buttons_layout.addWidget(pbCancel)
    #     dlg.exec_()
    #
    #     if dlg.OK and dlg.subgraph_name != '':
    #         qgv.addSubgraph(qgv.engine.graph, dlg.subgraph_name, subgraph_type=GraphType.SimpleGraph,
    #                         label=dlg.subgraph_label)
    #         qgv.build()
    #
    #
    # def rem_subgraph():
    #     qgv.manipulation_mode = QGraphVizManipulationMode.Subgraph_remove_Mode
    #     for btn in buttons_list:
    #         btn.setChecked(False)
    #     btnRemSubGraph.setChecked(True)


    # Add buttons
    btnNew = QPushButton("New")
    btnNew.clicked.connect(new)
    btnOpen = QPushButton("Open")
    btnOpen.clicked.connect(load)

    btnSave = QPushButton("Save")
    btnSave.clicked.connect(save)

    hpanel.addWidget(btnNew)
    hpanel.addWidget(btnOpen)
    hpanel.addWidget(btnSave)

    buttons_list = []
    btnManip = QPushButton("Manipulate")
    btnManip.setCheckable(True)
    btnManip.setChecked(True)
    btnManip.clicked.connect(manipulate)
    hpanel.addWidget(btnManip)
    buttons_list.append(btnManip)

    btnAddNode = QPushButton("Add Node")
    btnAddNode.clicked.connect(add_node)
    hpanel.addWidget(btnAddNode)
    buttons_list.append(btnManip)

    btnRemNode = QPushButton("Rem Node")
    btnRemNode.setCheckable(True)
    btnRemNode.clicked.connect(rem_node)
    hpanel.addWidget(btnRemNode)
    buttons_list.append(btnRemNode)

    btnAddEdge = QPushButton("Add Edge")
    btnAddEdge.setCheckable(True)
    btnAddEdge.clicked.connect(add_edge)
    hpanel.addWidget(btnAddEdge)
    buttons_list.append(btnAddEdge)

    btnRemEdge = QPushButton("Rem Edge")
    btnRemEdge.setCheckable(True)
    btnRemEdge.clicked.connect(rem_edge)
    hpanel.addWidget(btnRemEdge)
    buttons_list.append(btnRemEdge)

    # btnAddSubGraph = QPushButton("Add Subgraph")
    # btnAddSubGraph.clicked.connect(add_subgraph)
    # hpanel.addWidget(btnAddSubGraph)
    #
    # btnRemSubGraph = QPushButton("Rem Subgraph")
    # btnRemSubGraph.setCheckable(True)
    # btnRemSubGraph.clicked.connect(rem_subgraph)
    # hpanel.addWidget(btnRemSubGraph)
    # buttons_list.append(btnRemSubGraph)

    w.showMaximized()

    sys.exit(app.exec_())