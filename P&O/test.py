__author__ = 'Jelle'

import time

class communicator:
    def __init__(self, address, key):
        communicator.address = address
        communicator.key = key


class create_message:
    def __init__(self, sender, receiver, data=None):
    # header creation
        create_message.sender = self.string_generator(sender, 4)
        create_message.receiver = self.string_generator(receiver, 4)
        create_message.time = self.string_generator(int(time.time()), 32)
        create_message.header = create_message.sender + create_message.receiver + create_message.time
    # data creation
        if data != None:
            create_message.data = ''

            for device in data:
                #print message.data, device
                length = self.string_generator(len(device[4:]), 4)
                information = device[:4] + length + device[4:]
                print information
                create_message.data += information

    def string_generator(self, item, length):
        format_value = '#0' + str(length) + 'b'
        return str(format(int(item), format_value)[2:])
    def send(self):
        return self.header + self.
    def receive(self):
# class read_message:
#     def __init__(self, message):
#         self.header = message[:40]
#         self.data = message[40:]
#     def dissect_header(self):
#         self.sender = self.header[:4]
#         self.receiver = self.header[4:8]
#         self.timestamp = self.header[8:]


# M = create_message(1,2,['1001001101','000110110'])
# print M.header, M.data

# PI = communicator("Bert",1234)
# M = message('0000','0001')
# print message.header
# print bin(message.header)
# print len(bin(message.header))


