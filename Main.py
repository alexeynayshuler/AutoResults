import serial, socket, os, time, re

from PyQt4 import QtGui, QtCore
result_path = 'C:\\python\\AutoResults\\results\\'
cap1_path = 'C:\\python\\AutoResults\\capture\\capture1.txt'
cap2_path = 'C:\\python\\AutoResults\\capture\\capture2.txt'

global cap1
global cap2

try:
    cap1 =  open(cap1_path, 'w+')
    print cap1
    cap2 = open(cap2_path, 'w+')
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
        if ex.cb_application.currentText() == 'Alteon':
            ser.baudrate = '9600'
        else:
            ser.baudrate = '19200'

        ser.port = str('COM' + ex.cb_com.currentText())
        ser.timeout = 1
        # ser.port = str(com_info[0])
        ser.open()
        print ser.portstr + ' Opened'
        return ser;


    ########wait for function######
    def Waitfor(str_search, timer, ser):
        # from Gui_combo import cap1
        # from Gui_combo import cap2
        t1 = time.time()
        t3 = 0
        global serial_line, cap1
        while (t3 < timer):
            t2 = time.time()
            t3 = t2 - t1
            serial_line = ser.readline()
            print(serial_line)
            cap1.write(serial_line + "\n")
            if (str_search in serial_line):
                if os.path.getsize(cap1_path) > 5000:
                    print cap1
                    print os.path.getsize(cap1_path)
                    cap1.close()
                    cap2.close()
                    os.system('copy ' + cap1_path + ' ' + cap2_path)
                    try:
                        cap1 = open(cap1_path, 'w+')
                        print 'after open'
                        print cap1
                        time.sleep(3)
                    except:
                        print 'cant open capture file'
                return serial_line;
        cap1.close()
        cap2.close()
        os.system('copy ' + cap2_path + ' + ' + cap1_path + ' ' + cap2_path)
        try:
            cap1 = open(cap1_path, 'w+')
            print 'after open'
            print cap1
            time.sleep(3)
        except:
            print 'cant open capture file'
        return 0


    ########get the Device info from power up######
    def device_info(ex, ser):
        Device = ['mac', 'sw']
        if (ex.comboBox_application.currentText() == 'Alteon'):

            if Waitfor('kernel /', 100, ser):
                print 'reconize alteon'
                Device[1] = (serial_line.split('kernel /')[1]).split('/')[0]
            else:
                Device[1] = 'no ver'

            ####found Mac####################
            if Waitfor('Base MAC Address', 100, ser):
                Device[0] = (serial_line.split('= ')[1]).rstrip()
            else:
                Device[0] = 'no mac'
            return Device;
        ### DP applications
        elif (ex.comboBox_application.currentText() == 'DefensePro') and (
                            ex.comboBox_platform.currentText() == 'ODSMR' or 'ODSHTQ' or 'ODSHTQE'):
            if Waitfor('mnt/cf/', 100, ser):
                Device[1] = (serial_line.split('mnt/cf/')[1]).split('-64bit')[0]
            else:
                Device[1] = 'no ver'

            ####found Mac####################
            if Waitfor('Base MAC address', 100, ser):
                Device[0] = (serial_line.split(': ')[1]).rstrip()
            else:
                Device[0] = 'no mac'
            return Device;
        else:  ### rest of DP and other applications#
            if Waitfor('MAC address: ', 100, ser):
                Device[0] = (serial_line.split(': ')[1]).rstrip()
            else:
                Device[0] = 'no mac'
            return Device;
            ### get SW
            if Waitfor('cm:/', 100, ser):
                Device[1] = (serial_line.split('/')[1]).split('/')[0]
            else:
                Device[1] = 'no ver'


    ####save results####################
    def save(ex, Device, ls_card_result):
        maci = re.sub('[^0-9a-zA-Z]+', '', Device[0])
        try:
            fo = open(result_path + maci + ".txt", "w+")
            print (result_path + maci + ".txt")
        except:
            print 'cant save the file'
        fo.write("Device info :  Platform- %s Application- %s \n" % (
        ex.comboBox_platform.currentText(), ex.comboBox_application.currentText()))
        fo.write("MAC: %s  \n" % Device[0])
        fo.write("Version: %s  \n" % Device[1])
        fo.write("Reboot Test: %s  Result: %s %s Cycles \n" % (
        str(ex.checkBox_reboot.isChecked()), ex.label_reboot_result.text(), ex.lineEdit_reboot.text()))
        fo.write("ShutDown Test: %s  Result: %s %s Cycles \n" % (
        str(ex.checkBox_sd.isChecked()), ex.label_sd_result.text(), ex.lineEdit_sd.text()))
        fo.write("SSL Test: %s  Result: %s %s Cycles \n" % (
        str(ex.checkBox_ssl.isChecked()), ex.label_ssl_result.text(), ex.lineEdit_ssl.text()))
        fo.write("Last State Test: %s  Result: %s %s Cycles  \nReason: %s \n" % (
        str(ex.checkBox_ls.isChecked()), ex.label_ls_result.text(), ex.lineEdit_ls.text(), ls_card_result))
        fo.close()