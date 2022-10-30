# .\relayControl\Scripts> .\qt5-tools.exe designer
# .\Scripts\pyuic5.exe -o main_window_ui.py relay_control.ui

import os
import sys
from turtle import update
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
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
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
        self.loadRelayLabel()
        self.txtCurrentState.setText(str(self.myRelay.curr_state))

    def get_config(self, config_file):
        if os.path.isfile(config_file):
            try:
                tree = ET.parse(config_file) 
                root = tree.getroot()
                self.myMUX.MUX_COMMAND_PATH = root.find("mux").find("bin_path").text
                self.myRelay.RELAY_COMMAND_PATH = root.find("relay").find("bin_path").text
            except Exception as err:
                print(f"Error: {err}")
                print("An error occurs! Please check the path and content of config file.")
        else:
            print("Input config file is invalid! It's not a file!")

    def loadRelayLabel(self):
        self.lblNum1.setText("VBUS")
        self.lblNum3.setText("WD_OFF")
        self.lblNum4.setText("MOD_0")
        self.lblNum6.setText("IGN")
        self.lblNum7.setText("ACC")
        self.lblNum8.setText("BAT")

    def connectSignalsSlots(self):
        self.txtCurrentState.textChanged.connect(self.updateCurrentState)
        self.connectCommonMode()
        self.connectCommonFunc()
        self.connectRelayPins()
        self.connectMUXMode()
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

    def connectCommonMode(self):
        self.rbNone.toggled.connect(self.checkedNone)
        self.rbNormalMode.toggled.connect(self.checkedNormalMode)
        self.rbAurixMode.toggled.connect(self.checkedAurixMode)
        self.rbAndroidMode.toggled.connect(self.checkedAndroidMode)
    
    def connectCommonFunc(self):
        self.btnTargetOff.clicked.connect(self.turnOffTarget)
        self.btnTargetRestart.clicked.connect(self.restartTarget)
        self.btnACC_IGN_on.clicked.connect(self.turnOnACC_IGN)

    def connectRelayPins(self):
        self.cb1.stateChanged.connect(self.VBUSStateChanged)
        self.cb3.stateChanged.connect(self.WD_OFFStateChanged)
        self.cb4.stateChanged.connect(self.MOD_0StateChanged)
        self.cb6.stateChanged.connect(self.IGNStateChanged)
        self.cb7.stateChanged.connect(self.ACCStateChanged)
        self.cb8.stateChanged.connect(self.BATStateChanged)

    def connectMUXMode(self):
        self.rbMUXNormalMode.toggled.connect(self.checkedMUXNormalMode)
        self.rbMUXDLTMode.toggled.connect(self.checkedMUXDLTMode)

    def checkedMUXNormalMode(self):
        self.myMUX.switch_to_normal_mode()
        self.log("[Multiplexer] Switch to normal mode")

    def checkedMUXDLTMode(self):
        self.myMUX.swith_to_DLT_mode()
        self.log("[Multiplexer] Switch to DLT mode")

    def updateCurrentState(self):
        try:
            # Get current state
            state = self.myRelay.curr_state
            # Convert int -> binary and display on LCD
            self.lcdBinState.display(format(state, '08b')) # display 8 bit
        except ValueError as err:
            self.log("Value of current state is invalid! \
                accept number only and valid range is [0, 255]). Detail error: " + str(err))
    
    def VBUSStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectVBUS()
            self.lblNum1.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectVBUS()
            self.lblNum1.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def WD_OFFStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectWD_OFF()
            self.lblNum3.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectWD_OFF()
            self.lblNum3.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def MOD_0StateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectMOD_0()
            self.lblNum4.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectMOD_0()
            self.lblNum4.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def IGNStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectIGN()
            self.lblNum6.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectIGN()
            self.lblNum6.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def ACCStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectACC()
            self.lblNum7.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectACC()
            self.lblNum7.setStyleSheet("color: rgb(0, 0, 0);")
        self.updateState()
    
    def BATStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.myRelay.connectBAT()
            self.lblNum8.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.myRelay.disconnectBAT()
            self.lblNum8.setStyleSheet("color: rgb(0, 0, 0);")
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

    def checkedNone(self):
        self.clearAllRelayPins()
        self.log("[Relay] None")

    def checkedNormalMode(self):
        # BAT:8, ACC:7, IGN:6, WD_OFF:3 on
        self.clearAllRelayPins()
        self.log("[Relay] Switch to Normal mode")
        self.cb8.setChecked(True)
        self.cb7.setChecked(True)
        self.cb6.setChecked(True)
        self.cb3.setChecked(True)
    
    def checkedAurixMode(self):
        # VBUS:1, BAT:8, ACC:7, IGN:6 on
        self.clearAllRelayPins()
        self.log("[Relay] Switch to Aurix flashing mode")
        self.cb1.setChecked(True)
        self.cb8.setChecked(True)
        self.cb7.setChecked(True)
        self.cb6.setChecked(True)
    
    def checkedAndroidMode(self):
        # BAT:8, ACC:7, IGN:6, WD_OFF:3, MOD_0:4 on
        self.clearAllRelayPins()
        self.log("[Relay] Switch to Android flashing mode")
        self.cb8.setChecked(True)
        self.cb7.setChecked(True)
        self.cb6.setChecked(True)
        self.cb3.setChecked(True)
        self.cb4.setChecked(True)

    def restartTarget(self):
        self.log("[Relay] Restart the target!")
        self.myRelay.turnOffAllRelay()
        self.clearAllRelayPins()
        self.myRelay.connectBAT()
        self.cb8.setChecked(True)
        self.myRelay.connectACC()
        self.cb7.setChecked(True)
        self.myRelay.connectIGN()
        self.cb6.setChecked(True)
        self.updateState()
    
    def turnOffTarget(self):
        self.log("[Relay] Turn off the target!")
        self.myRelay.turnOffAllRelay()
        self.clearAllRelayPins()
        self.updateState()
    
    def turnOnACC_IGN(self):
        self.log("[Relay] Turn on ACC + IGN!")
        self.myRelay.connectACC()
        self.cb7.setChecked(True)
        self.myRelay.connectIGN()
        self.cb6.setChecked(True)
        self.updateState()
    
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
