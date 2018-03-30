import struct
import serial
import time
import datetime

init_clear = 1  # ========== 0-disabled, 1-enabled
pdn_check_1 = 2  # ========= first pdn to check connection
pdn_check_2 = 3  # ========= second pdn to check connection

try:
    def timest():
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        return st


    def parss():
        s = ''
        s = ser.readlines()
        out = ''
        for lines in s:
            out = lines.replace('\n', '').replace('\r', '')
            if out != '':
                print(timest() + ' ==> ' + out)
            if (out == 'ERROR') and (j == pdn_check_1 or j == pdn_check_2):
                out = 'FAULT'
                break

        return out

    
    ser = serial.Serial('/dev/ttyXRUSB2', 921600, timeout=0, parity=serial.PARITY_NONE, rtscts=1)  # open serial port
    print(' Port = ' + ser.name)
    #d = struct.pack('BB', 0x0D, 0x0A)
    d = "\r\n"
    comm_add = ['at+cgact?', 'at+sqnss', 'at+sqnsi', 'at+sqnscfg?', 'at!=\"ifconfig\"', 'at!=\"showpdn\"', 'at!=\"ping google.com\"']
    if init_clear == 1:
        print('=================================== Clear confs begin ===========================================')
        for i in range(1, 7):
            comm_rst = 'at+sqnscfg=%d,1,300,90,600,50' % i
            ser.write(comm_rst + d)
            time.sleep(5)
            parss()
            time.sleep(1)
        print('=================================== Clear confs end =============================================\n\n')

    print('=================================== Initial checks begin ========================================')
    for addc in comm_add:
        ser.write(addc + d)
        time.sleep(4)
        parss()
        time.sleep(1)
    print('=================================== Initial checks end ===========================================\n\n')

    print('=================================== Start tests ==================================================')
    for i in range(1, 7):
        for j in range(1, 9):

            comm_1 = 'at+sqnscfg=%d,%d,300,90,600,50' % (i, j)
            comm_2 = 'at+sqnsd=%d,0,80,"google.com",0,0,1' % i
            comm_3 = 'at+sqnsh=%d' % i

            ser.write(comm_1 + d)
            time.sleep(5)
            parss()
            time.sleep(1)

            ser.write(comm_2 + d)
            time.sleep(9)
            rrr = parss()
            time.sleep(1)
            if rrr == 'FAULT':
                print(timest() + ' ==> ' + 'EEERRROOORRR !!!!!!!!!!!!!!!!!!!!!!!! << HERE SHOULD BE OK')
                break
            if rrr == 'OK':
                ser.write(comm_3 + d)
                time.sleep(3)
                parss()
                time.sleep(1)
            print('=================================================')
        if rrr == 'FAULT':
            for addc in comm_add:
                ser.write(addc + d)
                time.sleep(3)
                parss()
                time.sleep(1)
            break

finally:
    ser.close()
