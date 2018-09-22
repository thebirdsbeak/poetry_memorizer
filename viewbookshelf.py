# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewbookshelf.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 519)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.learningLabel = QtWidgets.QLabel(self.centralwidget)
        self.learningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.learningLabel.setObjectName("learningLabel")
        self.gridLayout.addWidget(self.learningLabel, 0, 1, 1, 1)
        self.ignoredLabel = QtWidgets.QLabel(self.centralwidget)
        self.ignoredLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ignoredLabel.setObjectName("ignoredLabel")
        self.gridLayout.addWidget(self.ignoredLabel, 2, 1, 1, 1)
        self.memorizedBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.memorizedBrowser.setObjectName("memorizedBrowser")
        self.gridLayout.addWidget(self.memorizedBrowser, 1, 0, 1, 1)
        self.learningBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.learningBrowser.setObjectName("learningBrowser")
        self.gridLayout.addWidget(self.learningBrowser, 1, 1, 1, 1)
        self.memorizedLabel = QtWidgets.QLabel(self.centralwidget)
        self.memorizedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.memorizedLabel.setObjectName("memorizedLabel")
        self.gridLayout.addWidget(self.memorizedLabel, 0, 0, 1, 1)
        self.hitlistLabel = QtWidgets.QLabel(self.centralwidget)
        self.hitlistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hitlistLabel.setObjectName("hitlistLabel")
        self.gridLayout.addWidget(self.hitlistLabel, 2, 0, 1, 1)
        self.ignoredBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.ignoredBrowser.setObjectName("ignoredBrowser")
        self.gridLayout.addWidget(self.ignoredBrowser, 3, 1, 1, 1)
        self.unmarkedBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.unmarkedBrowser.setObjectName("unmarkedBrowser")
        self.gridLayout.addWidget(self.unmarkedBrowser, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 1, 0, 1, 1)
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setObjectName("refreshButton")
        self.gridLayout_2.addWidget(self.refreshButton, 1, 1, 1, 1)
        self.closeButton.raise_()
        self.refreshButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bookshelf"))
        self.learningLabel.setText(_translate("MainWindow", "Learning"))
        self.ignoredLabel.setText(_translate("MainWindow", "Ignored"))
        self.memorizedLabel.setText(_translate("MainWindow", "Memorized"))
        self.hitlistLabel.setText(_translate("MainWindow", "Unmarked"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

