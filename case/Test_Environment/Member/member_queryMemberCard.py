# -*- coding: utf-8 -*-
"""
Created: on 2018-06-07
@author: Four
Project: case\member_queryMemberCard
URL: http://member-pc-qa.eslink.net.cn/member/queryMemberCard
Description:会员卡信息查询接口
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
Sheet_Name = "member_queryMemberCard"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class member_queryMemberCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging = new_Loging_etbc()
        write_yaml(logging)
        cls.token = get_token()
        logger_message.loginfo("获取到token值：%s" % cls.token)
        print("获取到token值：%s" % cls.token)

    def test_member_queryMemberCard_1(self):
        u"""会员卡信息查询接口"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_2(self):
        u"""会员卡信息查询接口姓名查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 1
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_3(self):
        u"""会员卡信息查询接口昵称查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 2
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_4(self):
        u"""会员卡信息查询接口手机号查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 3
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_5(self):
        u"""会员卡信息查询接口身份证查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 4
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_6(self):
        u"""会员卡信息查询接口注册会员开始时间查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 5
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_7(self):
        u"""会员卡信息查询接口注册会员结束时间查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 6
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_8(self):
        u"""会员卡信息查询接口开卡开始时间查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 7
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_9(self):
        u"""会员卡信息查询接口开卡结束时间查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 8
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_10(self):
        u"""会员卡信息查询接口会员Id查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 9
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryMemberCard_11(self):
        u"""会员卡信息查询接口卡号查询条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 10
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

if __name__ == '__main__':
    unittest.main()
