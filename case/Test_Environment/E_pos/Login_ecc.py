# -*- coding: utf-8 -*-
"""
Created: on 2018-04-19
@author: Four
Project: case\Test_Environment\E_pos
"""
import time
import sys
import requests
from common.log import Logger

logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


def Login_ecc():
    u"""发送请求登陆etbc"""
    try:
        payload={
            "loginName":"admin",
            "loginPass":"admin123",
            "guidStr":"7a2b9053-86b2-4875-b7a4-e8f8b821b4b0"
        }
        logger_message.loginfo(u'%s\t入参%s\t'%(send_time,payload))
        login_etbc=requests.post('http://ecc-qa.eslink.net.cn/sysuser/account/doSysUserLogin',data=payload)
        print(login_etbc.cookies)
        logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,login_etbc.url,login_etbc.status_code,login_etbc.text))
        return login_etbc

    except AssertionError as Error:

        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
