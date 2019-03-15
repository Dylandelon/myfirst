#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/1/23 15:06
#@Author: zhangdelong
#@File  : serverhps.py
# 导入 socket、sys 模块
import socket
import sys
import json
import logging
filelog = True
path = r'messagelog.txt'

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)

# 调用模块时,如果错误引用，比如多次调用，每次会添加Handler，造成重复日志，这边每次都移除掉所有的handler，后面在重新添加，可以解决这类问题
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)

# file log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
if filelog:
    fh = logging.FileHandler(path,encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

# console log
formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 80

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)
data = {
    'code': "10000",
    'msg': "2222"
}
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    # print("连接地址: %s" % str(addr))
    logger.info("连接地址: %s" % str(addr))
    content = clientsocket.recv(2048)
    if not content: break  # 如果客户端传输过来的信息为空，关闭连接
    logger.info(str(content.decode('utf-8')))
    # clientsocket.send(Data)  # 把客户端传来的信息传给客户端

    # print("接收到的内容: %s" % str(content.decode('utf-8')))
    # logging.info(content)


    msg = json.dumps(data)
    clientsocket.send(msg.encode('utf-8'))
clientsocket.close()   #关闭套接字，可以把close写在循环外面，这样就可以一直通信，直到客户端主动断开