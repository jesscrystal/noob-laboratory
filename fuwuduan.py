# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 21:07:57 2018

@author: xg277
"""

import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.setblocking(False)#设置非阻塞模式
s.bind(("127.0.0.1",8000))  
s.listen(5)  
sock,addr=s.accept()
true=True  
def rec(sock):  
    global true  
    while true:
        t=sock.recv(1024).decode('utf8')#消息接收方法
        if t == "exit":
            true=False  
        print('收到消息:',t)
trd=threading.Thread(target=rec,args=(sock,))
trd.start()
while true:
    t=input('>>>:')
    sock.send(t.encode('utf8'))
    if t == "exit":  
        true=False  
        s.close()
        break