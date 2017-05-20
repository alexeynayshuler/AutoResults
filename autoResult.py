# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoResults_Gui.ui'
#
# Created: Thu May 11 11:00:24 2017
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Main, sys, time, threading, switch

result_path = 'C:\\python\\AutoResults\\results\\'
cap_path = 'C:\\python\\AutoResults\\capture\\capture1.txt'

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


class Ui_Dialog(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(515, 389)
        self.label_platform = QtGui.QLabel(Dialog)
        self.label_platform.setGeometry(QtCore.QRect(10, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_platform.setFont(font)
        self.label_platform.setObjectName(_fromUtf8("label_platform"))
        self.cb_platforms = QtGui.QComboBox(Dialog)
        self.cb_platforms.setGeometry(QtCore.QRect(70, 10, 91, 22))
        self.cb_platforms.setObjectName(_fromUtf8("cb_platforms"))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.cb_platforms.addItem(_fromUtf8(""))
        self.label_app = QtGui.QLabel(Dialog)
        self.label_app.setGeometry(QtCore.QRect(180, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_app.setFont(font)
        self.label_app.setObjectName(_fromUtf8("label_app"))
        self.cb_application = QtGui.QComboBox(Dialog)
        self.cb_application.setGeometry(QtCore.QRect(250, 10, 69, 22))
        self.cb_application.setObjectName(_fromUtf8("cb_application"))
        self.cb_application.addItem(_fromUtf8(""))
        self.cb_application.addItem(_fromUtf8(""))
        self.cb_application.addItem(_fromUtf8(""))
        self.groupBox_Params = QtGui.QGroupBox(Dialog)
        self.groupBox_Params.setGeometry(QtCore.QRect(10, 50, 491, 91))
        self.groupBox_Params.setObjectName(_fromUtf8("groupBox_Params"))
        self.checkBox_appVer = QtGui.QCheckBox(self.groupBox_Params)
        self.checkBox_appVer.setGeometry(QtCore.QRect(20, 30, 91, 17))
        self.checkBox_appVer.setObjectName(_fromUtf8("checkBox_appVer"))
        self.checkBox_biosVer = QtGui.QCheckBox(self.groupBox_Params)
        self.checkBox_biosVer.setGeometry(QtCore.QRect(150, 30, 70, 17))
        self.checkBox_biosVer.setObjectName(_fromUtf8("checkBox_biosVer"))
        self.checkBox_CPU = QtGui.QCheckBox(self.groupBox_Params)
        self.checkBox_CPU.setGeometry(QtCore.QRect(230, 30, 70, 17))
        self.checkBox_CPU.setObjectName(_fromUtf8("checkBox_CPU"))
        self.checkBox_BSP = QtGui.QCheckBox(self.groupBox_Params)
        self.checkBox_BSP.setGeometry(QtCore.QRect(290, 30, 70, 17))
        self.checkBox_BSP.setObjectName(_fromUtf8("checkBox_BSP"))
        self.checkBox_ndVer = QtGui.QCheckBox(self.groupBox_Params)
        self.checkBox_ndVer.setGeometry(QtCore.QRect(20, 60, 121, 17))
        self.checkBox_ndVer.setObjectName(_fromUtf8("checkBox_ndVer"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_Params)
        self.checkBox.setGeometry(QtCore.QRect(150, 60, 101, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_mac = QtGui.QCheckBox(self.groupBox_Params)
        self.checkBox_mac.setGeometry(QtCore.QRect(260, 60, 101, 17))
        self.checkBox_mac.setObjectName(_fromUtf8("checkBox_mac"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 491, 171))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_applVer = QtGui.QLabel(self.groupBox)
        self.label_applVer.setGeometry(QtCore.QRect(20, 20, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_applVer.setFont(font)
        self.label_applVer.setObjectName(_fromUtf8("label_applVer"))
        self.label_biosVer = QtGui.QLabel(self.groupBox)
        self.label_biosVer.setGeometry(QtCore.QRect(20, 40, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_biosVer.setFont(font)
        self.label_biosVer.setObjectName(_fromUtf8("label_biosVer"))
        self.label_CPU = QtGui.QLabel(self.groupBox)
        self.label_CPU.setGeometry(QtCore.QRect(20, 60, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CPU.setFont(font)
        self.label_CPU.setObjectName(_fromUtf8("label_CPU"))
        self.label_BSP = QtGui.QLabel(self.groupBox)
        self.label_BSP.setGeometry(QtCore.QRect(20, 80, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_BSP.setFont(font)
        self.label_BSP.setObjectName(_fromUtf8("label_BSP"))
        self.label_ndVer = QtGui.QLabel(self.groupBox)
        self.label_ndVer.setGeometry(QtCore.QRect(20, 100, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ndVer.setFont(font)
        self.label_ndVer.setObjectName(_fromUtf8("label_ndVer"))
        self.label_ramConfig = QtGui.QLabel(self.groupBox)
        self.label_ramConfig.setGeometry(QtCore.QRect(20, 120, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ramConfig.setFont(font)
        self.label_ramConfig.setObjectName(_fromUtf8("label_ramConfig"))
        self.label_mac = QtGui.QLabel(self.groupBox)
        self.label_mac.setGeometry(QtCore.QRect(20, 140, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_mac.setFont(font)
        self.label_mac.setObjectName(_fromUtf8("label_mac"))
        self.pushButton_start = QtGui.QPushButton(Dialog)
        self.pushButton_start.setGeometry(QtCore.QRect(340, 350, 75, 23))
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.pushButton_exit = QtGui.QPushButton(Dialog)
        self.pushButton_exit.setGeometry(QtCore.QRect(420, 350, 75, 23))
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.pushButton_saveResults = QtGui.QPushButton(Dialog)
        self.pushButton_saveResults.setGeometry(QtCore.QRect(20, 350, 75, 23))
        self.pushButton_saveResults.setObjectName(_fromUtf8("pushButton_saveResults"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.cb_platforms, self.cb_application)
        Dialog.setTabOrder(self.cb_application, self.checkBox_appVer)
        Dialog.setTabOrder(self.checkBox_appVer, self.checkBox_biosVer)
        Dialog.setTabOrder(self.checkBox_biosVer, self.checkBox_CPU)
        Dialog.setTabOrder(self.checkBox_CPU, self.checkBox_BSP)
        Dialog.setTabOrder(self.checkBox_BSP, self.checkBox_ndVer)
        Dialog.setTabOrder(self.checkBox_ndVer, self.checkBox)
        Dialog.setTabOrder(self.checkBox, self.checkBox_mac)
        Dialog.setTabOrder(self.checkBox_mac, self.pushButton_start)
        Dialog.setTabOrder(self.pushButton_start, self.pushButton_exit)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "AutoResults", None))
        self.label_platform.setText(_translate("Dialog", "Platform", None))
        self.cb_platforms.setItemText(0, _translate("Dialog", "ODSMR", None))
        self.cb_platforms.setItemText(1, _translate("Dialog", "ODSHTQe", None))
        self.cb_platforms.setItemText(2, _translate("Dialog", "ODSHTQ", None))
        self.cb_platforms.setItemText(3, _translate("Dialog", "ODSVL2", None))
        self.cb_platforms.setItemText(4, _translate("Dialog", "ODSLS", None))
        self.cb_platforms.setItemText(5, _translate("Dialog", "ODSVL", None))
        self.label_app.setText(_translate("Dialog", "Application", None))
        self.cb_application.setItemText(0, _translate("Dialog", "Alteon", None))
        self.cb_application.setItemText(1, _translate("Dialog", "DefensePro", None))
        self.cb_application.setItemText(2, _translate("Dialog", "AppDirector", None))
        self.groupBox_Params.setTitle(_translate("Dialog", "Parameters to check", None))
        self.checkBox_appVer.setText(_translate("Dialog", "Application ver", None))
        self.checkBox_biosVer.setText(_translate("Dialog", "BIOS Ver", None))
        self.checkBox_CPU.setText(_translate("Dialog", "CPU", None))
        self.checkBox_BSP.setText(_translate("Dialog", "BSP ver", None))
        self.checkBox_ndVer.setText(_translate("Dialog", "Network Driver ver", None))
        self.checkBox.setText(_translate("Dialog", "Memory config", None))
        self.checkBox_mac.setText(_translate("Dialog", "MAC Address", None))
        self.groupBox.setTitle(_translate("Dialog", "Results", None))
        self.label_applVer.setText(_translate("Dialog", "Application version: Unknown", None))
        self.label_biosVer.setText(_translate("Dialog", "BIOS version: Unknown", None))
        self.label_CPU.setText(_translate("Dialog", "CPU: Unknown", None))
        self.label_BSP.setText(_translate("Dialog", "BSP version: Unknown", None))
        self.label_ndVer.setText(_translate("Dialog", "Network Driver version: Unknown", None))
        self.label_ramConfig.setText(_translate("Dialog", "Memory Configuration: Unknown", None))
        self.label_mac.setText(_translate("Dialog", "MAC Address: Unknown", None))
        self.pushButton_start.setText(_translate("Dialog", "Start", None))
        self.pushButton_exit.setText(_translate("Dialog", "Exit", None))
        self.pushButton_saveResults.setText(_translate("Dialog", "Save Results", None))

        ####coding for buttons
        #self.pushButton_start.clicked.connect(self.start_chosen_t)
        self.pushButton_exit.clicked.connect(self.exit_chosen)
        self.pushButton_start.clicked.connect(self.start_chosen_t)


    ### Functions for buttons
    def start_chosen_t(self):
        t = threading.Thread(target=self.start_chosen)
        t.start()

    def start_chosen(self):
        app_triger = str(ex.cb_application.currentText())
        platform_triger = int(ex.cb_platforms.currentIndex())
        #print (switch.app_switch_case(app_triger))
        #print (switch.platform_switch_case(platform_triger))

        for case in switch.switch(app_triger):
            if case('Alteon'):
                print('This is Alteon')
                break
            if case('DefensePro'):
                print('This is DefensePro')
                break
            if case('AppDirector'):
                print('This is AppDirector')
                break

        for case in switch.switch(platform_triger):
            if case(0):
                print 'ODSMR'
                break
            if case() :
                print 'other platform'

    def exit_chosen(self):
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(app.exec_())
