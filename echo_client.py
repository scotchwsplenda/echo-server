# https://www.youtube.com/watch?v=6DtinPYTZBY

import socket
import sys


def client(log_buffer=sys.stderr):

    server_address = ('127.0.0.1', 10000)
    # xTODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    # xTODO: connect your socket to the server here.
    sock.connect(server_address)
    print('Helo Seattle, Im listening. \n Type ''exit'' to exit program')
    msg = input('Client> ')
    while msg != 'exit':
        # print('sending "{0}"'.format(msg), file=log_buffer)
        sock.sendall(msg.encode('utf8'))
        while True:# this True block is 'buffering' the 'echo'
            chunk = sock.recv(16)
            print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            if len(chunk) < 16:
                break
        msg = input('Client> ')
    sock.sendall('exit'.encode('utf8'))
    sock.close()


if __name__ == '__main__':
    client()
