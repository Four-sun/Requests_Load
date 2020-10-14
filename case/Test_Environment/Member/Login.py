# -*- coding: utf-8 -*-
"""
Created: on 2018-05-14
@author: Four
Project: case\Login.py
Description:登陆
"""
import time
import sys
import requests
from common.log import Logger
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


def loggin_wx():
    try:
            pay_load={
                        "type": "2",
                        "token": "eslinkoauthtoken_e1ee8be6fe414be1be8940b5d4f05f3b",
                        "opid": "oRgEnw-CVUwNu-kAduyK8qm9QeAY",
            }
            logger_message.loginfo(u'%s\t入参%s\t'%(send_time,pay_load))
            logging_wx = requests.get("http://patrol-mobile-qa.eslink.net.cn/member/index.html", params=pay_load)
            logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,logging_wx.url,logging_wx.status_code,logging_wx.text))
            return logging_wx
    except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))


class WxSession(object):
    u"""微信session"""
    def __init__(self):
        self.Session = "8a9e1e91-4b84-42ca-8c69-4fe91aeb4e9c"


def Loging_etbc(self):
    u"""发送请求登陆etbc"""
    try:
        payload={
            "loginName": "zhangyang1",
            "loginPwd": "zj03030418"
        }
        logger_message.loginfo(u'%s\t入参%s\t' % (send_time,payload))
        login_etbc = requests.post('http://etbc-qa.eslink.net.cn/user/login', data=payload)
        self.assertEqual(200,login_etbc.status_code,msg='失败原因：200 != %s' % (login_etbc.status_code))
        logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time, sys._getframe().f_code.co_name, login_etbc.url, login_etbc.status_code, login_etbc.text))
        return login_etbc

    except AssertionError as Error:

        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))

def etbc():
    u"""发送请求登陆etbc"""
    try:
        payload={
            "loginName": "zhangyang1",
            "loginPwd": "zj03030418"
        }
        logger_message.loginfo(u'%s\t入参%s\t' % (send_time,payload))
        login_etbc = requests.post('http://etbc-qa.eslink.net.cn/user/login', data=payload)
        # print(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time, sys._getframe().f_code.co_name, login_etbc.url, login_etbc.status_code, login_etbc.text))
        print(login_etbc.cookies)
        return login_etbc

    except AssertionError as Error:

        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))


if __name__ == '__main__':
    etbc()