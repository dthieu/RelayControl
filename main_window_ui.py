# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\relay_control.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 707)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\assets/icon/relay-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0)")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 70, 471, 591))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 351, 451, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtLog = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.txtLog.setObjectName("txtLog")
        self.horizontalLayout.addWidget(self.txtLog)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 261, 331))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbNone = QtWidgets.QRadioButton(self.groupBox)
        self.rbNone.setChecked(True)
        self.rbNone.setObjectName("rbNone")
        self.verticalLayout_2.addWidget(self.rbNone)
        self.rbNormalMode = QtWidgets.QRadioButton(self.groupBox)
        self.rbNormalMode.setObjectName("rbNormalMode")
        self.verticalLayout_2.addWidget(self.rbNormalMode)
        self.rbAurixMode = QtWidgets.QRadioButton(self.groupBox)
        self.rbAurixMode.setObjectName("rbAurixMode")
        self.verticalLayout_2.addWidget(self.rbAurixMode)
        self.rbAndroidMode = QtWidgets.QRadioButton(self.groupBox)
        self.rbAndroidMode.setObjectName("rbAndroidMode")
        self.verticalLayout_2.addWidget(self.rbAndroidMode)
        self.verticalLayout_14.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(60, 20, 51, 55))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lblNum7 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNum7.setFont(font)
        self.lblNum7.setText("")
        self.lblNum7.setObjectName("lblNum7")
        self.verticalLayout_7.addWidget(self.lblNum7)
        self.cb7 = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.cb7.setText("")
        self.cb7.setObjectName("cb7")
        self.verticalLayout_7.addWidget(self.cb7)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.layoutWidget_5 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget_5.setGeometry(QtCore.QRect(120, 20, 51, 55))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lblNum6 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNum6.setFont(font)
        self.lblNum6.setText("")
        self.lblNum6.setObjectName("lblNum6")
        self.verticalLayout_8.addWidget(self.lblNum6)
        self.cb6 = QtWidgets.QCheckBox(self.layoutWidget_5)
        self.cb6.setText("")
        self.cb6.setObjectName("cb6")
        self.verticalLayout_8.addWidget(self.cb6)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.layoutWidget_7 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget_7.setGeometry(QtCore.QRect(190, 20, 51, 55))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lblNum5 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNum5.setFont(font)
        self.lblNum5.setText("")
        self.lblNum5.setObjectName("lblNum5")
        self.verticalLayout_10.addWidget(self.lblNum5)
        self.cb5 = QtWidgets.QCheckBox(self.layoutWidget_7)
        self.cb5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb5.setText("")
        self.cb5.setObjectName("cb5")
        self.verticalLayout_10.addWidget(self.cb5)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_10.addWidget(self.label_18)
        self.layoutWidget_8 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget_8.setGeometry(QtCore.QRect(190, 100, 51, 55))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_12.addWidget(self.label_21)
        self.cb4 = QtWidgets.QCheckBox(self.layoutWidget_8)
        self.cb4.setText("")
        self.cb4.setObjectName("cb4")
        self.verticalLayout_12.addWidget(self.cb4)
        self.lblNum4 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNum4.setFont(font)
        self.lblNum4.setText("")
        self.lblNum4.setObjectName("lblNum4")
        self.verticalLayout_12.addWidget(self.lblNum4)
        self.layoutWidget_6 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget_6.setGeometry(QtCore.QRect(120, 100, 51, 55))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.cb3 = QtWidgets.QCheckBox(self.layoutWidget_6)
        self.cb3.setText("")
        self.cb3.setObjectName("cb3")
        self.verticalLayout_9.addWidget(self.cb3)
        self.lblNum3 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNum3.setFont(font)
        self.lblNum3.setText("")
        self.lblNum3.setObjectName("lblNum3")
        self.verticalLayout_9.addWidget(self.lblNum3)
        self.layoutWidget_9 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget_9.setGeometry(QtCore.QRect(60, 100, 51, 55))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_9)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_13.addWidget(self.label_23)
        self.cb2 = QtWidgets.QCheckBox(self.layoutWidget_9)
        self.cb2.setText("")
        self.cb2.setObjectName("cb2")
        self.verticalLayout_13.addWidget(self.cb2)
        self.lblNum2 = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNum2.setFont(font)
        self.lblNum2.setText("")
        self.lblNum2.setObjectName("lblNum2")
        self.verticalLayout_13.addWidget(self.lblNum2)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 100, 41, 55))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.cb1 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.cb1.setText("")
        self.cb1.setObjectName("cb1")
        self.verticalLayout_4.addWidget(self.cb1)
        self.lblNum1 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNum1.setFont(font)
        self.lblNum1.setText("")
        self.lblNum1.setObjectName("lblNum1")
        self.verticalLayout_4.addWidget(self.lblNum1)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 20, 41, 55))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblNum8 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblNum8.setFont(font)
        self.lblNum8.setText("")
        self.lblNum8.setObjectName("lblNum8")
        self.verticalLayout_3.addWidget(self.lblNum8)
        self.cb8 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.cb8.setText("")
        self.cb8.setObjectName("cb8")
        self.verticalLayout_3.addWidget(self.cb8)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_14.addWidget(self.groupBox_3)
        self.layoutWidget4 = QtWidgets.QWidget(self.frame)
        self.layoutWidget4.setGeometry(QtCore.QRect(290, 11, 170, 331))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.txtCurrentState = QtWidgets.QLineEdit(self.layoutWidget4)
        self.txtCurrentState.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtCurrentState.setFont(font)
        self.txtCurrentState.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtCurrentState.setAlignment(QtCore.Qt.AlignCenter)
        self.txtCurrentState.setReadOnly(True)
        self.txtCurrentState.setObjectName("txtCurrentState")
        self.horizontalLayout_2.addWidget(self.txtCurrentState)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.lcdBinState = QtWidgets.QLCDNumber(self.layoutWidget4)
        self.lcdBinState.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdBinState.sizePolicy().hasHeightForWidth())
        self.lcdBinState.setSizePolicy(sizePolicy)
        self.lcdBinState.setSizeIncrement(QtCore.QSize(0, 0))
        self.lcdBinState.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.lcdBinState.setFont(font)
        self.lcdBinState.setAutoFillBackground(False)
        self.lcdBinState.setStyleSheet("background-color: rgb(190, 190, 190);\n"
"color: blue")
        self.lcdBinState.setSmallDecimalPoint(True)
        self.lcdBinState.setDigitCount(8)
        self.lcdBinState.setMode(QtWidgets.QLCDNumber.Bin)
        self.lcdBinState.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdBinState.setProperty("value", 0.0)
        self.lcdBinState.setObjectName("lcdBinState")
        self.verticalLayout_6.addWidget(self.lcdBinState)
        spacerItem = QtWidgets.QSpacerItem(144, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnTargetOff = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnTargetOff.setFont(font)
        self.btnTargetOff.setStyleSheet("background-color: red;\n"
"color: white")
        self.btnTargetOff.setObjectName("btnTargetOff")
        self.verticalLayout.addWidget(self.btnTargetOff)
        self.btnTargetRestart = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnTargetRestart.setFont(font)
        self.btnTargetRestart.setStyleSheet("background-color: green;\n"
"color: white")
        self.btnTargetRestart.setObjectName("btnTargetRestart")
        self.verticalLayout.addWidget(self.btnTargetRestart)
        self.btnACC_IGN_on = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btnACC_IGN_on.setFont(font)
        self.btnACC_IGN_on.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.btnACC_IGN_on.setObjectName("btnACC_IGN_on")
        self.verticalLayout.addWidget(self.btnACC_IGN_on)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.rbMUXNormalMode = QtWidgets.QRadioButton(self.groupBox_4)
        self.rbMUXNormalMode.setChecked(True)
        self.rbMUXNormalMode.setObjectName("rbMUXNormalMode")
        self.verticalLayout_11.addWidget(self.rbMUXNormalMode)
        self.rbMUXDLTMode = QtWidgets.QRadioButton(self.groupBox_4)
        self.rbMUXDLTMode.setObjectName("rbMUXDLTMode")
        self.verticalLayout_11.addWidget(self.rbMUXDLTMode)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 45, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(85, 0, 255)")
        self.label_3.setObjectName("label_3")
        self.grbPowerControl = QtWidgets.QGroupBox(self.centralwidget)
        self.grbPowerControl.setGeometry(QtCore.QRect(500, 170, 301, 81))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.grbPowerControl.setFont(font)
        self.grbPowerControl.setObjectName("grbPowerControl")
        self.widget = QtWidgets.QWidget(self.grbPowerControl)
        self.widget.setGeometry(QtCore.QRect(11, 21, 251, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.txtSetVol = QtWidgets.QLineEdit(self.widget)
        self.txtSetVol.setObjectName("txtSetVol")
        self.horizontalLayout_3.addWidget(self.txtSetVol)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.btnSetVol = QtWidgets.QPushButton(self.widget)
        self.btnSetVol.setObjectName("btnSetVol")
        self.horizontalLayout_3.addWidget(self.btnSetVol)
        self.widget1 = QtWidgets.QWidget(self.grbPowerControl)
        self.widget1.setGeometry(QtCore.QRect(11, 50, 251, 25))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.txtGetVol = QtWidgets.QLineEdit(self.widget1)
        self.txtGetVol.setReadOnly(True)
        self.txtGetVol.setObjectName("txtGetVol")
        self.horizontalLayout_4.addWidget(self.txtGetVol)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.btnGetVol = QtWidgets.QPushButton(self.widget1)
        self.btnGetVol.setObjectName("btnGetVol")
        self.horizontalLayout_4.addWidget(self.btnGetVol)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(500, 560, 301, 91))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.widget2 = QtWidgets.QWidget(self.groupBox_5)
        self.widget2.setGeometry(QtCore.QRect(10, 22, 277, 54))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.btnRelayFlashMode = QtWidgets.QPushButton(self.widget2)
        self.btnRelayFlashMode.setObjectName("btnRelayFlashMode")
        self.verticalLayout_15.addWidget(self.btnRelayFlashMode)
        self.btnRelayNormalMode = QtWidgets.QPushButton(self.widget2)
        self.btnRelayNormalMode.setObjectName("btnRelayNormalMode")
        self.verticalLayout_15.addWidget(self.btnRelayNormalMode)
        self.grbMUXControl = QtWidgets.QGroupBox(self.centralwidget)
        self.grbMUXControl.setGeometry(QtCore.QRect(500, 260, 301, 291))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.grbMUXControl.setFont(font)
        self.grbMUXControl.setObjectName("grbMUXControl")
        self.widget3 = QtWidgets.QWidget(self.grbMUXControl)
        self.widget3.setGeometry(QtCore.QRect(10, 30, 281, 252))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.btnMUXTestingMode = QtWidgets.QPushButton(self.widget3)
        self.btnMUXTestingMode.setObjectName("btnMUXTestingMode")
        self.verticalLayout_16.addWidget(self.btnMUXTestingMode)
        self.btnMUXFlashMode = QtWidgets.QPushButton(self.widget3)
        self.btnMUXFlashMode.setObjectName("btnMUXFlashMode")
        self.verticalLayout_16.addWidget(self.btnMUXFlashMode)
        self.graphicsViewMUX = QtWidgets.QGraphicsView(self.widget3)
        self.graphicsViewMUX.setEnabled(True)
        self.graphicsViewMUX.setObjectName("graphicsViewMUX")
        self.verticalLayout_16.addWidget(self.graphicsViewMUX)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(610, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(85, 0, 255)")
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuSetting = QtWidgets.QAction(MainWindow)
        self.menuSetting.setObjectName("menuSetting")
        self.menuExit = QtWidgets.QAction(MainWindow)
        self.menuExit.setObjectName("menuExit")
        self.menuAbout = QtWidgets.QAction(MainWindow)
        self.menuAbout.setObjectName("menuAbout")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuSetting)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExit)
        self.menuHelp.addAction(self.menuAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CCS2 Relay Control"))
        self.label.setText(_translate("MainWindow", "Target Control"))
        self.label_7.setText(_translate("MainWindow", "Log:"))
        self.groupBox.setTitle(_translate("MainWindow", "Common modes"))
        self.rbNone.setText(_translate("MainWindow", "None"))
        self.rbNormalMode.setText(_translate("MainWindow", "Normal mode"))
        self.rbAurixMode.setText(_translate("MainWindow", "Aurix flashing mode"))
        self.rbAndroidMode.setText(_translate("MainWindow", "Android flashing mode"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Relay PINS"))
        self.label_12.setText(_translate("MainWindow", "7"))
        self.label_14.setText(_translate("MainWindow", "6"))
        self.label_18.setText(_translate("MainWindow", "5"))
        self.label_21.setText(_translate("MainWindow", "4"))
        self.label_15.setText(_translate("MainWindow", "3"))
        self.label_23.setText(_translate("MainWindow", "2"))
        self.label_5.setText(_translate("MainWindow", "1"))
        self.label_4.setText(_translate("MainWindow", "8"))
        self.label_2.setText(_translate("MainWindow", "Current state:"))
        self.txtCurrentState.setText(_translate("MainWindow", "232"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Common Functions"))
        self.btnTargetOff.setText(_translate("MainWindow", "Target OFF"))
        self.btnTargetRestart.setText(_translate("MainWindow", "Restart Target"))
        self.btnACC_IGN_on.setText(_translate("MainWindow", "ACC IGN ON"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Multiplexer mode"))
        self.rbMUXNormalMode.setText(_translate("MainWindow", "Normal mode"))
        self.rbMUXDLTMode.setText(_translate("MainWindow", "DLT mode"))
        self.label_3.setText(_translate("MainWindow", "CCS2"))
        self.grbPowerControl.setTitle(_translate("MainWindow", "Power controler"))
        self.label_6.setText(_translate("MainWindow", "Set Voltage"))
        self.txtSetVol.setText(_translate("MainWindow", "12"))
        self.label_9.setText(_translate("MainWindow", "V    "))
        self.btnSetVol.setText(_translate("MainWindow", "Set"))
        self.label_8.setText(_translate("MainWindow", "Get Voltage"))
        self.label_10.setText(_translate("MainWindow", "V    "))
        self.btnGetVol.setText(_translate("MainWindow", "Get"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Relay Controler"))
        self.btnRelayFlashMode.setText(_translate("MainWindow", "Active Android - QNX flash mode"))
        self.btnRelayNormalMode.setText(_translate("MainWindow", "Acitve normal  mode (Flash AR / Testing mode)"))
        self.grbMUXControl.setTitle(_translate("MainWindow", "Multiplexer controler"))
        self.btnMUXTestingMode.setText(_translate("MainWindow", "Acitve Testing / SSH mode"))
        self.btnMUXFlashMode.setText(_translate("MainWindow", "Active Flashing Autosar / Android - QNX mode"))
        self.label_11.setText(_translate("MainWindow", "GMVCU"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSetting.setText(_translate("MainWindow", "Setting"))
        self.menuExit.setText(_translate("MainWindow", "Exit"))
        self.menuAbout.setText(_translate("MainWindow", "About"))
