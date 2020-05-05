#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, \
    QFormLayout, QComboBox, QPushButton, QInputDialog, QLineEdit, QLabel
from PyQt5 import QtCore
import sys
import os
import time
from sys import platform
import xml.etree.cElementTree as ET
print(sys.path)
from QGraphViz import QGraphViz, QGraphVizManipulationMode
from DotParser import Graph, GraphType
from Engines import Dot

# Example Node Dicitonary of Node ID's with their Node name, team, time-stamp, and node discripiton
nodeDic = {
    "0001": {
        "name":"Node1",
        "team":"red",
        "time":"2020-3-3 13:09:40",
        "description":"SQL Injection",
    },
    "0002": {
        "name":"Node2",
        "team": "blue",
        "time": "2020-3-3 13:09:42",
        "description": "Windows SQL Server Log\nShows Red Team Query"
    },
    "0003": {
        "name": "Node3",
        "team": "blue",
        "time": "2020-3-3 13:09:46",
        "description": "Blue Team is aware of breach"
    },
    "0004": {
        "name": "Node4",
        "team": "blue",
        "time": "2020-3-3 13:09:52",
        "description": "Windows Log Shows Admin Login"
    },
    "0005": {
        "name": "Node5",
        "team": "white",
        "time": "2020-3-3 13:09:56",
        "description": "White Team records action"
    },
    "0006": {
        "name": "Node6",
        "team": "blue",
        "time": "2020-3-3 13:10:35",
        "description": "Windows Log Server Config Change"
    }
}
# Example relationships, Parent node ID's with their children node ID's and label text
edgeDic = {
    "0001":{
        "0002":"[Relationship label text]"
    },
    "0002":{
        "0003":"[Relationship label text]"
    },
    "0003":{
        "0004":"[Relationship label text]",
        "0005":"[Relationship label text]"
    },
    "0005":{
        "0006":"[Relationship label text]"
    }
}

#Visual toggles for node attributes
showNodeID = False
showNodeName = True
showNodeTime = True
showNodeDesc = True

if platform == "win32":
    redTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"\icon\redTeam.png"
    whiteTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"\icon\whiteTeam.png"
    blueTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"\icon\blueTeam.png"
else:
    redTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"/icon/redTeam.png"
    whiteTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"/icon/whiteTeam.png"
    blueTeamIcon = os.path.dirname(os.path.abspath(__file__)) + r"/icon/blueTeam.png"

if __name__ == "__main__":
    # Create QT application
    app = QApplication(sys.argv)

    # Events
    def node_selected(node):
        if (qgv.manipulation_mode == QGraphVizManipulationMode.Node_remove_Mode):
            print("Node {} removed".format(node))
            #print("Node with nodeID: "+ node.getID() + "removed")
        else:
            print("Node selected {}".format(node))

    def edge_selected(edge):
        if (qgv.manipulation_mode == QGraphVizManipulationMode.Edge_remove_Mode):
            print("Edge {} removed".format(edge))
        else:
            print("Edge selected {}".format(edge))

    def node_invoked(node):
        print("Node double clicked")
        edit_node(node)

    def edge_invoked(node):
        print("Edge double clicked")

    def node_removed(node):
        nodeID = node.getID()
        print("Node with nodeID: "+ nodeID +" removed")
        # remove node from node Dictionary
        print(nodeDic.pop(nodeID))
        if nodeID in edgeDic:
            edgeDic.pop(nodeID)
        for parent, children in edgeDic.items():
                if nodeID in children:
                    children.pop(nodeID)

    def edge_removed(edge):
        src = edge.getSource().getID()
        dest = edge.getDest().getID()

        if src in edgeDic:
            if dest in edgeDic[src]:
                edgeDic[src].pop(dest)
            if len(edgeDic[src])==0:
                edgeDic.pop(src)
        print(edgeDic)
        print("Edge removed: source ["+src+"] dest["+dest+"]")

    # Returns next unique node ID available, format ####,  increments value
    def getNextNodeID():
        val = len(nodeDic)
        nextID = format(val, '004d')
        while nextID in nodeDic:
            val+=1
            nextID = format(val, '004d')
        return nextID

    def new_edge_being_added(source, dest):
        srcName = source.getID()
        destName = dest.getID()
        if srcName in edgeDic:
            if destName in edgeDic[srcName]:
                print("Edge with same source ["+srcName+"] and dest ["+destName+"] already exists. Edge is not added")
                return False, {}
            else:
                edgeDic[srcName] = {destName: "[Edge Label Text]"}
                print("Adding edge with source [" + srcName + "] and dest [" + destName + "]")
                return True, {}
        else:
            edgeDic[srcName]={destName:"[Edge Label Text]"}
            print("Adding edge with source [" + srcName + "] and dest [" + destName + "]")
            return True,{}

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
        new_edge_beingAdded_callback = new_edge_being_added,

        hilight_Nodes=True,
        hilight_Edges=True
    )

    qgv.setStyleSheet("background-color:white;")
    # Create A new Graph using Dot layout engine
    qgv.new(Dot(Graph("Main_Graph"), show_subgraphs=show_subgraphs))
    # Define a graph

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
        fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.json;;*.jpg;;*.png;;*.xml")
        if(fname[1] == "*.jpg" and fname[0] != ""):
            qgv.saveAsJpg(fname[0])
        if (fname[1] == "*.json" and fname[0] != ""):
            qgv.saveAsJson(fname[0])
        if (fname[1] == "*.png" and fname[0] != ""):
            qgv.saveAsPng(fname[0])
        if (fname[1] == "*.xml" and fname[0] != ""):
            saveAsXml(fname[0])

    # Generates xml file for graph
    def saveAsXml(filename):
        # Sets top of xml file
        graphml = ET.Element('graphml',{'xmlns': "http://graphml.graphdrawing.org/xmlns",
                                        "xmlns:mtg":"http://maltego.paterva.com/xml/mtgx"})
        versInf = ET.SubElement(graphml,'VersionInfo', {'createdBy': "Maltego Community Edition",
                                                        "subtitle": "",
                                                        "version":"4.2.9.12898"})
        key1 = ET.SubElement(graphml, 'key', {'attr.name': "MaltegoEntity",
                                                         "for": "node",
                                                         "id": "d0"})
        key2 = ET.SubElement(graphml, 'key', {'for': "node",
                                             "id": "d1",
                                             "yfiles.type": "nodegraphics"})
        key3 = ET.SubElement(graphml, 'key', {'attr.name': "MaltegoLink",
                                             "for": "edge",
                                             "id": "d2"})
        key4 = ET.SubElement(graphml, 'key', {'for': "edge",
                                             "id": "d3",
                                             "yfiles.type": "edgegraphics"})
        graph = ET.SubElement(graphml, 'graph', {'edgedefault': "directed",
                                             "id": "G",})
        randNum = 250
        # Adds nodes to xml file
        for nodeID, nodeInfo in nodeDic.items():
            nodeTag = ET.SubElement(graph, 'node',{'id': nodeID})
            dataTag = ET.SubElement(nodeTag, 'data', {"key":"d0"})
            entityType = "yourorganization.WhiteTeam"
            dispName = "White Team"
            name = "properties.whiteteam"
            if(nodeInfo["team"]=='red'):
                entityType = "yourorganization.RedTeam"
                dispName = "Red Team"
                name = "properties.redteam"
            if (nodeInfo["team"] == 'blue'):
                entityType = "yourorganization.BlueTeam"
                dispName = "Blue Team"
                name = "properties.blueteam"
            idRand = "20nyvatspkbwg"+str(randNum)
            uniqueID= idRand[-13:]
            randNum+=1
            mtgMalt = ET.SubElement(dataTag, 'mtg:MaltegoEntity', {"id": uniqueID,
                                                                   "type": entityType})
            mtgProperties = ET.SubElement(mtgMalt,"mtg:Properties")
            mtgProp = ET.SubElement(mtgProperties, "mtg:Property",{"displayName": dispName,
                                                                   "hidden": "false",
                                                                   "name": name,
                                                                   "nullable":"true",
                                                                   "readonly":"false",
                                                                   "type":"string"})
            mtgValue = ET.SubElement(mtgProp,'mtg:Value')
            mtgValue.text = nodeInfo["description"]

            mtgNotes = ET.SubElement(mtgMalt,'mtg:Notes')
            mtgNotes.text = "![CDATA["+ nodeInfo["time"]+"]]"

            dataTag2 = ET.SubElement(nodeTag, 'data', {"key": "d1"})
            mtgERen = ET.SubElement(dataTag2,"mtg:EntityRenderer")
            position = nodeInfo["node"].getPos()
            mtgPos = ET.SubElement(mtgERen,'mtg:Position', {"x": str(position[0]),
                                                            "y": str(position[1])})

        # Adds edges to xml file
        counter=0#increment for unique id for each
        for parent, children in edgeDic.items():
                for child in children:
                    edgeID = "e"+str(counter)
                    counter+=1
                    edgeTag = ET.SubElement(graph, "edge", {"id": edgeID,
                                                            "source": parent,
                                                            "target":child})
                    dataTag3 = ET.SubElement(edgeTag, 'data',{"key":"d2"})
                    idRand = "20nyvatspkbwg" + str(counter)
                    uniqueID = idRand[-13:]
                    mtgMLink = ET.SubElement(dataTag3, "mtg:MaltegoLink",{"id":uniqueID,
                                                                          "type":"maltego.link.manual-link"})
                    mtgPropties = ET.SubElement(mtgMLink, "mtg:Properties")
                    mtgPropty = ET.SubElement(mtgPropties, "mtg:Property", {"displayName":"Label",
                                                                            "hidden":"false",
                                                                            "name":"maltego.link.manual.type",
                                                                            "nullable":"true",
                                                                            "readonly":"false",
                                                                            "type":"string"})
                    mtgVal = ET.SubElement(mtgPropty, "mtg:Value")
                    mtgVal.text = ""

                    mtgPropty2 = ET.SubElement(mtgPropties, "mtg:Property", {"displayName":"Show Label",
                                                                            "hidden":"false",
                                                                            "name":"maltego.link.show-label",
                                                                            "nullable":"true",
                                                                            "readonly":"false",
                                                                            "type":"int"})
                    mtgVal2 = ET.SubElement(mtgPropty2, "mtg:Value")
                    mtgVal2.text = "0"

                    mtgPropty3 = ET.SubElement(mtgPropties, "mtg:Property", {"displayName": "Color",
                                                                             "hidden": "false",
                                                                             "name": "maltego.link.color",
                                                                             "nullable": "true",
                                                                             "readonly": "false",
                                                                             "type": "color"})
                    mtgVal3 = ET.SubElement(mtgPropty3, "mtg:Value")
                    mtgVal3.text = "#000000"

                    mtgPropty4 = ET.SubElement(mtgPropties, "mtg:Property", {"displayName": "Description",
                                                                             "hidden": "false",
                                                                             "name": "maltego.link.manual.description",
                                                                             "nullable": "true",
                                                                             "readonly": "false",
                                                                             "type": "string"})
                    mtgVal4 = ET.SubElement(mtgPropty4, "mtg:Value")

                    dataTag4 = ET.SubElement(edgeTag, "data",{"key":"d3"})
                    mtgLingRen = ET.SubElement(dataTag4,"mtg:LinkRenderer")

        tree = ET.ElementTree(graphml)
        tree.write(filename)

    def new():
        qgv.engine.graph = Graph("MainGraph")
        qgv.build()
        qgv.repaint()

    def load():
        fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.json")
        if (fname[0] != ""):
            qgv.loadAJson(fname[0])

    def add_node():
        newNodeID = getNextNodeID()
        dlg = QDialog()
        dlg.setWindowTitle('Add New Node')
        dlg.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.WindowTitleHint|QtCore.Qt.CustomizeWindowHint) #remove close button
        dlg.ok = False
        dlg.OK = True
        dlg.node_name = ""
        dlg.node_time = ""
        dlg.node_desc = ""
        dlg.node_img = ""
        dlg.node_team = ""
        # Layouts
        main_layout = QVBoxLayout()
        l = QFormLayout()
        buttons_layout = QHBoxLayout()

        main_layout.addLayout(l)
        main_layout.addLayout(buttons_layout)
        dlg.setLayout(main_layout)

        leNodeName = QLineEdit()
        leNodeTime = QLineEdit()
        leNodeDesc = QLineEdit()
        cbxNodeType = QComboBox()
        leImagePath = QLineEdit()

        pbOK = QPushButton()
        pbCancel = QPushButton()

        cbxNodeType.addItems(["red", "blue", "white"])
        pbOK.setText("&OK")
        pbCancel.setText("&Cancel")

        l.setWidget(0, QFormLayout.LabelRole, QLabel("Node ID"))
        l.setWidget(0, QFormLayout.FieldRole, QLabel(newNodeID))
        l.setWidget(1, QFormLayout.LabelRole, QLabel("Node Name"))
        l.setWidget(1, QFormLayout.FieldRole, leNodeName)
        l.setWidget(2, QFormLayout.LabelRole, QLabel("Node Time-Stamp"))
        l.setWidget(2, QFormLayout.FieldRole, leNodeTime)
        l.setWidget(3, QFormLayout.LabelRole, QLabel("Node Description"))
        l.setWidget(3, QFormLayout.FieldRole, leNodeDesc)
        l.setWidget(4, QFormLayout.LabelRole, QLabel("Node Team"))
        l.setWidget(4, QFormLayout.FieldRole, cbxNodeType)
        l.setWidget(5, QFormLayout.LabelRole, QLabel("Icon Image"))
        l.setWidget(5, QFormLayout.FieldRole, leImagePath)

        def ok():
            dlg.OK = True
            dlg.node_name = leNodeName.text()
            dlg.node_time = leNodeTime.text()
            dlg.node_desc = leNodeDesc.text()
            dlg.node_img = ""
            if (leImagePath.text()):
                dlg.node_img = leImagePath.text()
            dlg.node_team = cbxNodeType.currentText()
            dlg.close()

        def cancel():
            dlg.OK = False
            dlg.close()

        pbOK.clicked.connect(ok)
        pbCancel.clicked.connect(cancel)

        buttons_layout.addWidget(pbOK)
        buttons_layout.addWidget(pbCancel)
        dlg.exec_()

        # Adds new node to node Dictionary and graph if OK is selected
        if dlg.OK:
            # Add node to Dictionary
            nodeDic[newNodeID] = {
                "name": dlg.node_name,
                "team": dlg.node_team,
                "time": dlg.node_time,
                "description": dlg.node_desc
            }
            # Add node to graph
            nodeText = ""
            if (showNodeID):
                nodeText += newNodeID
            if (showNodeName and nodeDic[newNodeID]["name"] != ""):
                nodeText += "\n" + nodeDic[newNodeID]["name"]
            if (showNodeTime and nodeDic[newNodeID]["time"] != ""):
                nodeText += "\n" + nodeDic[newNodeID]["time"]
            if (showNodeDesc and nodeDic[newNodeID]["description"] != ""):
                nodeText += "\n" + nodeDic[newNodeID]["description"]
            if (dlg.node_img != ""):
                team = dlg.node_img
            elif(dlg.node_team == "red"):
                team = redTeamIcon
            elif (dlg.node_team == "blue"):
                team = blueTeamIcon
            else:
                team = whiteTeamIcon
            nodeDic[newNodeID]["node"] = qgv.addNode(qgv.engine.graph, newNodeID, label=" ", text=nodeText, shape=team)

            print("Added new node with NodeID: " + newNodeID)
            qgv.build()

    def edit_node(node):
        nodeID = node.getID()
        dlg = QDialog()
        dlg.setWindowTitle('Edit Node')
        dlg.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)  # remove close button
        dlg.ok = False
        dlg.OK = True
        dlg.node_name = ""
        dlg.node_time = ""
        dlg.node_desc = ""
        dlg.node_img = ""
        dlg.node_team = ""
        # Layouts
        main_layout = QVBoxLayout()
        l = QFormLayout()
        buttons_layout = QHBoxLayout()
        main_layout.addLayout(l)
        main_layout.addLayout(buttons_layout)
        dlg.setLayout(main_layout)

        if (nodeDic[nodeID]["name"]):
            leNodeName = QLineEdit(nodeDic[nodeID]["name"])
        else:
            leNodeName = QLineEdit()
        if (nodeDic[nodeID]["time"]):
            leNodeTime = QLineEdit(nodeDic[nodeID]["time"])
        else:
            leNodeTime = QLineEdit()
        if (nodeDic[nodeID]["description"]):
            leNodeDesc = QLineEdit(nodeDic[nodeID]["description"])
        else:
            leNodeDesc = QLineEdit()
        cbxNodeType = QComboBox()

        icon = node.getIcon()
        # If there is a custom icon directory set, show it, else leave blank for default icon
        if (icon != redTeamIcon and icon != blueTeamIcon and icon != whiteTeamIcon):
            leImagePath = QLineEdit(icon)
        else:
            leImagePath = QLineEdit()
        pbOK = QPushButton()
        pbCancel = QPushButton()

        # Place current node's team as the first selection in the comboBox
        if (nodeDic[nodeID]["team"] == "blue"):
            cbxNodeType.addItems(["blue", "red", "white"])
        elif (nodeDic[nodeID]["team"] == "white"):
            cbxNodeType.addItems(["white", "blue", "red"])
        else:
            cbxNodeType.addItems(["red", "blue", "white"])
        pbOK.setText("&OK")
        pbCancel.setText("&Cancel")

        l.setWidget(0, QFormLayout.LabelRole, QLabel("Node ID"))
        l.setWidget(0, QFormLayout.FieldRole, QLabel(nodeID))
        l.setWidget(1, QFormLayout.LabelRole, QLabel("Node Name"))
        l.setWidget(1, QFormLayout.FieldRole, leNodeName)
        l.setWidget(2, QFormLayout.LabelRole, QLabel("Node Time-Stamp"))
        l.setWidget(2, QFormLayout.FieldRole, leNodeTime)
        l.setWidget(3, QFormLayout.LabelRole, QLabel("Node Description"))
        l.setWidget(3, QFormLayout.FieldRole, leNodeDesc)
        l.setWidget(4, QFormLayout.LabelRole, QLabel("Node Team"))
        l.setWidget(4, QFormLayout.FieldRole, cbxNodeType)
        l.setWidget(5, QFormLayout.LabelRole, QLabel("Icon Image"))
        l.setWidget(5, QFormLayout.FieldRole, leImagePath)

        def ok():
            dlg.OK = True
            dlg.node_name = leNodeName.text()
            dlg.node_time = leNodeTime.text()
            dlg.node_desc = leNodeDesc.text()
            dlg.node_img = ""
            if (leImagePath.text()):
                dlg.node_img = leImagePath.text()
            dlg.node_team = cbxNodeType.currentText()
            dlg.close()

        def cancel():
            dlg.OK = False
            dlg.close()

        pbOK.clicked.connect(ok)
        pbCancel.clicked.connect(cancel)

        buttons_layout.addWidget(pbOK)
        buttons_layout.addWidget(pbCancel)
        dlg.exec_()

        # Adds changes to node Dictionary and graph if OK is selected
        if dlg.OK:
            # Edit node in Dictionary
            nodeDic[nodeID] = {
                "name": dlg.node_name,
                "team": dlg.node_team,
                "time": dlg.node_time,
                "description": dlg.node_desc
            }
            # Edit node in graph
            nodeText = ""
            if (showNodeID):
                nodeText += newNodeID
            if (showNodeName and dlg.node_name != ""):
                nodeText += "\n" + dlg.node_name
            if (showNodeTime and dlg.node_time != ""):
                nodeText += "\n" + dlg.node_time
            if (showNodeDesc and dlg.node_desc != ""):
                nodeText += "\n" + dlg.node_desc
            if (dlg.node_img != ""):
                team = dlg.node_img
            elif (dlg.node_team == "red"):
                team = redTeamIcon
            elif (dlg.node_team == "blue"):
                team = blueTeamIcon
            else:
                team = whiteTeamIcon
            node.setText(nodeText)
            node.setIcon(team)

            print("Edited node with NodeID: " + nodeID)
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

    # Add buttons
    #btnNew = QPushButton("New")
    #btnNew.clicked.connect(new)

    btnOpen = QPushButton("Open")
    btnOpen.clicked.connect(load)

    btnSave = QPushButton("Save")
    btnSave.clicked.connect(save)

    #hpanel.addWidget(btnNew)
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

    w.showMaximized()

    sys.exit(app.exec_())