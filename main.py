# .\relayControl\Scripts> .\qt5-tools.exe designer
# .\Scripts\pyuic5.exe -o main_window_ui.py relay_control.ui
import os
import sys

from PyQt5.QtWidgets import (
	QApplication, QMainWindow, QFileDialog,
	QLineEdit, QDialog, QListView, QStackedWidget, 
	QGraphicsPixmapItem, QGraphicsScene
)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
# Load UI

from PyQt5.uic import loadUi
from main_window_ui import Ui_MainWindow
from setting_windows_ui import Ui_windowSetting
from relay_lib import Relay
from multiplexer_lib import Multiplexer
import xml.etree.ElementTree as ET # Read config from xml file

# Global variable
CONFIG_FILE_PATH = r"./CONFIG.xml"

class Window_Setting(Ui_windowSetting, QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		self.connectSignalsSlotsChoosePath()

	def connectSignalsSlotsChoosePath(self):
		self.btnRelayPath.clicked.connect(self.choosePathRelay)
		self.btnMUXPath.clicked.connect(self.choosePathMUX)

	def choosePathRelay(self):
		path = self.getOpenFilesAndDirs()[0]
		try:
			self.txtRelayPath.setText(path)
		except FileNotFoundError as err:
			print("Not choose file yet. Error ", err)
	
	def choosePathMUX(self):
		path = self.getOpenFilesAndDirs()[0]
		try:
			self.txtMUXPath.setText(path)
		except FileNotFoundError as err:
			print("Not choose file yet. Error ", err)

	def getOpenFilesAndDirs(self, parent=None, caption='', directory='', 
						filter='', initialFilter='', options=None):
		def updateText(self):
			# update the contents of the line edit widget with the selected files
			selected = []
			for index in view.selectionModel().selectedRows():
				selected.append('"{}"'.format(index.data()))
			lineEdit.setText(' '.join(selected))

		dialog = QFileDialog(parent, windowTitle=caption)
		dialog.setFileMode(dialog.ExistingFiles)
		if options:
			dialog.setOptions(options)
		dialog.setOption(dialog.DontUseNativeDialog, True)
		if directory:
			dialog.setDirectory(directory)
		if filter:
			dialog.setNameFilter(filter)
			if initialFilter:
				dialog.selectNameFilter(initialFilter)

		# by default, if a directory is opened in file listing mode, 
		# QFileDialog.accept() shows the contents of that directory, but we 
		# need to be able to "open" directories as we can do with files, so we 
		# just override accept() with the default QDialog implementation which 
		# will just return exec_()
		dialog.accept = lambda: QDialog.accept(dialog)

		# there are many item views in a non-native dialog, but the ones displaying 
		# the actual contents are created inside a QStackedWidget; they are a 
		# QTreeView and a QListView, and the tree is only used when the 
		# viewMode is set to QFileDialog.Details, which is not this case
		stackedWidget = dialog.findChild(QStackedWidget)
		view = stackedWidget.findChild(QListView)
		view.selectionModel().selectionChanged.connect(updateText)

		lineEdit = dialog.findChild(QLineEdit)
		# clear the line edit contents whenever the current directory changes
		dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

		dialog.exec_()
		return dialog.selectedFiles()

class Window(Ui_MainWindow, QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.settingWin = Window_Setting()
		#self.setFixedSize(485, 705)
		self.setupUi(self)
		self.myRelay = Relay()
		self.myMUX = Multiplexer()
		self.get_config(CONFIG_FILE_PATH)
		self.connectSignalsSlots()
		self.txtCurrentState.setText(str(self.myRelay.curr_state))

	def get_config(self, config_file):
		if os.path.exists(config_file):
			try:
				tree = ET.parse(config_file) 
				root = tree.getroot()
				self.myMUX.mux_command_path = root.find('mux').find('bin_path').text
				self.myRelay.relay_command_path = root.find('relay').find('bin_path').text
				# Set label relay
				relay_labels = {}
				for i in range(1, self.myRelay.MAX_PIN + 1):
					relay_labels[f'pin_{i}'] = root.find('relay').find(f'pin_{i}').text.strip()
				
				print("[Relay] Read relay lable: ", relay_labels)
				
				lable_pin_dic = {
					1: self.lblNum1, 2: self.lblNum2, 3: self.lblNum3, 4: self.lblNum4,
				   	5: self.lblNum5, 6: self.lblNum6, 7: self.lblNum7, 8: self.lblNum8 
				}
				
				for i in range(1, Relay.MAX_PIN + 1):
					if relay_labels[f'pin_{i}'] != "None" and relay_labels[f'pin_{i}'] != "":
						lable_pin_dic[i].setText(relay_labels[f'pin_{i}'])
					else: pass
			except Exception as err:
				print(f"Error: {err}")
				print("An error occurs! Please check the path and content of config file.")
		else:
			print("Path's config file is invalid! It's not a file!")

	def connectSignalsSlots(self):
		self.txtCurrentState.textChanged.connect(self.updateCurrentState)
		self.connectRelayPins()
		self.menuExit.triggered.connect(self.exit)

		self.menuSetting.triggered.connect(self.show_setting)
		
		# GMVCU function
		self.btnMUXFlashMode.clicked.connect(lambda: self.switch_mux("flash"))
		self.btnMUXTestingMode.clicked.connect(lambda: self.switch_mux("normal"))


	def switch_mux(self, mode):
		if mode == "flash":
			self.log("[GMVCU][MUX] Switch to flashing mode")
			image_path = r".\resource\mode1.png"
			self.myMUX.switch_to_flash_mode_gmvcu()
		elif mode == "normal":
			self.log("[GMVCU][MUX] Switch to testing / ssh mode")
			image_path = r".\resource\mode2.png"
			self.myMUX.switch_to_normal_mode_gmvcu()
		else:
			self.log("Input mode is invalid!")
			return
		# Show MUX images :) 
		if os.path.isfile(image_path):
			scene = QGraphicsScene(self)
			pixmap = QPixmap(image_path)
			item = QGraphicsPixmapItem(pixmap)
			scene.addItem(item)
			self.graphicsViewMUX.setScene(scene)

			# # Fit image in graphic view but image have been broken a litle bit :(
			# # 3 lines below is apply with big size image
			# img_aspect_ratio =  int(pixmap.size().width()) / pixmap.size().height() 
			# width = self.graphicsViewMUX.size().width()
			# self.graphicsViewMUX.setFixedHeight( int(width / img_aspect_ratio))
			self.graphicsViewMUX.fitInView(scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
		else:
			self.log("[GMVCU][MUX] Wrong image path!")

	def connectRelayPins(self):
		self.cb1.stateChanged.connect(lambda : self.pinStateChanged(self.cb1.checkState(), pin=1))
		self.cb2.stateChanged.connect(lambda : self.pinStateChanged(self.cb2.checkState(), pin=2))
		self.cb3.stateChanged.connect(lambda : self.pinStateChanged(self.cb3.checkState(), pin=3))
		self.cb4.stateChanged.connect(lambda : self.pinStateChanged(self.cb4.checkState(), pin=4))
		self.cb5.stateChanged.connect(lambda : self.pinStateChanged(self.cb5.checkState(), pin=5))
		self.cb6.stateChanged.connect(lambda : self.pinStateChanged(self.cb6.checkState(), pin=6))
		self.cb7.stateChanged.connect(lambda : self.pinStateChanged(self.cb7.checkState(), pin=7))
		self.cb8.stateChanged.connect(lambda : self.pinStateChanged(self.cb8.checkState(), pin=8))

	def updateCurrentState(self):
		try:
			# Get current state
			state = self.myRelay.curr_state
			# Convert int -> binary and display on LCD
			self.lcdBinState.display(format(state, '08b')) # display 8 bit
		except ValueError as err:
			self.log("Value of current state is invalid! \
				accept number only and valid range is [0, 255]). Detail error: " + str(err))
	
	def pinStateChanged(self, state, pin):
		lable_pin_dic = {
					1: self.lblNum1, 2: self.lblNum2, 3: self.lblNum3, 4: self.lblNum4,
				   	5: self.lblNum5, 6: self.lblNum6, 7: self.lblNum7, 8: self.lblNum8 
		}
		if state == QtCore.Qt.Checked:
			self.myRelay.connectPin(pin)
			lable_pin_dic[pin].setStyleSheet("color: rgb(255, 0, 0);")
		else:
			self.myRelay.disconnectPin(pin)
			lable_pin_dic[pin].setStyleSheet("color: rgb(0, 0, 0);")
		self.updateState()

	def updateState(self):
		self.txtCurrentState.setText(str(self.myRelay.curr_state))

	def clearAllRelayPins(self):
		self.cb1.setChecked(False)
		self.cb2.setChecked(False)
		self.cb3.setChecked(False)
		self.cb4.setChecked(False)
		self.cb5.setChecked(False)
		self.cb6.setChecked(False)
		self.cb7.setChecked(False)
		self.cb8.setChecked(False)
	
	def log(self, message):
		self.txtLog.appendPlainText(message)
	
	def exit(self):
		sys.exit()
	
	def show_setting(self):
		self.settingWin.show()
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec())
