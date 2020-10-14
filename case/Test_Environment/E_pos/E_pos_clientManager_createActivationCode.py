# -*- coding: utf-8 -*-
"""
Created: on 2018-04-19
@author: Four
Project: case\E-pos_clientManager_createActivationCode.py
URL: http://epos-pc-qa.eslink.net.cn/clientManager/createActivationCode
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
Sheet_Name = "clientManager_createActivation"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class clientManager_createActivationC(unittest.TestCase):

    def test_SearchActionCode_1(self):
        u"""正确的条件,成功创建一个激活码"""
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

    def test_SearchActionCode_2(self):
        u"""创建激活码:没有条件调用接口"""
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

    def test_SearchActionCode_3(self):
        u"""创建激活码:必输项检查：merchantCode"""
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

    def test_SearchActionCode_4(self):
        u"""创建激活码:非必输项检查：ownerShip"""
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

    def test_SearchActionCode_5(self):
        u"""创建激活码:必输项检查：creatNum"""
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

    def test_SearchActionCode_6(self):
        u"""创建激活码:输入项float字段类型校验:merchantCode"""
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

    def test_SearchActionCode_7(self):
        u"""创建激活码:输入项int字段类型校验:creatNum"""
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

    def test_SearchActionCode_8(self):
        u"""创建激活码输入项float字段类型校验:ownerShip"""
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

    def test_SearchActionCode_9(self):
        u"""创建激活码:输入项float字段类型校验:subMerchantCode"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 8
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_SearchActionCode_10(self):
        u"""创建激活码:输入项字段的特定类型校验：merchantCode"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 9
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_SearchActionCode_11(self):
        u"""创建激活码:输入项字段的特定类型校验：subMerchantCode"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 10
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_SearchActionCode_12(self):
        u"""创建激活码:输入项字段的特定类型校验：creatNum"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 11
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_SearchActionCode_13(self):
        u"""创建激活码:输入项字段的特定类型校验：ownerShip"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 12
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_SearchActionCode_14(self):
        u"""创建激活码:creatNum创建个数边界值：0"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 13
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_SearchActionCode_15(self):
        u"""创建激活码:creatNum创建个数边界值：51"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 14
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_SearchActionCode_16(self):
        u"""创建激活码:特殊字符的校验"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            login_cookies=Login_ecc()
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            test_id = 15
            s = requests.session()
            res = send_requests(s, data[test_id], cookie)
            self.assertTrue(res)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

if __name__ == '__main__':
    unittest.main()
