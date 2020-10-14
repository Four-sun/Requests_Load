# -*- coding: utf-8 -*-
"""
Created: on 2018-04-15
@author: Four
Project: case\Test_push_wechat_template.py
URL: http://push-pc-qa.eslink.net.cn/push/wechat/send
Description:微信模版推送
"""
import unittest
import os
import time
import sys
import requests
from common.Request_Package import send_requests
from common.Excel_readline import ExcelUtil
from common.log import Logger

testxlsx = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))), "config")
reportxlsx = os.path.join(testxlsx, "push_wechat_template.xlsx")
Sheet_Name = "wechat_template"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class Test_push_wechat_template(unittest.TestCase):

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

    def test_Push_wechat_template(self):
        u"""微信模版推送"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Test_push_wechat_template.Loging_etbc(self)
            c=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise


if __name__ == "__main__":
    unittest.main()
