#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""



import logging
# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

import dueros.Log as Log
# 导入我们自己编写的application函数:
from BotServer import application
from dueros.Constants import constants

Log.init_log(constants.LOG_PATH)

# https://things.yy845.com:8100/
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('192.168.0.52', 8000, application)
print('Serving HTTP on port 8000...')
logging.info('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
