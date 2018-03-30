import serial
import argparse
import logging
import sys
import time
import filecmp
import re
import ftplib
import tempfile

try:
    import queue
except ImportError:
    import Queue as queue

logging.basicConfig(format='%(asctime)s: %(message)s')

class ATException(Exception):
    pass

class AtParser(serial.Serial):
    def __init__(self, pname, bdrate, rcts=1, timeout=10, bytesize=8, parity='N', stopbits=1):
        super(AtParser, self).__init__(port=pname, baudrate=bdrate,
                rtscts=rcts, timeout=timeout, bytesize=bytesize, parity=parity,
                stopbits=stopbits)

    def readLine(self):
        out = ""
        while not out.endswith("\r\n"):
            out += self.read(1)
        out = out.replace('\n', '').replace('\r', '')
        logging.info("Got line: %s", out)
        return out
    
    def readBinary(self, n):
        blob = bytearray(self.read(n))
        logging.info("Got line: %s", " ".join("{:02x}".format(c) for c in blob))
        return blob

    def writeLine(self, cmd):
        self.write("{0}{1}".format(cmd, "\r\n"))

    def sendAt(self, cmd, timeout=5, OkInAnswer=False):
        start = time.time()
        end = start + timeout
        URCs = ["^SIS", "^SISR"]
        self.write("{0}{1}".format(cmd, "\r\n"))
        lines = ''
        line = self.readLine()
        if line == "ERROR":
            raise ATException("AT command (%r) ended with ERROR" % (cmd))
        while line != "OK":
            print(line)
            #print "LINE NOT OK: ", ":".join("{:02x}".format(ord(c)) for c in line)
            if time.time() > end:
                raise ATException("AT command (%r) ended by timeout" % (cmd))
            for urc in URCs:
                if line.startswith(urc):
                    line = ''
            lines += line
            line = self.readLine()
            if line == "ERROR":
                raise ATException("AT command (%r) ended with ERROR" % (cmd))
        if OkInAnswer:
            if line == "OK":
                lines += line
            else:
                raise ATException("No OK is printed at the end of AT command (%r)" % (cmd))
        return lines

    def send_raw_at(self, cmd, timeout=5, throw=0):
        start = time.time()
        end = start + timeout
        URCs = ["^SIS", "^SISR"]
        CMS_ERROR = "+CMS ERROR:"
        self.write(cmd)
        lines = ''
        line = self.readLine()
        if line == "ERROR\r\n":
            raise ATException("AT command (%r) ended with ERROR" % (cmd))
        while line != "OK\r\n":
            #print "LINE NOT OK: ", ":".join("{:02x}".format(ord(c)) for c in line)
            if time.time() > end:
                print("AT command "+ cmd + " ended by timeout")
                return lines
            for urc in URCs:
                if line.startswith(urc):
                    line = ''
            lines += line
            if line.startswith(CMS_ERROR):
                break
            line = self.readLine()
            if line == "ERROR\r\n":
                if throw:
                    raise ATException("AT command (%r) ended with ERROR" % (cmd))
                logging.error("AT command (%r) ended with ERROR", cmd)
                break
        lines += line
        return lines
    
    
    def wait_until(self, string, timeout=5):
        end = time.time() + timeout
        common_line = ""
        while True:
            if end < time.time():
                logging.error("Warning! waiting for '%s' ended with timeout!",
                        string)
                return common_line
            if self.inWaiting():
                line = self.readLine()
                common_line += line
                logging.info("Wating for line %s, current line: %s", string, line)
                if line.startswith(string):
                    break
        return common_line

    def wait_URCs(self, URCs, timeout=5):
        match_counts = {}
        length = len(URCs)
        common_line = ""
        for URC in URCs:
            match_counts[URC] = 0
        end = time.time() + timeout
        while True:
            if end < time.time():
                logging.error("Warning! waiting for '%s' ended with timeout!",
                        "".join(URCs))
                return common_line
            if self.inWaiting():
                line = self.readLine()
                common_line += line
                for string in URCs:
                    logging.info("Wating for line %s, current line: %s", string, line)
                    if line.startswith(string):
                        match_counts[string] = 1
                if sum(match_counts.values()) == length:
                    break
        return common_line

    def waitUntil(self, string, timeout=5):
        end = time.time() + timeout
        while True:
            if end < time.time():
                logging.error("Warning! waiting for '%s' ended with timeout!",
                        string)
                return None
            if self.inWaiting():
                line = self.readLine()
                logging.info("Wating for line %s, current line: %s", string, line)
                if line.startswith(string):
                    break
        return line

