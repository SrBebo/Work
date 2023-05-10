import random
import time
import string
from collections import deque

queue = []

def addClient (queue):
    queue.append(random.choice(string.ascii_letters))
    return print("The client: ",queue[-1]," has been added to the queue")


def attendClient (queue):
    if len(queue) > 0:
        print("The client: ",queue[0]," has been attended")
        queue.pop(0)
    else:
        print("There are no clients to attend")
    return queue

while True:
    if random.random()<0.5:
        addClient(queue)
    else:
        if queue:
            attendClient(queue)
    time.sleep(2)
