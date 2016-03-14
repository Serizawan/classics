import socket

def main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.connect((host, port))
    msg = input('> ')
    while msg != 'q':
        s.send(msg.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print('Received from server: ' + data)
        msg = input('> ')
    s.close()

if __name__ == '__main__':
    main()
