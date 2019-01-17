# Communication Client program
from data import Network_Communication
import socket

HOST = Network_Communication.HOST
PORT = Network_Communication.PORT
TIMEOUT = Network_Communication.SUBSCEN_MAXTIME

s = None
conn = None
addr = None


def connect(send_it=False, time_out=None):
    """
    used to connect
    :return: only when we connect successfully will stop this function and return True
    """
    global s, conn, addr
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            if send_it is True:
                s.connect(sa)
            else:
                s.bind(sa)
                s.listen(1)
        except OSError as msg:
            s.close()
            s = None
            continue
        break

    if s is not None:
        return True
        # if s is None:
        #     print('could not open socket')
        #     sys.exit(1)


def receive():
    """
    used to get the message from the robot
    :return data: return the message that we get from the robot
    """
    while True:
        t = connect()
        if t:
            break

    global s, conn, addr
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            #return data.decode('utf-8')
            return str(data, encoding='utf-8')


def send(message):
    """
    used to send message back to the robot
    :param message: string, specific sentence of particular scenario
    :return:
    """
    while True:
        t = connect(True)
        if t:
            break

    global s
    # s.sendall(message.encode('utf-8'))  # here we must send byte type
    s.sendall(bytes(message, encoding='utf-8'))

