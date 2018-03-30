import struct
import serial
import time
import datetime

try:

    def parss():
        s = ''
        s = ser.readlines()
        out = ''
        for lines in s:
            out = lines.replace('\n', '').replace('\r', '')
            if out != '':
                print(' ==> ' + out)

        return out


    ser = serial.Serial('/dev/ttyUSB0', 921600, timeout=0, parity=serial.PARITY_NONE, rtscts=1)  # open serial port
    print(' Port = ' + ser.name)
    # d = struct.pack('BB', 0x0D, 0x0A)
    d = "\r\n"
    comm_1 = 'at'
    for i in range(1, 999):
        ser.write(comm_1 + d)
        time.sleep(0.5)
        rrr = parss()
        time.sleep(0.5)


finally:
    ser.close()
