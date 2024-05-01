from threading import Thread
from time import sleep


def print_number():
    for i in range(1, 11):
        print('#', i, '#')
        sleep(1)


def print_char():
    for ch in range(ord('a'), ord('j')+1):
        print('$', chr(ch), '$')
        sleep(1)


num = Thread(target=print_number)
char = Thread(target=print_char)

num.start()
char.start()

num.join()
num.join()
