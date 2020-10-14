# -*- coding: utf-8 -*-
"""
Created: on 2018-05-15
@author: Four
Project: case\member_openChildCard.py
URL: http://patrol-mobile-qa.eslink.net.cn/member/member/openChildCard
Description:会员管理开通附属卡接口
"""
import unittest
import os
import time
import sys
import requests
from case.Test_Environment.Member.Login import WxSession
from case.Test_Environment.Member.Login import loggin_wx
from common.Request_Package import send_requests
from common.Excel_readline import ExcelUtil
from common.log import Logger

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "test_member_interface.xlsx")
Sheet_Name = "member_openChildCard"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
wx_session=WxSession().Session


class member_openChildCard(unittest.TestCase):

    def test_openChildCard_1(self):
        u"""开通附属卡,附属卡已存在的情况"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                "SERVERID": "%s" % cookie,
                "SESSION": "%s" % wx_session,
            }
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_openChildCard_2(self):
        u"""开通附属卡，主卡人ID错误"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                "SERVERID": "%s" % cookie,
                "SESSION": "%s" % wx_session,
            }
            test_id = 1
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise
    def test_openChildCard_3(self):
        u"""开通附属卡，主卡ID错误"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                "SERVERID": "%s" % cookie,
                "SESSION": "%s" % wx_session,
            }
            test_id = 2
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_openChildCard_4(self):
        u"""开通附属卡，附属卡持卡人姓名与身份证不符"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                "SERVERID": "%s" % cookie,
                "SESSION": "%s" % wx_session,
            }
            test_id = 3
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_openChildCard_5(self):
        u"""开通附属卡，条件加上手机号"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                "SERVERID": "%s" % cookie,
                "SESSION": "%s" % wx_session,
            }
            test_id = 4
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise
if __name__ == "__main__":
    unittest.main()