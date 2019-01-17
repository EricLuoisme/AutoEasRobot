# Communication server program
from NAudioProcess.data import Network_Connection
import socket
import time

HOST = Network_Connection.HOST
PORT = Network_Connection.PORT
TIMEOUT = Network_Connection.SUBSCEN_MAXTIME

s = None
conn = None
addr = None


def connect(send_it=False):
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


def receive(sub_scenario=False):
    """
    used to get the message from the robot
    :return data: return the message that we get from the robot
    """
    if sub_scenario:

        start = time.perf_counter()
        while time.perf_counter() - start < TIMEOUT:
            t = connect()
            if t:
                break
        if t is not True:
            print('超时')
            return '超时'

    else:
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
            # return data.decode('utf-8')
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
