#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/1/23 15:09
#@Author: zhangdelong
#@File  : clienthps.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 80

# 连接服务，指定主机和端口

s.connect((host, port))


while True:
    user_input = input('请输入要传输的信息：')
    s.sendall(bytes(user_input, encoding="utf-8"))
    msg =  s.recv(1024) #recv方法用于接收数据，后面1024是每次接收数据的最大长度，可以自己设定
    print (msg.decode('utf-8'))   #打印服务器端传输过来的内容
s.close() #关闭连接