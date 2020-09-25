import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("making a server on {0}:{1}".format(*address), file=log_buffer)
    sock.bind(address)
    sock.listen(1)
    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)
            try:
                conn, addr = sock.accept()
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)
                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    bytesize = 16
                    data = conn.recv(bytesize)
                    print('received "{0}"'.format(data.decode('utf8')))
                    conn.sendall(data) #need to add the data
                    print('sent "{0}"'.format(data.decode('utf8')))
                    print('String has {} bytes in it'.format(len(data)))
                    if len(data) < 16:
                        break
            except Exception as e:
                traceback.print_exc()
                sys.exit(1)
            finally:
                conn.close()
                print(
                    'echo complete, client connection closed', file=log_buffer
                )

    except KeyboardInterrupt:
        conn.close()
        sock.close()
        print('quitting echo server', file=log_buffer)
        sys.exit(0)


if __name__ == '__main__':
    server()
    sys.exit(0)
