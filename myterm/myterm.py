import sys
import select
import tty
import termios
import serial
import time
import datetime

port = '/dev/ttyUSB0'

time_o = 0
terminator = 0
fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)
ser = serial.Serial(port, 921600, timeout=0, parity=serial.PARITY_NONE, rtscts=1)  # open serial port


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def timest():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')
    return st


try:
    tty.setcbreak(fd)
    print('==================================== HELP KEYS ======================================')
    print('=                                                                                   =')
    print('=  CTRL+I to set.dtr = True, voltage=0V                                             =')
    print('=  CTRL+O to set.dtr = False, voltage=1.8V                                          =')
    print('=  CTRL+Y - on/off timestamp toggled                                                =')
    print('=                                                                                   =')
    print('=====================================================================================')
    while 1:
        s = ser.readlines()
        if s:
            for lines in s:
                # ss = lines.decode().replace('\n', '').replace('\r', '')
                ss = lines.decode()
                if lines.decode().find('\r') > -1:
                    terminator = 1
                else:
                    terminator = 0
                if time_o == 1 & terminator == 1:
                    sys.stdout.write('['+timest()+'] ')
                sys.stdout.write(ss)

        if isData():
            c = sys.stdin.read(1)
            #print ord(c)
            if c == '\x09':  # x09 is CTRL+I
                ser.dtr = True
                print('>>> Service message >> CTRL+I pressed set.dtr = True, voltage=0V')
            elif c == '\x0F':  # x0F is CTRL+O
                ser.dtr = False
                print('>>> Service message >> CTRL+O pressed set.dtr = False, voltage=1.8V')
            elif c == '\x19':  # x19 is CTRL+Y - on/off timestamp
                if time_o == 0:
                    time_o = 1
                else:
                    time_o = 0
                print('>>> Service message >> CTRL+Y pressed - on/off timestamp toggled')
            elif c == '\x1b':  # x1b is ESC
                break

            else:
                ser.write(c.encode())

finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old)

