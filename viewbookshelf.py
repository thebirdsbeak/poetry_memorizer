# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewbookshelf.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.learningLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.learningLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.learningLabel.setObjectName("learningLabel")
        self.gridLayout.addWidget(self.learningLabel, 0, 1, 1, 1)
        self.ignoredLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ignoredLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ignoredLabel.setObjectName("ignoredLabel")
        self.gridLayout.addWidget(self.ignoredLabel, 2, 1, 1, 1)
        self.memorizedBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.memorizedBrowser.setObjectName("memorizedBrowser")
        self.gridLayout.addWidget(self.memorizedBrowser, 1, 0, 1, 1)
        self.learningBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.learningBrowser.setObjectName("learningBrowser")
        self.gridLayout.addWidget(self.learningBrowser, 1, 1, 1, 1)
        self.memorizedLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.memorizedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.memorizedLabel.setObjectName("memorizedLabel")
        self.gridLayout.addWidget(self.memorizedLabel, 0, 0, 1, 1)
        self.hitlistLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.hitlistLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hitlistLabel.setObjectName("hitlistLabel")
        self.gridLayout.addWidget(self.hitlistLabel, 2, 0, 1, 1)
        self.ignoredBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.ignoredBrowser.setObjectName("ignoredBrowser")
        self.gridLayout.addWidget(self.ignoredBrowser, 3, 1, 1, 1)
        self.unmarkedBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.unmarkedBrowser.setObjectName("unmarkedBrowser")
        self.gridLayout.addWidget(self.unmarkedBrowser, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 2)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(310, 470, 92, 36))
        self.closeButton.setObjectName("closeButton")
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(410, 470, 90, 36))
        self.refreshButton.setObjectName("refreshButton")
        self.closeButton.raise_()
        self.gridLayoutWidget.raise_()
        self.refreshButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 28))
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

