import socket

def main():
    host = '127.0.0.1'
    port = 5002
    server = ('127.0.0.1', 5001)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    msg = input('> ')
    while msg != 'q':
        s.sendto(msg.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Received from server: ' + data)
        msg = input('> ')
    s.close()

if __name__ == '__main__':
    main()

