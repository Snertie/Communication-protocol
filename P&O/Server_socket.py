__author__ = 'Bert'


import socket, time,os, random

class Server():
  def __init__(self,Adress=('',7000),MaxClient=2):
      self.s = socket.socket()
      self.s.bind(Adress)
      self.s.listen(MaxClient)
      self.connections = 0
  def WaitForConnection(self):
      if self.connections == 0:
        (self.Client, self.Adr)=(self.s.accept())
        print('Got a connection from: '+str(self.Adr)+'.')
        self.connections += 1
      else:
          (self.Client2, self.Adr2)=(self.s.accept())
          print('Got a connection from: '+str(self.Adr2)+'.')

  def receive(self):
      data_1 = self.Client.recv(1024).decode()

      data_2 = self.Client2.recv(1024).decode()
      print ("Sensor huis 1: " +str(data_1))
      print ("Sensor huis 2: " +str(data_2))
      self.Client.send('Aangekomen'.encode())
      self.Client2.send('Aangekomen'.encode())
      data_1 = ''
      data_2 = ''


Sensor=Server()
Sensor.WaitForConnection()
Sensor.WaitForConnection()
print Sensor.Client
print Sensor.Client2

while 1 < 2:
    Sensor.receive()