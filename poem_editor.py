from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import newpoem
import mygui


class NewPoem(QtWidgets.QMainWindow, newpoem.Ui_mainWindow):

    ### Setup ###
    def __init__(self, parent=mygui.Ui_MainWindow):
        ''' Initialiser for new poem window '''
        super(NewPoem, self).__init__(parent)
        self.setupUi(self)
        self.nameInput.setStyleSheet("background-color:  #ff666b")
        self.authorInput.setStyleSheet("background-color:  #ff666b")
        self.poemInput.setStyleSheet("background-color:  #ff666b")

    ### Events ###
        self.nameInput.textEdited.connect(self.poem_name_input)
        self.authorInput.textEdited.connect(self.author_name_input)
        self.poemInput.textChanged.connect(self.poem_text_input)
        self.saveButton.setEnabled(False)
        self.saveButton.clicked.connect(self.save_poem)
        self.cancelButton.clicked.connect(self.cancel_new_poem)
        self.clearButton.clicked.connect(self.clear_new_poem)
        self.editButton.clicked.connect(self.edit_poem)


    def poem_name_input(self):
        ''' Triggers styling for poem name '''
        entered_text = str(self.nameInput.text())
        self.test_for_save()
        if entered_text == "":
            self.nameInput.setStyleSheet("background-color:  #ff666b")
        else:
            self.nameInput.setStyleSheet("background-color: #99ff99")


    def author_name_input(self):
        ''' Triggers styling for author name '''
        self.test_for_save()
        entered_text = str(self.authorInput.text())
        if entered_text == "":
            self.authorInput.setStyleSheet("background-color:  #ff666b")
        else:
            self.authorInput.setStyleSheet("background-color: #99ff99")


    def poem_text_input(self):
        ''' Triggers styling for poem text '''
        self.test_for_save()
        entered_text = str(self.poemInput.toPlainText())
        if entered_text == "":
            self.poemInput.setStyleSheet("background-color:  #ff666b")
        else:
            self.poemInput.setStyleSheet("background-color: ")


    def test_for_save(self):
        ''' If all new poems inputs are > 0, save button is active'''
        testname = str(self.nameInput.text())
        testauthor = str(self.authorInput.text())
        testtext = str(self.poemInput.toPlainText())
        if testname != "" and testauthor != "" and testtext != "":
            self.saveButton.setEnabled(True)
        else:
            self.saveButton.setEnabled(False)


    def clear_new_poem(self):
        self.poemInput.setPlainText("")
        self.authorInput.setText("")
        self.nameInput.setText("")
        self.poemStatus.setText("Not saved")
        self.authorInput.setStyleSheet("background-color:  #ff666b")
        self.nameInput.setStyleSheet("background-color:  #ff666b")
        self.poemInput.setStyleSheet("background-color:  #ff666b")


    def save_poem(self):
        testname = str(self.nameInput.text().strip().lower())
        testname = testname.replace(" ", "_")
        testauthor = str(self.authorInput.text().strip().lower())
        testauthor = testauthor.replace(" ", "_")
        text_to_save = str(self.poemInput.toPlainText())
        file_name = "{}-{}.txt".format(testname, testauthor)
        save_name = "./bookshelf/{}".format(file_name)
        try:
            with open(save_name, "x") as save_me:
                save_me.write(text_to_save)
            self.poemStatus.setText("Saved {}".format(file_name))
            with open("metadata.txt", "a") as meta_data:
                new_poem_meta = "{};{}".format(file_name, "u\n")
                meta_data.write(new_poem_meta)
        except FileExistsError:
            msg = QMessageBox
            overwrite = msg.question(self, 'File exists', "Overwrite poem?", QMessageBox.Yes | QMessageBox.No)
            if overwrite == QMessageBox.Yes:
                with open(save_name, "w") as save_me:
                    save_me.write(text_to_save)
                self.poemStatus.setText("Saved {}".format(file_name))


    def edit_poem(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Edit poem", "./bookshelf")
        poem = filename[0]
        poem_name = poem.split("/")[-1]
        raw_poem_name = poem_name.replace(".txt", "").title().replace("_", " ")
        formatted_poem_name = raw_poem_name.split("-")
        self.poemStatus.setText(raw_poem_name)
        self.nameInput.setText(formatted_poem_name[0])
        self.authorInput.setStyleSheet("background-color: #99ff99")
        self.nameInput.setStyleSheet("background-color: #99ff99")
        self.authorInput.setText(formatted_poem_name[1])
        with open(poem, "r") as read_poem:
            raw_poem = read_poem.read()
            self.poemInput.setPlainText(raw_poem)


    def cancel_new_poem(self):
        self.hide()
