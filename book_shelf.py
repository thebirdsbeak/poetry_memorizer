from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mygui
import viewbookshelf

class BookShelfViewer(QtWidgets.QMainWindow, viewbookshelf.Ui_MainWindow):

    ### Setup ###
    def __init__(self, parent=mygui.Ui_MainWindow):
        ''' initaliser for bookshelf view '''
        super(BookShelfViewer, self).__init__(parent)
        self.setupUi(self)
        self.load_info()

        ### Events ###
        self.closeButton.clicked.connect(self.close_bookshelf)
        self.refreshButton.clicked.connect(self.load_info)

    def load_info(self):
        # ''' clears text browsers and reloads metadata '''
        self.learningBrowser.setText("")
        self.memorizedBrowser.setText("")
        self.ignoredBrowser.setText("")
        self.unmarkedBrowser.setText("")
        with open("metadata.txt", "r") as meta_file:
            meta_contents = meta_file.readlines()
            for i in meta_contents:
                meta_datum = i.split(';')
                meta_tag = meta_datum[1]
                display_name = meta_datum[0].title()
                clean_name = display_name.replace("_", " ").replace("-", " - ").replace(".Txt", "")
                if meta_tag == "l\n":
                    self.learningBrowser.append(clean_name)
                elif meta_tag == "m\n":
                    self.memorizedBrowser.append(clean_name)
                elif meta_tag == "x\n":
                    self.ignoredBrowser.append(clean_name)
                else:
                    self.unmarkedBrowser.append(clean_name)


    def close_bookshelf(self):
        ''' Closes bookshelf window '''
        self.hide()
