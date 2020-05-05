from PyQt5 import QtGui, QtCore


class UiStyle:
    checkbox_palettes = dict()
    checkbox_palettes['dark_grey'] = QtGui.QPalette()
    checkbox_palettes['dark_grey'].setColor(QtGui.QPalette.WindowText, QtCore.Qt.darkGray)
    checkbox_palettes['black'] = QtGui.QPalette()
    checkbox_palettes['black'].setColor(QtGui.QPalette.WindowText, QtCore.Qt.black)
    checkbox_palettes['dark_green'] = QtGui.QPalette()
    checkbox_palettes['dark_green'].setColor(QtGui.QPalette.WindowText, QtCore.Qt.darkGreen)
