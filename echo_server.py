import socket
import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    sock.bind(address)
    sock.listen(5)
    try:
        print('waiting for a connection', file=log_buffer)
        conn, addr = sock.accept()
        print('connection - {0}:{1}'.format(*addr), file=log_buffer)
        while True:#this true loop is for the exit
            while True:#this true loop is to 'buffer'
                bytesize = 16
                data = conn.recv(bytesize)
                print('received "{0}"'.format(data.decode('utf8')))
                conn.sendall(data) #it seems you cannot monkey around with an f string here
                print('sent "{0}"'.format(data.decode('utf8')))
                print('String has {} bytes in it'.format(len(data)))
                if len(data) < 16:
                    break
            if data == 'exit':
                break
    except Exception:
        sys.exit(1)
    finally:
        conn.close()
        print('echo complete, client connection closed', file=log_buffer)


if __name__ == '__main__':
    server()
