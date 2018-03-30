# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newpoem.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 801, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nameInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.nameInput.setObjectName("nameInput")
        self.gridLayout.addWidget(self.nameInput, 0, 0, 1, 1)
        self.authorInput = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.authorInput.setObjectName("authorInput")
        self.gridLayout.addWidget(self.authorInput, 1, 0, 1, 1)
        self.poemName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.poemName.setObjectName("poemName")
        self.gridLayout.addWidget(self.poemName, 0, 1, 1, 1)
        self.authorName = QtWidgets.QLabel(self.gridLayoutWidget)
        self.authorName.setObjectName("authorName")
        self.gridLayout.addWidget(self.authorName, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 120, 801, 341))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.poemInput = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.poemInput.setObjectName("poemInput")
        self.gridLayout_2.addWidget(self.poemInput, 1, 0, 1, 1)
        self.poemStatus = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.poemStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.poemStatus.setObjectName("poemStatus")
        self.gridLayout_2.addWidget(self.poemStatus, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 460, 801, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.poemName.setText(_translate("MainWindow", "TextLabel"))
        self.authorName.setText(_translate("MainWindow", "TextLabel"))
        self.poemStatus.setText(_translate("MainWindow", "Not  Saved"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.saveButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

