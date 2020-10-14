# -*- coding: utf-8 -*-
"""
Created: on 2018-04-19
@author: Four
Project: case\E-pos_clientManager_createActivationCode.py
URL: http://epos-pc-qa.eslink.net.cn/clientSet/searchActionCode
"""
import unittest
import os
import time
import sys
import requests
from case.Test_Environment.E_pos.Login_ecc import Login_ecc
from common.Request_Package import send_requests
from common.Excel_readline import ExcelUtil
from common.log import Logger

# 获取demo_api.xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "Epos-eccManager-testcase.xlsx")
logger_message = Logger()
#获取当前时间
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
Sheet_Name = "clientSet_searchActionCode"


class clientSet_searchActionCode(unittest.TestCase):

    def test_SearchActionCode_1(self):
        u"""激活码列表查询，正确输入数据后查询"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            c=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_SearchActionCode_2(self):
        u"""激活码列表查询，错误查询条件:status=0"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            c=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 1
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_SearchActionCode_3(self):
        u"""缺少一个查询参数：status"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            c=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 2
            s = requests.session()
            res = send_requests(s, data[test_id], c)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

if __name__ == "__main__":
    unittest.main()
