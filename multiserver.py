# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 22:38:22 2018

@author: xg277
"""

from socketserver import BaseRequestHandler,ThreadingTCPServer
import threading

BUF_SIZE=1024

class Handler(BaseRequestHandler):
    def handle(self):
        address,pid = self.client_address
        print('%s connected!'%address)
        while True:
            data = self.request.recv(BUF_SIZE)
            if len(data)>0:
                print('receive=',data.decode('utf-8'))
                cur_thread = threading.current_thread()
                #sock.sendall(data.encode('utf-8'))
                #response = '{}:{}'.format(cur_thread.ident,data)
                self.request.sendall('response'.encode('utf-8'))
                print('send:','response')
            else:
                print('close')
                break
            control = input('command# ')
            if control=='quit':
                sock.close()
                break

if __name__ == '__main__':
    HOST = '192.168.0.107'
    PORT = 8998
    ADDR = (HOST,PORT)
    server = ThreadingTCPServer(ADDR,Handler)  #参数为监听地址和已建立连接的处理类
    print('listening')
    server.serve_forever()  #监听，建立好TCP连接后，为该连接创建新的socket和线程，并由处理类中的handle方法处理
    print(server)