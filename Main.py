import serial, socket, os

from PyQt4 import QtGui, QtCore
result_path = 'C:\\python\\AutoResults\\results\\'
cap_path = 'C:\\python\\AutoResults\\capture\\capture1.txt'

global cap1

try:
    cap1 =  open(cap_path, 'w+')
    print cap1
except:
    print 'cant open capture file'

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


    # device list [MAC,Sw version]
    ######### Open serial interface for Radware Device
    def openSerial(ex):  # com_info = [COM3,9600]
        ser = serial.Serial()
        if ex.comboBox.currentText() == 'Alteon':
            ser.baudrate = '9600'
        else:
            ser.baudrate = '19200'

        ser.port = str('COM' + ex.lineEdit_COM.text())
        ser.timeout = 1
        # ser.port = str(com_info[0])
        ser.open()
        print ser.portstr + ' Opened'
        return ser;