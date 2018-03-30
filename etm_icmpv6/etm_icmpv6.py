import sys

str1 = "ETM/ICMP6 - Forwarded msg content"
str2 = "ETM/ICMP6 - (L="
str3 = "<END>"
tmps = ""
flag_msg = 0
flag_l = 0
flag_end = 0

def getnewline():
    line = file_in.readline()
    si = line.replace('\n', '').replace('\r', '')
    return si

try:
    file_in=open(sys.argv[1], 'r')
    file_out=open(sys.argv[1]+'.pcapng', 'w+')
    ss = getnewline()
    while ss:
        if ss.find(str1) > -1:
            ss = getnewline()
            if ss.find(str2) > -1:
                tmps = ss[0:15].replace('.', '')
                tmps = tmps.replace("'", '.')
                tmps += '\n'
                file_out.write(tmps)                #=============================change
                ss = '000000 ' + getnewline()

                while ss.find(str3) == -1:
                    ss = ss.replace('  ', ' ') + ' '
                    file_out.write(ss)
                    ss = getnewline()
                file_out.write('\n')
        ss = getnewline()

finally:
    file_in.close()
    file_out.close()
    print('=================================================')