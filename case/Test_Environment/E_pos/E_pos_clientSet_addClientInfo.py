# -*- coding: utf-8 -*-
"""
Created: on 2018-04-25
@author: Four
Project: case\E-pos_clientSet_addClientInfo.py
URL: http://epos-pc-qa.eslink.net.cn/clientSet/addClientInfo
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

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "Epos-eccManager-testcase.xlsx")
Sheet_Name = "clientSet_addClientInfo"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class clientSet_addClientInfo(unittest.TestCase):

    def test_addClientInfo_1(self):
        u"""新增设备版本信息，正确的数据"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    # def test_addClientInfo_2(self):
    #     u"""新增设备版本信息，版本号输入错误字符类型：ABC"""
    #     try:
    #         data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
    #         login_cookies=Login_ecc()
    #         cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
    #         test_id = 1
    #         s = requests.session()
    #         res = send_requests(s, data[test_id], cookie)
    #         self.assertTrue(res)
    #     except Exception as Error:
    #         logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
    #         raise
    #
    # def test_addClientInfo_3(self):
    #     u"""新增设备版本信息，版本号输入浮点型：0.1"""
    #     try:
    #         data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
    #         login_cookies=Login_ecc()
    #         cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
    #         test_id = 2
    #         s = requests.session()
    #         res = send_requests(s, data[test_id], cookie)
    #         self.assertTrue(res)
    #     except Exception as Error:
    #         logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
    #         raise
    #
    # def test_addClientInfo_4(self):
    #     u"""新增设备版本信息，版本号输入字符串类型：01"""
    #     try:
    #         data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
    #         login_cookies=Login_ecc()
    #         cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
    #         test_id = 3
    #         s = requests.session()
    #         res = send_requests(s, data[test_id], cookie)
    #         self.assertTrue(res)
    #     except Exception as Error:
    #         logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
    #         raise
    #
    # def test_addClientInfo_5(self):
    #     u"""新增设备版本信息，版本号少传一位：1.0."""
    #     try:
    #         data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
    #         login_cookies=Login_ecc()
    #         cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
    #         test_id = 4
    #         s = requests.session()
    #         res = send_requests(s, data[test_id], cookie)
    #         self.assertTrue(res)
    #     except Exception as Error:
    #         logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
    #         raise
    #
    # def test_addClientInfo_6(self):
    #     u"""新增设备版本信息，版本号输入最大字符：99999.99999.99999"""
    #     try:
    #         data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
    #         login_cookies=Login_ecc()
    #         cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
    #         test_id = 5
    #         s = requests.session()
    #         res = send_requests(s, data[test_id], cookie)
    #         self.assertTrue(res)
    #     except Exception as Error:
    #         logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
    #         raise
    #
    # def test_addClientInfo_7(self):
    #     u"""新增设备版本信息，设备类型错误"""
    #     try:
    #         data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
    #         login_cookies=Login_ecc()
    #         cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
    #         test_id = 6
    #         s = requests.session()
    #         res = send_requests(s, data[test_id], cookie)
    #         self.assertTrue(res)
    #     except Exception as Error:
    #         logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
    #         raise

if __name__ == '__main__':
    unittest.main()
