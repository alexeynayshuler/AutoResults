# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoResults_Gui.ui'
#
# Created: Sun May 28 14:07:04 2017
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AutoResult_Form(object):
    def setupUi(self, AutoResult_Form):
        AutoResult_Form.setObjectName(_fromUtf8("AutoResult_Form"))
        AutoResult_Form.resize(410, 376)
        self.verticalLayoutWidget = QtGui.QWidget(AutoResult_Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 391, 101))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox_Params_2 = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_Params_2.setObjectName(_fromUtf8("groupBox_Params_2"))
        self.checkBox_appVer = QtGui.QCheckBox(self.groupBox_Params_2)
        self.checkBox_appVer.setGeometry(QtCore.QRect(20, 30, 91, 17))
        self.checkBox_appVer.setObjectName(_fromUtf8("checkBox_appVer"))
        self.checkBox_biosVer = QtGui.QCheckBox(self.groupBox_Params_2)
        self.checkBox_biosVer.setGeometry(QtCore.QRect(150, 30, 70, 17))
        self.checkBox_biosVer.setObjectName(_fromUtf8("checkBox_biosVer"))
        self.checkBox_cpu = QtGui.QCheckBox(self.groupBox_Params_2)
        self.checkBox_cpu.setGeometry(QtCore.QRect(230, 30, 70, 17))
        self.checkBox_cpu.setObjectName(_fromUtf8("checkBox_cpu"))
        self.checkBox_bsp = QtGui.QCheckBox(self.groupBox_Params_2)
        self.checkBox_bsp.setGeometry(QtCore.QRect(290, 30, 70, 17))
        self.checkBox_bsp.setObjectName(_fromUtf8("checkBox_bsp"))
        self.checkBox_ndVer = QtGui.QCheckBox(self.groupBox_Params_2)
        self.checkBox_ndVer.setGeometry(QtCore.QRect(20, 60, 121, 17))
        self.checkBox_ndVer.setObjectName(_fromUtf8("checkBox_ndVer"))
        self.checkBox_memConf = QtGui.QCheckBox(self.groupBox_Params_2)
        self.checkBox_memConf.setGeometry(QtCore.QRect(150, 60, 101, 17))
        self.checkBox_memConf.setObjectName(_fromUtf8("checkBox_memConf"))
        self.checkBox_mac = QtGui.QCheckBox(self.groupBox_Params_2)
        self.checkBox_mac.setGeometry(QtCore.QRect(260, 60, 101, 17))
        self.checkBox_mac.setObjectName(_fromUtf8("checkBox_mac"))
        self.verticalLayout_4.addWidget(self.groupBox_Params_2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(AutoResult_Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 341, 181))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_2 = QtGui.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_applVer = QtGui.QLabel(self.groupBox_2)
        self.label_applVer.setGeometry(QtCore.QRect(20, 20, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_applVer.setFont(font)
        self.label_applVer.setObjectName(_fromUtf8("label_applVer"))
        self.label_biosVer = QtGui.QLabel(self.groupBox_2)
        self.label_biosVer.setGeometry(QtCore.QRect(20, 40, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_biosVer.setFont(font)
        self.label_biosVer.setObjectName(_fromUtf8("label_biosVer"))
        self.label_cpu = QtGui.QLabel(self.groupBox_2)
        self.label_cpu.setGeometry(QtCore.QRect(20, 60, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_cpu.setFont(font)
        self.label_cpu.setObjectName(_fromUtf8("label_cpu"))
        self.label_bsp = QtGui.QLabel(self.groupBox_2)
        self.label_bsp.setGeometry(QtCore.QRect(20, 80, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_bsp.setFont(font)
        self.label_bsp.setObjectName(_fromUtf8("label_bsp"))
        self.label_ndVer = QtGui.QLabel(self.groupBox_2)
        self.label_ndVer.setGeometry(QtCore.QRect(20, 100, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ndVer.setFont(font)
        self.label_ndVer.setObjectName(_fromUtf8("label_ndVer"))
        self.label_ramConfig = QtGui.QLabel(self.groupBox_2)
        self.label_ramConfig.setGeometry(QtCore.QRect(20, 120, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ramConfig.setFont(font)
        self.label_ramConfig.setObjectName(_fromUtf8("label_ramConfig"))
        self.label_mac = QtGui.QLabel(self.groupBox_2)
        self.label_mac.setGeometry(QtCore.QRect(20, 140, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_mac.setFont(font)
        self.label_mac.setObjectName(_fromUtf8("label_mac"))
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayoutWidget = QtGui.QWidget(AutoResult_Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 389, 22))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_platform = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_platform.setFont(font)
        self.label_platform.setObjectName(_fromUtf8("label_platform"))
        self.horizontalLayout_2.addWidget(self.label_platform)
        self.cb_platforms = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.cb_platforms.setObjectName(_fromUtf8("cb_platforms"))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cb_platforms)
        self.label_app = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_app.setFont(font)
        self.label_app.setObjectName(_fromUtf8("label_app"))
        self.horizontalLayout_2.addWidget(self.label_app)
        self.cb_application = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.cb_application.setObjectName(_fromUtf8("cb_application"))
        self.cb_application.addItem(_fromUtf8(""))
        self.cb_application.addItem(_fromUtf8(""))
        self.cb_application.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cb_application)
        self.label_com = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_com.setObjectName(_fromUtf8("label_com"))
        self.horizontalLayout_2.addWidget(self.label_com)
        self.cb_com = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.cb_com.setObjectName(_fromUtf8("cb_com"))
        self.horizontalLayout_2.addWidget(self.cb_com)
        self.gridLayoutWidget = QtGui.QWidget(AutoResult_Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 340, 239, 25))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_exit = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_exit.setDefault(True)
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.gridLayout_3.addWidget(self.pushButton_exit, 0, 2, 1, 1)
        self.pushButton_saveResults = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_saveResults.setDefault(True)
        self.pushButton_saveResults.setObjectName(_fromUtf8("pushButton_saveResults"))
        self.gridLayout_3.addWidget(self.pushButton_saveResults, 0, 0, 1, 1)
        self.pushButton_start = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_start.setDefault(True)
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.gridLayout_3.addWidget(self.pushButton_start, 0, 1, 1, 1)

        self.retranslateUi(AutoResult_Form)
        QtCore.QMetaObject.connectSlotsByName(AutoResult_Form)

    def retranslateUi(self, AutoResult_Form):
        AutoResult_Form.setWindowTitle(_translate("AutoResult_Form", "AutoResult_Gui", None))
        self.groupBox_Params_2.setTitle(_translate("AutoResult_Form", "Parameters to check", None))
        self.checkBox_appVer.setText(_translate("AutoResult_Form", "Application ver", None))
        self.checkBox_biosVer.setText(_translate("AutoResult_Form", "BIOS Ver", None))
        self.checkBox_cpu.setText(_translate("AutoResult_Form", "CPU", None))
        self.checkBox_bsp.setText(_translate("AutoResult_Form", "BSP ver", None))
        self.checkBox_ndVer.setText(_translate("AutoResult_Form", "Network Driver ver", None))
        self.checkBox_memConf.setText(_translate("AutoResult_Form", "Memory config", None))
        self.checkBox_mac.setText(_translate("AutoResult_Form", "MAC Address", None))
        self.groupBox_2.setTitle(_translate("AutoResult_Form", "Results", None))
        self.label_applVer.setText(_translate("AutoResult_Form", "Application version: Unknown", None))
        self.label_biosVer.setText(_translate("AutoResult_Form", "BIOS version: Unknown", None))
        self.label_cpu.setText(_translate("AutoResult_Form", "CPU: Unknown", None))
        self.label_bsp.setText(_translate("AutoResult_Form", "BSP version: Unknown", None))
        self.label_ndVer.setText(_translate("AutoResult_Form", "Network Driver version: Unknown", None))
        self.label_ramConfig.setText(_translate("AutoResult_Form", "Memory Configuration: Unknown", None))
        self.label_mac.setText(_translate("AutoResult_Form", "MAC Address: Unknown", None))
        self.label_platform.setText(_translate("AutoResult_Form", "Platform", None))
        self.cb_platforms.setItemText(0, _translate("AutoResult_Form", "ODSMR", None))
        self.cb_platforms.setItemText(1, _translate("AutoResult_Form", "ODSHTQe", None))
        self.cb_platforms.setItemText(2, _translate("AutoResult_Form", "ODSHTQ", None))
        self.cb_platforms.setItemText(3, _translate("AutoResult_Form", "ODSVL2", None))
        self.cb_platforms.setItemText(4, _translate("AutoResult_Form", "ODSLS", None))
        self.cb_platforms.setItemText(5, _translate("AutoResult_Form", "ODSVL", None))
        self.label_app.setText(_translate("AutoResult_Form", "Application", None))
        self.cb_application.setItemText(0, _translate("AutoResult_Form", "Alteon", None))
        self.cb_application.setItemText(1, _translate("AutoResult_Form", "DefensePro", None))
        self.cb_application.setItemText(2, _translate("AutoResult_Form", "AppDirector", None))
        self.label_com.setText(_translate("AutoResult_Form", "Com", None))
        self.pushButton_exit.setText(_translate("AutoResult_Form", "Exit", None))
        self.pushButton_saveResults.setText(_translate("AutoResult_Form", "Save Results", None))
        self.pushButton_start.setText(_translate("AutoResult_Form", "Start", None))

