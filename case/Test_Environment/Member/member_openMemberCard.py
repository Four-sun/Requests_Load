# -*- coding: utf-8 -*-
"""
Created: on 2018-05-03
@author: Four
Project: case\member_openMemberCard.py
URL: http://patrol-mobile-qa.eslink.net.cn/member/member/openMemberCard
Description:会员管理开通主卡接口
"""

import os
import sys
import time
import unittest
import requests
from common.log import Logger
from common.Excel_readline import ExcelUtil
from common.Request_Package import send_requests
from config.re_token import get_token
from config.Login_comment import write_yaml
from config.Login_comment import new_Loging_etbc

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "test_member_interface.xlsx")
Sheet_Name = "member_openMemberCard"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class member_openMemberCard(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            logging = new_Loging_etbc()
            write_yaml(logging)
            cls.token = get_token()
            logger_message.loginfo("获取到token值：%s" % cls.token)

        def test_openMemberCard_1(self):
            u"""会员管理开通主卡，姓名错误"""
            try:
                data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
                test_id = 0
                s = requests.session()
                res = send_requests(s, data[test_id], cookie=self.token)
                self.assertTrue(res)

            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def test_openMemberCard_2(self):
            u"""会员管理开通主卡，手机号错误"""
            try:
                data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
                test_id = 1
                s = requests.session()
                res = send_requests(s, data[test_id], cookie=self.token)
                self.assertTrue(res)

            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def test_openMemberCard_3(self):
            u"""会员管理开通主卡，身份证错误"""
            try:
                data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
                test_id = 2
                s = requests.session()
                res = send_requests(s, data[test_id], cookie=self.token)
                self.assertTrue(res)

            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def test_openMemberCard_4(self):
            u"""会员管理开通主卡，卡类型错误"""
            try:
                data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
                test_id = 3
                s = requests.session()
                res = send_requests(s, data[test_id], cookie=self.token)
                self.assertTrue(res)

            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def test_openMemberCard_5(self):
            u"""会员管理开通主卡，卡二类型错误"""
            try:
                data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
                test_id = 4
                s = requests.session()
                res = send_requests(s, data[test_id], cookie=self.token)
                self.assertTrue(res)

            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def test_openMemberCard_6(self):
            u"""会员管理开通主卡，卡已存在的情况"""
            try:
                data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
                test_id = 5
                s = requests.session()
                res = send_requests(s, data[test_id], cookie=self.token)
                self.assertTrue(res)

            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

if __name__ == '__main__':
    unittest.main()
