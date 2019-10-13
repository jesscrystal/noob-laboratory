# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 21:42:18 2018

@author: xg277
"""

import socket  
import threading  
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.connect(("127.0.0.1",8000))  
true=True  
def rec(s):  
    global true  
    while true:  
        t=s.recv(1024).decode("utf8")  #客户端也同理  
        if t == "exit":  
            true=False  
        print('收到消息:',t)  
trd=threading.Thread(target=rec,args=(s,))  
trd.start()  
while true:  
    t=input('>>>:')  
    s.send(t.encode('utf8'))  
    if t == "exit":  
        true=False  
        s.close()
        break
