from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import time
from subprocess import call
from random import choice, shuffle
import mygui
import newpoem
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
        ''' clears text browsers and reloads metadata '''
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

    ### Functions ###

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

class MainDialog(QtWidgets.QMainWindow, mygui.Ui_MainWindow):

    ### Variables ###
    current_poem = []
    obfuscated_poem = []
    poem_name = ""

    ### Setup ###
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.book_status = []

    ### Settings ###
        self.poemdisplay.setText("Welcome to poetry memorizer!\n\n\
Open a poem, then enter each line until complete.\n\
Try the different toggles to increase the difficulty as you advance.")
        self.line_numbers = False
        self.display_toggle = False
        self.hide_text = False
        self.obfusc_flag = False
        self.progress_whole = 0
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.font_size = 12
        self.timer_var = float
        self.final_time = float
        self.timer_enabled = False
        self.actionUse_all_2.setEnabled(False)
        self.activate_buttons(False)
        self.dialog = NewPoem(self)
        self.books = BookShelfViewer(self)
        self.wpm = float
        self.poem_buffer = []
        self.bookshelf_flag = "a"

    ### Events ###
        self.lineentry.returnPressed.connect(self.enter_line)
        self.actionRandom.triggered.connect(self.random_poem)
        self.actionMove_to_memorised.triggered.connect(self.memorized_poem)
        self.actionMove_to_learning.triggered.connect(self.learn_poem)
        self.actionNever_learn.triggered.connect(self.ignore_poem)
        self.actionUntag.triggered.connect(self.untag_poem)
        self.refresh.clicked.connect(self.refresh_poem)
        self.voiceover.clicked.connect(self.voice_over)
        self.line_nos.clicked.connect(self.toggle_line_nos)
        self.display_mode.clicked.connect(self.toggle_display_mode)
        self.hide.clicked.connect(self.toggle_hide)
        self.obfuscator.sliderReleased.connect(self.obfuscate_poem)
        self.poem_progress.valueChanged.connect(self.chicken_dinner)
        self.randomButton.clicked.connect(self.random_poem)
        self.actionOpen.triggered.connect(self.open_poem)
        self.actionNew.triggered.connect(self.new_poem)
        self.startTimeButton.clicked.connect(self.timer)
        self.actionUse_all_2.triggered.connect(self.use_all_poems)
        self.actionUse_learning_2.triggered.connect(self.use_learning_poems)
        self.actionUse_memorized.triggered.connect(self.use_memorized_poems)
        self.actionView_bookshelf.triggered.connect(self.view_bookshelf)


    ### Functions ###

    def view_bookshelf(self):
        ''' Opens bookshelf dialogue '''
        self.books.show()

    def timer(self):
        ''' starts / restarts timer '''
        self.refresh_poem()
        self.poem_buffer = []
        self.wpmLcd.display(0)
        self.timerLcd.display(0)
        self.startTimeButton.setText("Restart")
        self.timer_enabled = True
        self.startTimeButton.setStyleSheet("background-color: #99ff99")
        self.timer_var = time.time()
        self.lineentry.setFocus()

    def get_timer(self):
        ''' Time elapsed since last restart '''
        current_time = time.time()
        time_delta = current_time - float(self.timer_var)
        self.timerLcd.display(time_delta)

    def get_wpm(self, signal):
        ''' returns the wpm '''
        poem_line = signal.split(" ")
        self.poem_buffer.append(poem_line)
        word_count = 0
        current_time = time.time()
        time_delta = current_time - float(self.timer_var)
        for i in self.poem_buffer:
            word_count += len(i)
        self.wpm = ((word_count + 1) / (time_delta / 60))
        self.wpmLcd.display(self.wpm)

    def activate_buttons(self, bool):
        ''' buttons only allowed when there is current poem '''
        self.hide.setEnabled(bool)
        self.refresh.setEnabled(bool)
        self.voiceover.setEnabled(bool)
        self.line_nos.setEnabled(bool)
        self.display_mode.setEnabled(bool)
        self.obfuscator.setEnabled(bool)
        self.startTimeButton.setEnabled(bool)

    def use_all_poems(self):
        self.use_which_poems(signal = "a")
        self.actionUse_memorized.setEnabled(True)
        self.actionUse_all_2.setEnabled(False)
        self.actionUse_learning_2.setEnabled(True)
        self.footer_label.setText("Using all poems")

    def use_learning_poems(self, signal):
        self.use_which_poems(signal = "l")
        self.actionUse_memorized.setEnabled(True)
        self.actionUse_learning_2.setEnabled(False)
        self.actionUse_all_2.setEnabled(True)
        self.footer_label.setText("Using learning poems")


    def use_memorized_poems(self, signal):
        self.use_which_poems(signal = "m")
        self.actionUse_memorized.setEnabled(False)
        self.actionUse_learning_2.setEnabled(True)
        self.actionUse_all_2.setEnabled(True)
        self.footer_label.setText("Using memorized poems")

    def use_which_poems(self, signal):
        self.bookshelf_flag = signal

    def new_poem(self):
        ''' handler for new poem window '''
        self.dialog.show()

    def load_metadata(self):
        ''' May be used for 'use all' etc... functionality '''
        with open('./metadata.txt', 'r') as metas:
            return metas.readlines()

    def memorized_poem(self):
        ''' Set poem metadata to memorized '''
        self.amend_book_info("m")

    def learn_poem(self):
        ''' Set poem metadata to learning '''
        self.amend_book_info("l")

    def ignore_poem(self):
        ''' Set poem metadata to ignore '''
        self.amend_book_info("x")

    def untag_poem(self):
        ''' Untag poem '''
        self.amend_book_info("u")

    def amend_book_info(self, signal):
        ''' Takes relevant signal and sets books meta status'''
        global poem_name
        try:
            new_meta = []
            catalogue = "./metadata.txt"
            with open(catalogue, "r") as metas:
                current_meta = metas.readlines()
                for i in current_meta:
                    if poem_name in i:
                        if signal == "m":
                            meta_parsed = "{};{}".format(poem_name, "m\n")
                        elif signal == "l":
                            meta_parsed = "{};{}".format(poem_name, "l\n")
                        elif signal == "x":
                            meta_parsed = "{};{}".format(poem_name, "x\n")
                        elif signal == "u":
                            meta_parsed = "{};{}".format(poem_name, "u\n")
                        else:
                            return
                    else:
                        meta_parsed = i
                    new_meta.append(meta_parsed)

            with open(catalogue, "w") as write_metas:
                for i in new_meta:
                    write_metas.write(i)
        except NameError:
            return


    def enter_line(self):
        '''Tests line against first line in current_poem'''
        global current_poem
        global obfuscated_poem
        if self.lineentry.text() == "":
            return
        elif len(current_poem) == 0:
            return
        else:
            if self.timer_enabled == True:
                self.get_timer()
            entered_text = str(self.lineentry.text())
            if str(current_poem[0][1].strip()) == "":
                del current_poem[0]
            if self.obfusc_flag == False:
                current_line = str(current_poem[0][1].strip())
                if entered_text == current_line:
                    if self.timer_enabled == True:
                        self.get_wpm(current_line)
                    del current_poem[0]
                    current_progress = len(current_poem)
                    progress = int(((self.progress_whole - current_progress)/self.progress_whole) * 100)
                    self.poem_progress.setProperty("value", progress)
                    self.poemdisplay.setText("")
                    self.lineentry.setText("")
                    self.print_current_poem()
            else:
                if entered_text == str(obfuscated_poem[0][1].strip()):
                    del current_poem[0]
                    current_progress = len(current_poem)
                    progress = int(((self.progress_whole - current_progress)/self.progress_whole) * 100)
                    self.poem_progress.setProperty("value", progress)
                    self.poemdisplay.setText("")
                    self.lineentry.setText("")
                    self.print_current_poem()

    def open_poem(self):
        ''' Load a poem from file explorer '''
        global current_poem
        current_poem = []
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Load poem", "./bookshelf")
        poem = filename[0]
        poem_name = poem.split("/")[-1]
        self.update_name(poem_name)
        with open(poem, "r") as page:
            raw_poem = page.readlines()
            for index, i in enumerate(raw_poem):
                current_poem.append([index, i])
                self.progress_whole = len(current_poem)
        self.print_current_poem()

    def random_poem(self):
        '''Loads random poem - in serious need of refactoring :( '''
        global current_poem
        current_poem = []
        self.poem_progress.setProperty("value", 0)
        self.poemdisplay.setText("")
        meta_data = self.load_metadata()
        if self.bookshelf_flag == "a":
            bookshelf = []
            for i in meta_data:
                if i.split(";")[1] != "x\n":
                    bookshelf.append(i.split(';'))
            chosen_poem = choice(bookshelf)
            with open("./bookshelf/" + str(chosen_poem[0]), "r") as page:
                self.update_name(chosen_poem[0])
                raw_poem = page.readlines()
                for index, i in enumerate(raw_poem):
                    current_poem.append([index, i])
                self.progress_whole = len(current_poem)
            self.print_current_poem()
        elif self.bookshelf_flag == "m":
            bookshelf = []
            for i in meta_data:
                if i.split(";")[1] == "m\n":
                    bookshelf.append(i.split(';'))
            chosen_poem = choice(bookshelf)
            with open("./bookshelf/" + str(chosen_poem[0]), "r") as page:
                self.update_name(chosen_poem[0])
                raw_poem = page.readlines()
                for index, i in enumerate(raw_poem):
                    current_poem.append([index, i])
                self.progress_whole = len(current_poem)
            self.print_current_poem()
        else:
            learning_choice = []
            for i in meta_data:
                if i.split(';')[1] == "l\n":
                    learning_choice.append(i.split(';'))
            chosen_poem = choice(learning_choice)
            self.update_name(chosen_poem[0])
            with open("./bookshelf/" + str(chosen_poem[0]), "r") as page:
                raw_poem = page.readlines()
                for index, i in enumerate(raw_poem):
                    current_poem.append([index, i])
                self.progress_whole = len(current_poem)
            self.print_current_poem()

    def update_name(self, new_name):
        '''updates the name of the poem'''
        global poem_name
        poem_name = new_name.replace("_", " ").replace(".txt", "").replace("-", " - ")
        self.poemname.setText(poem_name.title())
        poem_name = new_name

    def refresh_poem(self):
        '''reinstates all lines of poem'''
        global poem_name
        global current_poem
        current_poem = []
        self.poem_progress.setProperty("value", 0)
        self.poemdisplay.setText("")
        with open ("./bookshelf/"+poem_name, "r") as page:
            raw_poem = page.readlines()
            for index, i in enumerate(raw_poem):
                current_poem.append([index, i])
            self.progress_whole = len(current_poem)
        self.print_current_poem()

    def obfuscate_poem(self):
        ''' Variable obfuscator for words in poem. '''
        global obfuscated_poem
        global current_poem
        current_poem = []
        obfuscated_poem = []
        backup_poem = []
        with open ("./bookshelf/"+poem_name, "r") as page:
            raw_poem = page.readlines()
            for index, i in enumerate(raw_poem):
                current_poem.append([index, i])
                backup_poem.append([index, i])
                self.progress_whole = len(current_poem)
        gain = self.obfuscator.value()
        roullette_wheel = ["Hit", "Miss", "Miss", "Miss", "Miss"]
        if gain > 0:
            self.obfusc_flag = True
            for index, i in enumerate(current_poem):
                obfuscated_string = ""
                word_list = i[1].strip()
                word_list = word_list.split(" ")
                for x in word_list:
                    obfuscated_word = ""
                    if choice(roullette_wheel[::gain]) == "Hit":
                        l = list(x)
                        shuffle(l)
                        result = ''.join(l)
                        obfuscated_word += result
                    else:
                        obfuscated_word = x
                    obfuscated_string += obfuscated_word + " "
                obfuscated_poem.append([index, obfuscated_string])
            current_poem = obfuscated_poem
            obfuscated_poem = backup_poem
            self.print_current_poem()


        else:
            self.obfusc_flag = False
            self.print_current_poem()


    def voice_over(self):
        ''' Reads first line of current poem aloud '''
        global current_poem
        call(["espeak", current_poem[0][1]])

    def toggle_line_nos(self):
        ''' Toggles line numbers '''
        if self.line_numbers == True:
            self.line_numbers = False
            try:
                self.print_current_poem()
            except NameError:
                return
        else:
            self.line_numbers = True
            try:
                self.print_current_poem()
            except NameError:
                return

    def toggle_display_mode(self):
        ''' Toggles line by line display mode '''
        if self.display_toggle == True:
            self.display_mode.setText("Line by line")
            self.display_toggle = False
            self.print_current_poem()
        else:
            self.display_toggle = True
            self.display_mode.setText("Rote")
            self.print_current_poem()

    def toggle_hide(self):
        ''' Toggles hide text mode '''
        if self.hide_text == True:
            self.hide.setText("Hide")
            self.hide_text = False
            self.print_current_poem()
        else:
            self.hide_text = True
            self.hide.setText("Show")
            self.print_current_poem()

    def print_current_poem(self):
        ''' Prints the current poem on screen '''
        global current_poem
        self.poemdisplay.setText("")
        self.activate_buttons(True)
        if self.hide_text == True:
            for i in current_poem:
                first_string = ""
                for x in i[1]:
                    if x.lower() in self.alphabet:
                        first_string += "_"
                    else:
                        first_string += x
                if self.line_numbers == True:
                    self.poemdisplay.append("{}. {}".format(i[0]+1, first_string.strip()))
                else:
                    self.poemdisplay.append(first_string.strip())
            self.poemdisplay.verticalScrollBar().setValue(0)

        else:
            if self.display_toggle == True:
                if self.line_numbers == True:
                    first_string = ""
                    for i in current_poem[0][1]:
                        if i.lower() in self.alphabet:
                            first_string += "_"
                        else:
                            first_string += i
                    self.poemdisplay.append("{}. {}".format(current_poem[0][0]+1, first_string.strip()))
                    for i in current_poem[1::]:
                        self.poemdisplay.append("{}. {}".format(i[0]+1, i[1].strip()))
                else:
                    first_string = ""
                    for i in current_poem[0][1]:
                        if i.lower() in self.alphabet:
                            first_string += "_"
                        else:
                            first_string += i
                    self.poemdisplay.append(first_string.strip())
                    for i in current_poem[1::]:
                        self.poemdisplay.append(i[1].strip())
            else:
                for i in current_poem:
                    if self.line_numbers == True:
                        self.poemdisplay.append("{}. {}".format(i[0]+1, i[1].strip()))
                    else:
                        self.poemdisplay.append(i[1].strip())
            self.poemdisplay.verticalScrollBar().setValue(0)

    def chicken_dinner(self):
        ''' Triggers events on completion of poem entry '''
        if self.poem_progress.value() == 100:
            if self.timer_enabled == True:
                self.final_time = time.time() - self.timer_var
                self.timerLcd.display(self.final_time)
            self.startTimeButton.setStyleSheet("background-color:")
            self.timer_enabled = False
            self.footer_label.setText("Well done! Refresh to go again.")

    ### Launch ###
app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()


