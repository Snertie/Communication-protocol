__author__ = 'Bert'
import time

class communicator:
    def __init__(self, address, key):
        communicator.address = address
        communicator.key = key





class message:
    def __init__(self, sender, receiver, data=None):
        message.sender = sender
        message.receiver = receiver
        message.time = int(time.time())

        header = [sender, receiver, str(message.time)]
        message.header = int(''.join(header))


PI = communicator("Bert",1234)
M = message('0000','0001')
print message.header
print bin(message.header)
print len(bin(message.header))


