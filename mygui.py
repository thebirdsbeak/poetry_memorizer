# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 811, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.poemdisplay = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.poemdisplay.setObjectName("poemdisplay")
        self.verticalLayout.addWidget(self.poemdisplay)
        self.lineentry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineentry.setObjectName("lineentry")
        self.verticalLayout.addWidget(self.lineentry)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.poemname = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.poemname.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.poemname.setObjectName("poemname")
        self.verticalLayout.addWidget(self.poemname)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 471, 811, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.display_mode = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.display_mode.setObjectName("display_mode")
        self.gridLayout_2.addWidget(self.display_mode, 1, 2, 1, 1)
        self.poem_progress = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.poem_progress.setProperty("value", 0)
        self.poem_progress.setObjectName("poem_progress")
        self.gridLayout_2.addWidget(self.poem_progress, 1, 7, 1, 1)
        self.progess_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.progess_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progess_label.setObjectName("progess_label")
        self.gridLayout_2.addWidget(self.progess_label, 2, 7, 1, 1)
        self.hide = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.hide.setObjectName("hide")
        self.gridLayout_2.addWidget(self.hide, 1, 3, 1, 1)
        self.line_nos = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.line_nos.setObjectName("line_nos")
        self.gridLayout_2.addWidget(self.line_nos, 1, 1, 1, 1)
        self.voiceover = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.voiceover.setObjectName("voiceover")
        self.gridLayout_2.addWidget(self.voiceover, 2, 2, 1, 1)
        self.obfuscator = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.obfuscator.setMaximum(5)
        self.obfuscator.setOrientation(QtCore.Qt.Horizontal)
        self.obfuscator.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.obfuscator.setTickInterval(1)
        self.obfuscator.setObjectName("obfuscator")
        self.gridLayout_2.addWidget(self.obfuscator, 1, 0, 1, 1)
        self.timerLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.timerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timerLabel.setObjectName("timerLabel")
        self.gridLayout_2.addWidget(self.timerLabel, 5, 3, 1, 1)
        self.wpmLcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.wpmLcd.setObjectName("wpmLcd")
        self.gridLayout_2.addWidget(self.wpmLcd, 4, 1, 1, 1)
        self.refresh = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.refresh.setObjectName("refresh")
        self.gridLayout_2.addWidget(self.refresh, 2, 1, 1, 1)
        self.timerLcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.timerLcd.setObjectName("timerLcd")
        self.gridLayout_2.addWidget(self.timerLcd, 4, 3, 1, 1)
        self.randomButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.randomButton.setObjectName("randomButton")
        self.gridLayout_2.addWidget(self.randomButton, 2, 3, 1, 1)
        self.saveTimeButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.saveTimeButton.setObjectName("saveTimeButton")
        self.gridLayout_2.addWidget(self.saveTimeButton, 5, 2, 1, 1)
        self.wpmLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.wpmLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.wpmLabel.setObjectName("wpmLabel")
        self.gridLayout_2.addWidget(self.wpmLabel, 5, 1, 1, 1)
        self.startTimeButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.startTimeButton.setObjectName("startTimeButton")
        self.gridLayout_2.addWidget(self.startTimeButton, 4, 2, 1, 1)
        self.missing_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.missing_label.setAlignment(QtCore.Qt.AlignCenter)
        self.missing_label.setObjectName("missing_label")
        self.gridLayout_2.addWidget(self.missing_label, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.footer_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.footer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.footer_label.setObjectName("footer_label")
        self.gridLayout_5.addWidget(self.footer_label, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 28))
        self.menubar.setObjectName("menubar")
        self.menuLexpad = QtWidgets.QMenu(self.menubar)
        self.menuLexpad.setObjectName("menuLexpad")
        self.menuNew_poem = QtWidgets.QMenu(self.menuLexpad)
        self.menuNew_poem.setObjectName("menuNew_poem")
        self.menuSettings = QtWidgets.QMenu(self.menuLexpad)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMove_to_learning = QtWidgets.QAction(MainWindow)
        self.actionMove_to_learning.setObjectName("actionMove_to_learning")
        self.actionMove_to_memorised = QtWidgets.QAction(MainWindow)
        self.actionMove_to_memorised.setObjectName("actionMove_to_memorised")
        self.actionNever_learn = QtWidgets.QAction(MainWindow)
        self.actionNever_learn.setObjectName("actionNever_learn")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRandom = QtWidgets.QAction(MainWindow)
        self.actionRandom.setObjectName("actionRandom")
        self.actionUse_all = QtWidgets.QAction(MainWindow)
        self.actionUse_all.setObjectName("actionUse_all")
        self.actionUse_learning = QtWidgets.QAction(MainWindow)
        self.actionUse_learning.setObjectName("actionUse_learning")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionFontIncrease = QtWidgets.QAction(MainWindow)
        self.actionFontIncrease.setObjectName("actionFontIncrease")
        self.actionFontDecrease = QtWidgets.QAction(MainWindow)
        self.actionFontDecrease.setObjectName("actionFontDecrease")
        self.menuNew_poem.addAction(self.actionOpen)
        self.menuNew_poem.addAction(self.actionRandom)
        self.menuNew_poem.addAction(self.actionNew)
        self.menuSettings.addAction(self.actionUse_all)
        self.menuSettings.addAction(self.actionUse_learning)
        self.menuLexpad.addAction(self.menuNew_poem.menuAction())
        self.menuLexpad.addAction(self.actionMove_to_learning)
        self.menuLexpad.addAction(self.actionMove_to_memorised)
        self.menuLexpad.addAction(self.actionNever_learn)
        self.menuLexpad.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuLexpad.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Poetry Memorizer"))
        self.poemname.setText(_translate("MainWindow", "No Poem Loaded"))
        self.display_mode.setText(_translate("MainWindow", "Line by Line"))
        self.progess_label.setText(_translate("MainWindow", "Progress"))
        self.hide.setText(_translate("MainWindow", "Hide"))
        self.line_nos.setText(_translate("MainWindow", "Line Nos"))
        self.voiceover.setText(_translate("MainWindow", "Read Line"))
        self.timerLabel.setText(_translate("MainWindow", "Time"))
        self.refresh.setText(_translate("MainWindow", "Refresh"))
        self.randomButton.setText(_translate("MainWindow", "Random"))
        self.saveTimeButton.setText(_translate("MainWindow", "Save Time"))
        self.wpmLabel.setText(_translate("MainWindow", "WPM"))
        self.startTimeButton.setText(_translate("MainWindow", "Start Timer"))
        self.missing_label.setText(_translate("MainWindow", "Obfuscate"))
        self.footer_label.setText(_translate("MainWindow", "(c) thebirdsbeak.com"))
        self.menuLexpad.setTitle(_translate("MainWindow", "File"))
        self.menuNew_poem.setTitle(_translate("MainWindow", "New poem"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionMove_to_learning.setText(_translate("MainWindow", "Tag as learning"))
        self.actionMove_to_memorised.setText(_translate("MainWindow", "Tag as memorized"))
        self.actionNever_learn.setText(_translate("MainWindow", "Tag as ignore"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionRandom.setText(_translate("MainWindow", "Random"))
        self.actionUse_all.setText(_translate("MainWindow", "Use all"))
        self.actionUse_learning.setText(_translate("MainWindow", "Use learning"))
        self.actionNew.setText(_translate("MainWindow", "New / Edit"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionFontIncrease.setText(_translate("MainWindow", "Font +"))
        self.actionFontDecrease.setText(_translate("MainWindow", "Font -"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

