#!/usr/bin/python

import socket




s = socket.socket()
print(s.connect_ex(("192.168.0.111", 5000)))
s.close()
