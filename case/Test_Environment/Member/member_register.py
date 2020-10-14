# -*- coding: utf-8 -*-
"""
Created: on 2018-05-02
@author: Four
Project: case\member_register.py
URL: http://patrol-mobile-qa.eslink.net.cn/member/register
Description:注册会员完成之后需完善会员信息（移动端)
"""
import unittest
import os
import time
import sys
import requests
from common.Request_Package import send_requests
from common.Excel_readline import ExcelUtil
from case.Test_Environment.Member.Login import loggin_wx
from case.Test_Environment.Member.Login import WxSession
from common.log import Logger

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "test_member_interface.xlsx")
Sheet_Name = "member_register"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
wx_session=WxSession().Session


class member_register(unittest.TestCase):

    def sendSmsCode(self):
        try:
            post_body = {
                "mobilePhone": "18858271977"
            }
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                "SERVERID": "%s" % cookie,
                "SESSION": "%s" % wx_session,
            }
            send_message = requests.post(url="http://patrol-mobile-qa.eslink.net.cn/member/member/sendSmsCode", data=post_body, cookies=cookies)
            logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,send_message.url,send_message.status_code,send_message.text))

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_register_1(self):
        u"""会员管理开通会员"""
        try:
            member_register.sendSmsCode(self)
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

    def test_register_2(self):
        u"""注册会员缺少参数：手机号"""
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

    def test_register_3(self):
        u"""注册会员缺少参数：身份证"""
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

    def test_register_4(self):
        u"""注册会员缺少参数：验证码"""
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

    def test_register_5(self):
        u"""姓名字符超限"""
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

    def test_register_6(self):
        u"""身份证错误位数：17位"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                        "SERVERID": "%s" % cookie,
                        "SESSION": "%s" % wx_session,
                    }
            test_id = 5
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_register_7(self):
        u"""身份证错误位数：19位"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                        "SERVERID": "%s" % cookie,
                        "SESSION": "%s" % wx_session,
                    }
            test_id = 6
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_register_8(self):
        u"""身份证末尾是X的校验"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                        "SERVERID": "%s" % cookie,
                        "SESSION": "%s" % wx_session,
                    }
            test_id = 7
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_register_9(self):
        u"""身份证英文字母校验"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                        "SERVERID": "%s" % cookie,
                        "SESSION": "%s" % wx_session,
                    }
            test_id = 8
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_register_10(self):
        u"""身份证汉字校验"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                        "SERVERID": "%s" % cookie,
                        "SESSION": "%s" % wx_session,
                    }
            test_id = 9
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_register_11(self):
        u"""身份证特殊字符校验"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                        "SERVERID": "%s" % cookie,
                        "SESSION": "%s" % wx_session,
                    }
            test_id = 10
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_register_12(self):
        u"""手机号10位"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                        "SERVERID": "%s" % cookie,
                        "SESSION": "%s" % wx_session,
                    }
            test_id = 11
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_register_13(self):
        u"""手机号12位"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                        "SERVERID": "%s" % cookie,
                        "SESSION": "%s" % wx_session,
                    }
            test_id = 12
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_register_14(self):
        u"""错误验证码"""
        try:
            member_register.sendSmsCode(self)
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies = loggin_wx()
            cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                        "SERVERID": "%s" % cookie,
                        "SESSION": "%s" % wx_session,
                    }
            test_id = 13
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise
if __name__ == '__main__':
    unittest.main()
