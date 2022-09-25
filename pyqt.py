from PyQt5 import QtWidgets,uic
from PyQt5.QtSerialPort import QSerialPort,QSerialPortInfo
from PyQt5.QtCore import QIODevice


app=QtWidgets.QApplication([])
ui=uic.loadUi('designer.ui')

serial=QSerialPort()
serial.setBaudRate(115200)
portList=[]
ports=QSerialPortInfo().availablePorts()
for port in ports:
    portList.append(port.portName())
ui.comboBox.addItems(portList)

def connect_to_arduino():
    serial.setPortName(ui.comboBox.currentText())
    serial.open(QIODevice.ReadWrite)
    print('hi')



ui.btn_open.clicked.connect(connect_to_arduino)





ui.show()
app.exec()


