# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 22:40:36 2018

@author: xg277
"""

import socket,sys
HOST = '192.168.1.6'
PORT = 8998
ADDR =(HOST,PORT)
BUFSIZE = 1024

sock = socket.socket()
try:
    sock.connect(ADDR)
    print('have connected with server')
    while True:
      data = input('lockey# ')
      if data=='quit':
        sock.close()
        break
      if len(data)>0:
        print('send:',data)
        sock.sendall(data.encode('utf-8')) #不要用send()
        recv_data = sock.recv(BUFSIZE)
        print('receive:',recv_data.decode('utf-8'))
      else:
        sock.close()
        break
except Exception:
    print('error')
    sock.close()
    sys.exit()