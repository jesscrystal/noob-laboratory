# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:07:08 2018

@author: xg277
"""

#客户端
import socket
sock=socket.socket()
sock.connect(("127.1.0.1",8000))
 
while True:
    data=input(">>>")
    sock.send(data.encode("utf8"))
    res=sock.recv(1024)
    print(res.decode("utf8"))
    if data=='exit':
        sock.close()
        break