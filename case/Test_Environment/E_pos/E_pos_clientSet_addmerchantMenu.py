# -*- coding: utf-8 -*-
"""
Created: on 2018-04-27
@author: Four
Project: case\E-pos_clientSet_addmerchantMenu.py
URL: http://epos-pc-qa.eslink.net.cn/clientSet/addmerchantMenu
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
Sheet_Name = "clientSet_addmerchantMenu"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class clientSet_addmerchantMenu(unittest.TestCase):

    def test_addmerchantMenu_1(self):
        u"""新增商户菜单配置，商户菜单重复的情况"""
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

    def test_addmerchantMenu_2(self):
        u"""商户菜单配置必选项缺少：merchantCode"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 1
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_addmerchantMenu_3(self):
        u"""商户菜单配置必选项缺少：type"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 2
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_addmerchantMenu_4(self):
        u"""商户菜单配置必选项缺少：menu"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 3
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_addmerchantMenu_5(self):
        u"""商户菜单配置必选项缺少：voucherConfig"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 4
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_addmerchantMenu_6(self):
        u"""商户菜单配置必选项缺少：codePrintType"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 5
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_addmerchantMenu_7(self):
        u"""商户编码最大字符数：4"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 6
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_addmerchantMenu_8(self):
        u"""子商户编码最大字符数：10"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 7
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

if __name__ == '__main__':
    unittest.main()