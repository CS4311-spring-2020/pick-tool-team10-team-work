from PyQt5.QtWidgets import QFileDialog, QWidget

class DirDialog:
    def dir_dialog(self, dialogtitle):
        widget = QFileDialog()
        filename = QFileDialog.getExistingDirectory(widget, dialogtitle)
        return filename