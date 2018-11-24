from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from designfiles import mygui
from designfiles import viewshortcuts

class ShortcutViewer(QtWidgets.QMainWindow, viewshortcuts.Ui_MainWindow):

    ### Setup ###
    def __init__(self, parent=mygui.Ui_MainWindow):
        ''' initaliser for bookshelf view '''
        super(ShortcutViewer, self).__init__(parent)
        self.setupUi(self)
        self.textBrowser.setText("""Welcome to poetry memorizer!\n\n\
Open a poem, then enter each line until complete. Try the different toggles to increase the difficulty as you advance.

Hotkeys:
Ctrl S  - Restart poem
Ctrl T  - Start / restart timer
Ctrl R  - Random Poem
Ctrl O  - Open Poem from file
Ctrl N  - New / Edit poem
Ctrl L  - Hide / Show line
Ctrl H  - Hide / Show all
Ctrl G  - Read line aloud
Ctrl B  - Open Bookshelf
Ctrl 1  - Decrement starting stanza
Ctrl 2  - Increment starting stanza
Ctrl 3  - Decrement ending stanza
Ctrl 4  - Increment ending stanza
Ctrl *  - Toggle line numbers
Ctrl +  - Increase font size
Ctrl -  - Decrease font size
Esc     - Close poetry memorizer
Ctrl ?  - Show shortcuts"""
)
        self.pushButton.clicked.connect(self.close_shortcuts)

    def keyPressEvent(self, e):
        ''' Keypress events to close window '''
        if e.key() == QtCore.Qt.Key_Escape:
            self.hide()

    def close_shortcuts(self):
        ''' Closes bookshelf window '''
        self.hide()
