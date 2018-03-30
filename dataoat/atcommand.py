class huawei:
    connId = range(1, 6)  # Socket connection identifier [1-6]
    txProt = range(0, 1)  # Transmission protocol. 0-TCP, 1-UDP
    rPort = 80  # Remote host port to contact. Integer type [0-65535].
    IPaddr = '192.168.3.1'  # Address of the remote host.
    closureType = 0  # Socket closure behaviour for TCP, has no effect for UDP connections.
    # 0 - local host closes immediately when remote host has closed (default)
    # 1 - local host closes after an escape sequence (+++) or after remote closure
    lPort = 0  # UDP connections local port, has no effect for TCP connections.
    connMode = 0  # Connection mode. 0 - online mode connection (default) 1 - command mode connection
    cid = 1  # PDP context identifier [1-5]
    pktSz = 0  # Packet size to be used by the TCP/UDP/IP stack for data sending. Used for online data mode only [
    # 0-1500].
    # 0 - automatically chosen by the device (default 300)
    # 1-1500 - packet size in bytes
    maxTo = 0  # Exchange timeout, if there is no data exchange within this timeout, period the connection is closed
    # [0-65535].
    # 0 - no timeout
    # 1-65535 - timeout value in seconds (default 90 s.)
    connTo = 0  # Connection timeout; if we can’t establish a connection to the remote within this timeout period,
    # an error is raised [0,10-1200].
    # 0 - no timeout
    # 10-1200 - timeout value in hundreds of milliseconds (default 600)
    txTo = 0  # Data sending timeout. Data are sent even if they are less than max packet size, after this period.
    # Used for online data mode only [0-255].
    # 0 - no timeout
    # 1-255 - timeout value in hundreds of milliseconds (default 50)

    srMode = 0  # SRing URC mode
    # 0 - normal mode (default), SQNSRING : <connId>
    # 1 - data amount mode, SQNSRING : <connId>,<recData>
    # 2 - data view mode, SQNSRING : <connId>,<recData>,<data>

    recvDataMode = 0  # "Received data view mode” presentation format
    # 0 - data represented as text (default)
    # 1 - data represented as sequence of hexadecimal numbers (from 00 to FF)
    # keepalive = 0 #Not used for the moment
    listenAutoRsp = 0  # "Listen auto-response mode”, that affects AT+SQNSL command
    # 0 - deactivated (default). Call AT+SQNSA to accept incomming TCP connection.
    # 1 - activated. Incomming TCP connection is automatically accepted. Modem remains in command mode.
    sendDataMode = 0  # "Sent data view mode” presentation format
    # 0 - data represented as text (default)
    # 1 - data represented as sequence of hexadecimal numbers (from 00 to FF)
    maxByte = 1500  # Max number of bytes to read [1-1500]
    bytestosend = 100  # Number of bytes to be sent [1-1500]
    listenState = 1  # 0 - Close listening socket, 1 - Open listening socket
    listenPort = 1234  # Listening TCP port, Integer [0-65535].

    # 6.47.1 Socket Dial: +SQNSD #AT+SQNSD=<connId>,<txProt>,<rPort>,<IPaddr>[,<closureType> [,<lPort> [,<connMode>]]]
    def SQNSD(self, connId, txProt, rPort, IPaddr, closureType, lPort, connMode):

        out = 'AT+SQNSD=%d,%d,%d,"%s",%d,%d,%d' % (connId, txProt, rPort, IPaddr, closureType, lPort, connMode)

        return out

    # 6.47.2 Socket Restore: +SQNSO
    # AT+SQNS0=<connId>

    # 6.47.3 Socket Configuration: +SQNSCFG
    # AT+SQNSCFG=<connId>, <cid>, <pktSz>, <maxTo>,<connTo>, <txTo>

    # 6.47.4 Socket Configuration Extended: +SQNSCFGEXT
    # AT+SQNSCFGEXT=<connId>, <srMode>,<recvDataMode>, <keepalive>,[<listenAutoRsp>], [<sendDataMode>]

    # 6.47.5 Socket Shutdown: +SQNSH
    # AT+SQNSH=<connId>

    # 6.47.6 Receive Data in Command Mode: +SQNSRECV
    # AT+SQNSRECV=<connId>,<maxByte>

    # 6.47.7 Send Data In Command Mode : +SQNSSEND
    # AT+SQNSSEND=<connId>. . . <CTRL+Z>

    # 6.47.8 Send Data In Command Mode : +SQNSSENDEXT
    # AT+SQNSSENDEXT=<connId>,<bytestosend>

    # 6.47.9 Socket Status : +SQNSS
    # AT+SQNSS

    # 6.47.10 Socket Listen : +SQNSL
    # AT+SQNSL=<connId>,<listenState>,<listenPort>[,<closureType>]

    # 6.47.11 Socket Accept: +SQNSA
    # AT+SQNSA=<connId>[,<connMode>]

    # 6.47.12 Socket Listen UDP : +SQNSLUDP
    # AT+SQNSLUDP=<connId>,<listenState>,<listenPort>

    def __init__(self):
        return 'Hello'

    def __del__(self):
        pass
