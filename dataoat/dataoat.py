import os, serial
from atcommand import huawei


try:
    print('Port to connect [/dev/ttyUSB0]:')
    retc = os.access("/dev/ttyUSB80", os.F_OK)
    if retc:
        print(retc)
        ser = serial.Serial(uart, 921600, timeout=0, parity=serial.PARITY_NONE, rtscts=0)  # open serial port
        print(' Port = ' + ser.name)


    d = "\r\n"

    comm_add = huawei.SQNSD(None, 3, 0, 80, '192.168.3.1', 0, 0, 0)
    print(comm_add+d)

finally:
    ser.close()
