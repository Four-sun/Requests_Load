# -*- coding: utf-8 -*-
"""
Created: on 2018-05-14
@author: Four
Project: case\Login.py
Description:登陆
"""
import time,os
import sys
import requests
from ruamel import yaml
from common.log import Logger
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
current_path = os.path.dirname(os.path.realpath(__file__))


def loggin_wx():
    try:
            pay_load={
                        "type": "1",
                        "token": "eslink_7cc9b182028f4d3991e14553400abea3",
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
        self.Session = "0ab0e0b3-ce0e-4d22-9eb8-33fe5348c12a"


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
        return login_etbc.cookies

    except AssertionError as Error:

        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))


def new_Loging_etbc():
    u"""发送请求登陆etbc"""
    try:
        payload = {
            "loginName": "xiaozhangyang",
            "loginPwd": "xiaozhangyang"
        }
        logger_message.loginfo(u'%s\t入参%s\t' % (send_time, payload))
        login_etbc = requests.post('http://etbc-qa.eslink.net.cn/user/login', data=payload)
        logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time, sys._getframe().f_code.co_name, login_etbc.url, login_etbc.status_code, login_etbc.text))
        SESSION = login_etbc.cookies["SESSION"]
        # SERVERID = login_etbc.cookies["SERVERID"]
        logger_message.loginfo('SESSION:%s' % (SESSION))
        # s = [SESSION,SERVERID]
        s = [SESSION]
        return s

    except AssertionError as Error:

        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))


def write_yaml(value):
    """
    把获取到的token值写入到yaml文件
    :param value:
    :return:
    """
    ypath = os.path.join(current_path, "token.yaml")
    # 需写入的内容
    # t = {"SESSION": value[0],"SERVERID": value[1]}
    t = {"SESSION": value[0]}
    # 写入到yaml文件
    with open(ypath, "w", encoding="utf-8") as f:
        yaml.dump(t, f, Dumper=yaml.RoundTripDumper)


if __name__ == '__main__':

    case = new_Loging_etbc()
    write_yaml(case)