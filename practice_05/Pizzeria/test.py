from time import sleep
from random import randint
from threading import Thread


def cook(name):
    sleep(randint(0, 3))
    print("Start cooking - ", name)
    sleep(randint(0, 6))
    print("In process - ", name)
    sleep(randint(0, 3))
    print("Finish! - ", name)


t1 = Thread(target=cook, args=("t1",))
t2 = Thread(target=cook, args=("t2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads are finished!")