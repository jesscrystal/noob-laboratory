# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 16:36:44 2018

@author: xg277
"""
import socket
import threading                                                # 导入多线程模块
print("等待连接中......")
HostPort = ('127.0.0.1',9999)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)            # 创建socket实例
s.bind(HostPort)
s.listen(1)
conn,addr = s.accept()
true=True
addr = str(addr)
print('正在与 : %s 连接' %addr )
def Receve(conn):                                               # 将接收定义成一个函数
    global true                                                 # 声明全局变量，当接收到的消息为quit时，则触发全局变量 true = False，则会将socket关闭
    while true:
        data = conn.recv(1024).decode('utf8')          
        if data == 'quit':
            true=False
        print("收到消息: "+data+" from"+addr)            # 当接收的值为'quit'时，退出接收线程，否则，循环接收并打印
thrd=threading.Thread(target=Receve,args=(conn,))               # 线程实例化，target为方法，args为方法的参数 
thrd.start()                                                    # 启动线程
while true:
    user_input = input('>>>')
    conn.send(user_input.encode('utf8'))                        # 循环发送消息
    if user_input == 'quit':                                    # 当发送为‘quit’时，关闭socket
         conn.close()
         s.close()
print("u are sb")