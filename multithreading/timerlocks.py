import time
import threading

tLock = threading.Lock()

def timer(name, delay, repeat):
    print('Timer: ' + name + ' started')
    tLock.acquire()
    print(name + ' has acquired the Lock')
    while repeat:
        time.sleep(delay)
        print(name + ': ' + str(time.ctime(time.time())))
        repeat -= 1
    print(name + ' is releasing the lock')
    tLock.release()
    print('Timer: ' + name + ' completed')

def main():
    t1 = threading.Thread(target=timer, args=('Timer1', 1, 5))
    t2 = threading.Thread(target=timer, args=('Timer2', 2, 5))
    t1.start()
    t2.start()
    print('Main completed')

if __name__ == '__main__':
    main()
