# -*- coding: utf-8 -*-
"""
Created: on 2018-06-07
@author: Four
Project: case\member_queryCardDeal
URL: http://member-pc-qa.eslink.net.cn/member/queryCardDeal
Description:消费流水查询接口
"""
import unittest
import os
import time
import sys
import requests
from common.Request_Package import send_requests
from common.Excel_readline import ExcelUtil
from common.log import Logger
from config.re_token import get_token
from config.Login_comment import new_Loging_etbc
from config.Login_comment import write_yaml

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "test_member_interface.xlsx")
Sheet_Name = "member_queryCardDeal"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class member_queryCardDeal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging = new_Loging_etbc()
        write_yaml(logging)
        cls.token = get_token()
        logger_message.loginfo("获取到token值：%s" % cls.token)
        print("获取到token值：%s" % cls.token)

    def test_member_queryCardDeal_1(self):
        u"""消费流水查询接口"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryCardDeal_2(self):
        u"""充值成功记录查询接口,会员ID错误条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 1
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryCardDeal_3(self):
        u"""充值成功记录查询接口,会员卡号多一位错误条件"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 2
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryCardDeal_4(self):
        u"""充值成功记录查询接口,缺少会员ID"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 3
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_queryCardDeal_5(self):
        u"""充值成功记录查询接口,缺少会员卡号"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 4
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise


if __name__ == "__main__":
    unittest.main()

