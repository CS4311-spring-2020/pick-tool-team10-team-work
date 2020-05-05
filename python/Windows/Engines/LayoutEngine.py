#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget

class LayoutEngine():
    """
    An abstract main class for layout engines
    """
    def __init__(self):
        pass

    def paint(self, painter, graph):
        pass 
    
