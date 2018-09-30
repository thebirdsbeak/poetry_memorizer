# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newpoem.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(792, 583)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setObjectName("nameInput")
        self.gridLayout.addWidget(self.nameInput, 1, 0, 1, 1)
        self.authorInput = QtWidgets.QLineEdit(self.centralwidget)
        self.authorInput.setObjectName("authorInput")
        self.gridLayout.addWidget(self.authorInput, 2, 0, 1, 1)
        self.poemName = QtWidgets.QLabel(self.centralwidget)
        self.poemName.setObjectName("poemName")
        self.gridLayout.addWidget(self.poemName, 1, 1, 1, 1)
        self.authorName = QtWidgets.QLabel(self.centralwidget)
        self.authorName.setObjectName("authorName")
        self.gridLayout.addWidget(self.authorName, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.poemInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.poemInput.setObjectName("poemInput")
        self.gridLayout_2.addWidget(self.poemInput, 1, 0, 1, 1)
        self.poemStatus = QtWidgets.QLabel(self.centralwidget)
        self.poemStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.poemStatus.setObjectName("poemStatus")
        self.gridLayout_2.addWidget(self.poemStatus, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 20))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "New Poem"))
        self.poemName.setText(_translate("mainWindow", "Poem Name"))
        self.authorName.setText(_translate("mainWindow", "Author"))
        self.poemStatus.setText(_translate("mainWindow", "Not  Saved"))
        self.cancelButton.setText(_translate("mainWindow", "Close"))
        self.clearButton.setText(_translate("mainWindow", "Clear All"))
        self.editButton.setText(_translate("mainWindow", "Open / Edit Poem"))
        self.saveButton.setText(_translate("mainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

