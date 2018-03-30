import serial
import time
import datetime
import sys
import io

tti = 0.008  # <<< timeout between sending seconds
try:
    def timest():
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')
        return st


    def parss2(i):
        s = ser.readlines()
        qq = 0
        for lines in s:
            ss = lines.decode().replace('\n', '').replace('\r', '')
            if i > 0:
                print(str(i) + " " + timest() + "  " + ss)
            else:
                print(timest() + "  " + ss)
            # if ss == 'CONNECT':
            #    qq = 1
            #    break
            if ss == 'OK':
                qq = 2
                break
                # if ss == 'stlport: out of memory':
                #    qq = 3
                #    break
        return qq


    ser = serial.Serial('/dev/ttyXRUSB1', 921600, timeout=0, parity=serial.PARITY_NONE, rtscts=1)  # open serial port
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
    print(' Port = ' + ser.name)
    #time.sleep(7);
    d = "\r"
    z = "\x1A"
    comm_0 = 'ATE1'
    comm_1 = 'AT+SQNSH=1'
    comm_2 = 'AT+SQNSD=1,0,1233,"192.168.3.1",0,0,1'
    comm_3 = 'AT+SQNSSENDTEST=1,"121212"'
    comm_4 = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
    comm_5 = 'AT+SQNSH=1'
    comm_6 = 'AT+SQNSSENDEXT=1,100'
    comm_7 = 'AT+SQNSS'
    comm_8 = 'AT+SQNSSEND=1'
    comm_0 += d
    comm_1 += d
    comm_2 += d
    comm_3 += d
    comm_5 += d
    comm_6 += d
    comm_7 += d
    comm_8 += d
    err = 0
    print('=================================== Start tests ==================================================')
    ser.write(comm_0.encode())  # ============== send AT
    time.sleep(3)
    parss2(0)
    ser.write(comm_1.encode())  # ============== send AT+SQNSH=1
    time.sleep(3)
    parss2(0)
    ser.write(comm_2.encode())  # ============== send AT+SQNSD=1,0,123,"192.168.3.1",0,0,1
    time.sleep(4)
    b = 0
    if parss2(0) == 2:
        print 'Sending data (%s), timeout=%.2f' % (comm_3, tti)

        b = 0
        for i in range(1, 10000):
#===============================================================================
#            ser.write(comm_8.encode()) #======= AT+SQNSSEND=1
#            time.sleep(0.01)
#            ser.write(comm_4.encode())
#            ser.write(z.encode())
#            time.sleep(0.02)
#            time.sleep(tti)
#            cc = parss2(i)
#===============================================================================
            ser.write(comm_3.encode())    #======== AT+SQNSSENDTEST=1,"121212"
            time.sleep(tti)
            cc = parss2(i)
#===============================================================================
#            cc = parss2(i)
#            ser.write(comm_6.encode()) #======= AT+SQNSSENDEXT=1,100
#            time.sleep(0.08)
##            cc = parss2(i)
#            ser.write(comm_4.encode())
#            time.sleep(0.05)
#            cc = parss2(i)
#            time.sleep(tti)


        # print("")
        # if cc == 2:
        #    print 'OK\r\n'
        # err = 12
        # break
        # else:
        #    err = 12
        #    print('Error!\r\n')

finally:

    # if err != 12:
    #    print('')
    #    print('Log:')
    # time.sleep(1)
    # ser.write(comm_8.encode())  # ============ AT+SEXIT
    # time.sleep(3)
    # parss2()
    # ser.write(comm_6.encode())  # ============ cbe"infoall"
    # time.sleep(1)
    # parss2()
    print('===================== Test end ============================')
ser.close()
