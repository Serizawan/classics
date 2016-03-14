import time
import threading

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        super().__init__()
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, 'a')
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print('Finished Background File Write to ' + self.out)

def main():
    msg = input('> ')
    bckg = AsyncWrite(msg, 'out.txt')
    bckg.start()
    print('The program can continue while it writes in another thread')
    print('100 + 400 =', 100 + 400)
    bckg.join()
    print('Waited until thread was complete')

if __name__ == '__main__':
    main()
