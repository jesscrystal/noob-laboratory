# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:05:15 2018

@author: xg277
"""

#服务端
import socket
import select
sock=socket.socket()
sock.bind(("127.5.0.1",8000))
sock.listen(5)
 
# sock.setblocking(False)
inputs=[sock,]
while True:
    r,w,e=select.select(inputs,[],[]) #监听有变化的套接字，
 
    for obj in r:
        if obj==sock:
            conn,addr=obj.accept()
            inputs.append(conn)  #l=[sock,conn]
        else:
            data=obj.recv(1024)
            print(data.decode("utf8"))
            send_data=input(">>>")
            obj.send(send_data.encode("utf8"))
        if data.decode("utf8")=='exit':
            sock.close()
            break
            