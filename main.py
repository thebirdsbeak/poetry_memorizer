from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import time
from subprocess import call
from random import choice, shuffle
import mygui
from poem_editor import NewPoem
from book_shelf import BookShelfViewer


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
        self.font_value = 14
        self.poemdisplay.setStyleSheet("font-size: 14px")

    ### Settings ###
        self.poemdisplay.setText("""Welcome to poetry memorizer!\n\n\
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
""")
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
        self.stopTimeButton.setEnabled(False)
        self.activate_buttons(False)
        self.dialog = NewPoem(self)
        self.books = BookShelfViewer(self)
        self.wpm = float
        self.poem_buffer = []
        self.bookshelf_flag = "a"
        self.stanza_tracker = []


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
        self.stopTimeButton.clicked.connect(self.stop_timer)
        self.actionUse_all_2.triggered.connect(self.use_all_poems)
        self.actionUse_learning_2.triggered.connect(self.use_learning_poems)
        self.actionUse_memorized.triggered.connect(self.use_memorized_poems)
        self.actionView_bookshelf.triggered.connect(self.view_bookshelf)
        self.action_Fontminus.triggered.connect(self.decrease_font)
        self.action_Fontplus.triggered.connect(self.increase_font)
        self.spinBoxStart.valueChanged.connect(self.stanza_start)
        self.spinBoxEnd.valueChanged.connect(self.stanza_end)


    def keyPressEvent(self, e):
        global current_poem
        # Always enabled functions
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif e.key() == QtCore.Qt.Key_R:
            self.random_poem()
        elif e.key() == QtCore.Qt.Key_N:
            self.new_poem()
        elif e.key() == QtCore.Qt.Key_O:
            self.open_poem()
        elif e.key() == QtCore.Qt.Key_Plus:
            self.increase_font()
        elif e.key() == QtCore.Qt.Key_Minus:
            self.decrease_font()
        elif e.key() == QtCore.Qt.Key_B:
            self.view_bookshelf()
        # Sometimes enabled functions
        elif e.key() == QtCore.Qt.Key_H:
            if self.hide.isEnabled():
               self.toggle_hide()
        elif e.key() == QtCore.Qt.Key_T:
            if self.startTimeButton.isEnabled():
               self.timer()
        elif e.key() == QtCore.Qt.Key_L:
            if self.display_mode.isEnabled():
               self.toggle_display_mode()
        elif e.key() == QtCore.Qt.Key_G:
            if self.voiceover.isEnabled():
               self.voice_over()
        elif e.key() == QtCore.Qt.Key_Asterisk:
            if self.line_nos.isEnabled():
               self.toggle_line_nos()
        elif e.key() == QtCore.Qt.Key_S:
            if self.refresh.isEnabled():
               self.refresh_poem()
        elif e.key() == QtCore.Qt.Key_K:
            if self.stopTimeButton.isEnabled():
                   self.stop_timer()
        elif e.key() == QtCore.Qt.Key_1:
            if self.refresh.isEnabled():
                step_value = self.spinBoxStart.value() - 1
                self.spinBoxStart.setValue(step_value)
        elif e.key() == QtCore.Qt.Key_2:
            if self.refresh.isEnabled():
                step_value = self.spinBoxStart.value() + 1
                self.spinBoxStart.setValue(step_value)
        elif e.key() == QtCore.Qt.Key_3:
            if self.refresh.isEnabled():
               step_value = self.spinBoxEnd.value() - 1
               self.spinBoxEnd.setValue(step_value)
        elif e.key() == QtCore.Qt.Key_4:
            if self.refresh.isEnabled():
                step_value = self.spinBoxEnd.value() + 1
                self.spinBoxEnd.setValue(step_value)


    ### Launchers ###

    def view_bookshelf(self):
        ''' Opens bookshelf dialogue '''
        self.books.show()


    def new_poem(self):
        ''' handler for new poem window '''
        self.dialog.show()


    ### States ###

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


    ### Utilities ###

    def decrease_font(self):
        '''Decrease font size'''
        self.font_value -= 1
        value_string = "font-size: {}px".format(str(self.font_value))
        self.poemdisplay.setStyleSheet(value_string)


    def increase_font(self):
        '''Increase font size'''
        self.font_value += 1
        value_string = "font-size: {}px".format(str(self.font_value))
        self.poemdisplay.setStyleSheet(value_string)


    def update_name(self, new_name):
        '''updates the name of the poem'''
        global poem_name
        poem_name = new_name.replace("_", " ").replace(".txt", "").replace("-", " - ")
        self.poemname.setText(poem_name.title())
        poem_name = new_name


    ### Timer ###

    def stop_timer(self):
        ''' stops timer '''
        self.wpmLcd.display(0)
        self.timerLcd.display(0)
        self.startTimeButton.setText("Start Timer")
        self.timer_enabled = False
        self.startTimeButton.setStyleSheet("background-color: ")
        self.stopTimeButton.setStyleSheet("background-color: ")
        self.stopTimeButton.setEnabled(False)

    def timer(self):
        ''' starts / restarts timer '''
        self.refresh_poem()
        self.poem_buffer = []
        self.wpmLcd.display(0)
        self.timerLcd.display(0)
        self.startTimeButton.setText("Restart")
        self.timer_enabled = True
        self.stopTimeButton.setEnabled(True)
        self.stopTimeButton.setStyleSheet("background-color: #ff666b; color:black;")
        self.startTimeButton.setStyleSheet("background-color: #99ff99; color:black;")
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


   ### Toggles ###

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
            self.display_mode.setText("Hide line")
            self.display_toggle = False
            self.print_current_poem()
        else:
            self.display_toggle = True
            self.display_mode.setText("Show line")
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

    ### Loading poems ###

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
            stanza_list = []
            counter = 1
            for i in current_poem:
                if i[1] == "\n":
                    stanza_list.append([i[0],i[1], counter])
                    counter += 1
                else:
                    stanza_list.append([i[0], i[1], counter])
            current_poem = stanza_list
        self.progress_whole = len(current_poem)
        self.get_stanzas()
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
            stanza_list = []
            counter = 1
            for i in current_poem:
                if i[1] == "\n":
                    stanza_list.append([i[0],i[1], counter])
                    counter += 1
                else:
                    stanza_list.append([i[0], i[1], counter])
            current_poem = stanza_list
            self.progress_whole = len(current_poem)
            self.get_stanzas()
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
            stanza_list = []
            counter = 1
            for i in current_poem:
                if i[1] == "\n":
                    stanza_list.append([i[0],i[1], counter])
                    counter += 1
                else:
                    stanza_list.append([i[0], i[1], counter])
            current_poem = stanza_list
            self.progress_whole = len(current_poem)
            self.get_stanzas()
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
            stanza_list = []
            counter = 1
            for i in current_poem:
                if i[1] == "\n":
                    stanza_list.append([i[0],i[1], counter])
                    counter += 1
                else:
                    stanza_list.append([i[0], i[1], counter])
            current_poem = stanza_list
            self.progress_whole = len(current_poem)
            self.get_stanzas()
            self.print_current_poem()


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
            stanza_list = []
            counter = 1
            for i in current_poem:
                if i[1] == "\n":
                    stanza_list.append([i[0],i[1], counter])
                    counter += 1
                else:
                    stanza_list.append([i[0], i[1], counter])
            current_poem = stanza_list
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

        stanza_list = []
        counter = 1
        for i in current_poem:
            if i[1] == "\n":
                stanza_list.append([i[0],i[1], counter])
                counter += 1
            else:
                stanza_list.append([i[0], i[1], counter])
        current_poem = stanza_list

        temp_poem = []
        numlist = [i for i in range(self.stanza_tracker[0], self.stanza_tracker[1] + 1)]
        for x in current_poem:
            if x[2] in numlist:
                temp_poem.append(x)
        current_poem = temp_poem
        backup_poem = temp_poem


        gain = self.obfuscator.value()
        roullette_wheel = ["Hit", "Miss", "Miss", "Miss", "Miss"]
        if gain > 0:
            self.obfusc_flag = True
            for i in current_poem:
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
                obfuscated_poem.append([i[0], obfuscated_string, i[2]])
            current_poem = obfuscated_poem
            obfuscated_poem = backup_poem
            self.print_current_poem()
        else:
            self.obfusc_flag = False
            self.print_current_poem()


    ### Stanzas ###

    def stanza_start(self):
        global current_poem
        self.spinBoxEnd.setMinimum(self.spinBoxStart.value())
        self.stanza_tracker = [self.spinBoxStart.value(), self.spinBoxEnd.value()]
        self.refresh_poem()
        self.progress_whole = len(current_poem)
        self.print_current_poem()


    def stanza_end(self):
        global current_poem
        self.stanza_tracker = [self.spinBoxStart.value(), self.spinBoxEnd.value()]
        self.refresh_poem()
        self.progress_whole = len(current_poem)
        self.print_current_poem()

    def get_stanzas(self):
        '''  Mins and maxes stanzas on newly opened poem '''
        global current_poem
        poem_string = ""
        for i in current_poem:
            poem_string += i[1]
        stanzas = poem_string.split("\n\n")
        numstanzas = len(stanzas)
        self.spinBoxEnd.setMaximum(numstanzas)
        self.spinBoxEnd.setMinimum(1)
        self.spinBoxEnd.setValue(numstanzas)
        self.spinBoxStart.setMaximum(numstanzas)
        self.spinBoxStart.setMinimum(1)
        self.stanza_tracker = [1, numstanzas]


    ### Print ###

    def print_current_poem(self):
        ''' Prints the current poem on screen '''
        self.lineentry.setFocus()
        global current_poem
        self.poemdisplay.setText("")
        self.activate_buttons(True)
        temp_poem = []
        if len(current_poem) > 0:
            numlist = [i for i in range(self.stanza_tracker[0], self.stanza_tracker[1] + 1)]
            for x in current_poem:
                if x[2] in numlist:
                    temp_poem.append(x)
            current_poem = temp_poem
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

        else:
            return


    ### Business end ###

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

                    if current_progress == 1:
                        if current_poem[0][1] == "\n":
                            self.poem_progress.setValue(100)
                        else:
                            self.poem_progress.setProperty("value", progress)
                    else:
                        self.poem_progress.setProperty("value", progress)
                    self.poemdisplay.setText("")
                    self.lineentry.setText("")
                    self.print_current_poem()


            else:
                if entered_text == str(obfuscated_poem[0][1].strip()):
                    if self.timer_enabled == True:
                        self.get_wpm(current_line)
                    del current_poem[0]
                    del obfuscated_poem[0]
                    current_progress = len(current_poem)
                    progress = int(((self.progress_whole - current_progress)/self.progress_whole) * 100)
                    if current_progress == 1:
                        print(obfuscated_poem)
                        if obfuscated_poem[0][1] == "\n":
                            self.poem_progress.setValue(100)
                        else:
                            self.poem_progress.setProperty("value", progress)
                    else:
                        self.poem_progress.setProperty("value", progress)
                    self.poemdisplay.setText("")
                    self.lineentry.setText("")
                    self.print_current_poem()


    def chicken_dinner(self):
        ''' Triggers events on completion of poem entry '''
        if self.poem_progress.value() == 100:
            if self.timer_enabled == True:
                self.final_time = time.time() - self.timer_var
                self.timerLcd.display(self.final_time)
            self.startTimeButton.setStyleSheet("background-color:")
            self.timer_enabled = False
            self.footer_label.setText("Well done! Restart to go again.")

### Launch ###
app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()


