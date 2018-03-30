from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from subprocess import call
from random import choice, shuffle
import mygui
import newpoem


class NewPoem(QtWidgets.QMainWindow, newpoem.Ui_MainWindow):
	
	def __init__(self, parent=None):
		super(NewPoem, self).__init__(parent)
		self.setupUi(self)

class MainDialog(QtWidgets.QMainWindow, mygui.Ui_MainWindow):
	
	current_poem = []
	obfuscated_poem = []	
	poem_name = ""
			
	### Setup ###
	def __init__(self, parent=None):
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)
		self.book_status = []
		self.load_metadata()
	### Settings ###
		self.line_numbers = False
		self.display_toggle = False
		self.hide_text = False
		self.obfusc_flag = False
		self.progress_whole = 0
		self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	### Actions ###
		self.poemdisplay.setText("Welcome to Learnatron-8000")
		self.lineentry.returnPressed.connect(self.enter_line)
		self.actionRandom.triggered.connect(self.random_poem)
		self.actionMove_to_memorised.triggered.connect(self.memorized_poem)
		self.actionMove_to_learning.triggered.connect(self.learn_poem)
		self.actionNever_learn.triggered.connect(self.ignore_poem)
		self.refresh.clicked.connect(self.refresh_poem)
		self.voiceover.clicked.connect(self.voice_over)
		self.line_nos.clicked.connect(self.toggle_line_nos)
		self.display_mode.clicked.connect(self.toggle_display_mode)
		self.hide.clicked.connect(self.toggle_hide)
		self.obfuscator.sliderReleased.connect(self.obfuscate_poem)
		self.poem_progress.valueChanged.connect(self.chicken_dinner)
		self.fuzzy_match.clicked.connect(self.random_poem)
		self.actionOpen.triggered.connect(self.open_poem)
		self.actionUse_all.triggered.connect(self.new_poem)
		self.dialog = NewPoem(self)

	def new_poem(self):
		self.dialog.show()

	def load_metadata(self):
		with open('./metadata.txt', 'r') as metas:
			self.book_status = metas.readlines()
			
	def memorized_poem(self):
		self.amend_book_info("m")

	def learn_poem(self):
		self.amend_book_info("l")
		
	def ignore_poem(self):
		self.amend_book_info("x")
			
	def amend_book_info(self, signal):
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
			
		### Functions ###
	def enter_line(self):
		'''Tests line against first line in current_poem'''
		global current_poem
		global obfuscated_poem
		entered_text = str(self.lineentry.text())
		if self.obfusc_flag == False:
			if entered_text == str(current_poem[0][1].strip()):
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
		'''loads random poem'''
		global current_poem
		current_poem = []
		self.poem_progress.setProperty("value", 0)
		self.poemdisplay.setText("")
		self.footer_label.setText("Keep at it, champ")
		bookshelf = []
		for i in os.listdir('./bookshelf'):
			bookshelf.append(i)
		if len(bookshelf) > 1:
			selected = choice(bookshelf)
			poem = "./{}/{}".format("/bookshelf", selected)
			self.update_name(selected)
			with open(poem, "r") as page:
				raw_poem = page.readlines()
				for index, i in enumerate(raw_poem):
					current_poem.append([index, i])
				self.progress_whole = len(current_poem)
			self.print_current_poem()
				
	def update_name(self, new_name):
		'''updates the name of the poem'''
		global poem_name
		poem_name = new_name.replace("_", " ").replace(".txt", "")
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
		'''reads first line  of current poem'''
		global current_poem
		call(["espeak", current_poem[0][1]])
		
	def toggle_line_nos(self):
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
		if self.display_toggle == True:
			self.display_mode.setText("Line by line")
			self.display_toggle = False
			self.print_current_poem()
		else:
			self.display_toggle = True
			self.display_mode.setText("Rote")
			self.print_current_poem()
	
	def toggle_hide(self):
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
		if self.poem_progress.value() == 100:
			self.footer_label.setText("Well done! Refresh to go again.")
	
app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()


