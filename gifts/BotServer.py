#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/3

"""
    desc:pass
"""
from cgi import parse_qs, escape
import json
import logging
from ChristmasGifts import AnimalSounds
import sys  # 要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法

reload(sys)
sys.setdefaultencoding('utf-8')


def application(environ, start_response):
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except(ValueError):
        request_body_size = 0
    request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')
    print('request_body = %s\n' % request_body)
    logging.info('request_body = %s\n' % request_body)
    if not request_body:
        return writeResponse(start_response, '未获取到请求数据')

    bot = AnimalSounds(request_body)
    # 添加错误回调方法
    # bot.set_callback(bot.errorCallBack())

    # 验证签名enableVerifyRequestSign  disableVerifyRequestSign 关闭验证签名
    # bot.initCertificate(environ).enableVerifyRequestSign()
    bot.init_certificate(environ).disable_verify_request_sign()
    #bot.set_private_key(priKey)

    body_str = bot.run()
    print(body_str)
    return writeResponse(start_response, body_str)


def writeResponse(start_response, body_str):
    body = body_str.encode('utf-8')
    # ('Content-Encoding', 'utf-8')
    response_headers = [('Content-Type', 'application/json'),
                        ('Content-Length', str(len(body))),
                        ]
    status = '200 OK'
    print(body)
    logging.info('response_body = %s\n' % body)
    start_response(status, response_headers)
    return [body]