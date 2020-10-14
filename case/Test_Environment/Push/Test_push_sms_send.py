# -*- coding: utf-8 -*-
"""
Created: on 2018-04-11
@author: Four
Project: case\send_message.py
URL: http://push-pc-qa.eslink.net.cn/push/sms/send
"""
import unittest
import os
import time
import sys
import requests
from common.Request_Package import send_requests
from common.Excel_readline import ExcelUtil
from common.log import Logger

# 获取demo_api.xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "push_send_message.xlsx")
Sheet_Name = "Sheet1"
logger_message = Logger()
#获取当前时间
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class Test_Push_Sms_Send(unittest.TestCase):

    def Loging_etbc(self):
        u"""发送请求登陆etbc"""
        try:
            payload={
                "loginName": "zhangyang1",
                "loginPwd": "zj03030418"
            }
            logger_message.loginfo(u'%s\t入参%s\t' % (send_time,payload))
            login_etbc = requests.post('http://etbc-qa.eslink.net.cn/user/login', data=payload)
            json_result = login_etbc.json()
            self.assertEqual(200,login_etbc.status_code,msg='失败原因：200 != %s' % (login_etbc.status_code))
            self.assertTrue(json_result["success"],msg='失败原因：%s' % json_result["msg"])
            logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time, sys._getframe().f_code.co_name, login_etbc.url, login_etbc.status_code, login_etbc.text))
            return login_etbc

        except AssertionError as Error:

            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))

    def test_ID_0(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise
        finally:
            time.sleep(30)

    def test_ID_1(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 1
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise

    def test_ID_2(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 2
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise
        finally:
            time.sleep(30)

    def test_ID_3(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 3
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise

    def test_ID_4(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 4
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise
        finally:
            time.sleep(30)

    def test_ID_5(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 5
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise

    def test_ID_6(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 6
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise

    def test_ID_7(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 7
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise

    def test_ID_8(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 8
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise

    def test_ID_9(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 9
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise

    def test_ID_010(self):
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_Push_Sms_Send.Loging_etbc(self)
            c = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 10
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise

if __name__ == "__main__":
    unittest.main()
