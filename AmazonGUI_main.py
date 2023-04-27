from AmazonGUI import Ui_MainWindow

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class GUIWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == '__main__':
    app = qtw.QApplication([])

    widget = GUIWindow()
    widget.show()

    app.exec_()