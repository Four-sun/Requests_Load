# -*- coding: utf-8 -*-
"""
Created: on 2018-12-24
@author: Four
Project: operation_saveIndex.py
URL:http://operation-pc-qa.eslink.net.cn/etbc/product/saveIndex
Description:云商城-保存店铺首页公告
"""

import os
import sys
import time
import unittest
import requests
import warnings
from common.log import Logger
from common.Excel_readline import ExcelUtil
from common.Request_PictureFile import send_requests
from config.re_token import get_token
from config.Login_comment import write_yaml
from config.Login_comment import new_Loging_etbc
from case.Test_Environment.operation.operation_file_upload import operation_file_upload_1

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
xlsx_path = os.path.join(path, "config")
report_xlsx = os.path.join(xlsx_path, "test_operation.xlsx")
Sheet_Name = "operation_saveIndex"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


def operation_saveIndex_1(self):
    u"""保存店铺首页公告接口"""
    try:
        data = ExcelUtil(report_xlsx, Sheet_Name).dict_data()
        test_id = 0
        s = requests.session()
        res = send_requests(s, data[test_id], cookie=self.token)
        if str(res["responseCode"]) == '100000':
            logger_message.loginfo("接口返回信息：%s" % res)
        else:
            logger_message.logwarning("接口返回信息：%s" % res)
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


def operation_saveIndex_2(self):
    u"""保存店铺首页广告接口"""
    try:
        operation_file_upload = operation_file_upload_1(self)
        save_index_load = {
            # "image[0]": "%s" % operation_file_upload["result"],
            "adName": "新版商城广告列表",
            "path": "http://www.eslink.cc/",
            "orders": "1",
            "adMemo": "新版商城广告列表",
            "status": "1",
            "type": "4",
            "commont": "%s" % operation_file_upload["result"],
        }
        data = ExcelUtil(report_xlsx, Sheet_Name).dict_data()
        test_id = 1
        s = requests.session()
        res = send_requests(s, data[test_id], send_load=save_index_load, cookie=self.token)
        if str(res["responseCode"]) == '100000':
            logger_message.loginfo("接口返回信息：%s" % res)
        else:
            logger_message.logwarning("接口返回信息：%s" % res)
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


def operation_saveIndex_3(self):
    u"""保存店铺首页轮播图片接口"""
    try:
        operation_file_upload = operation_file_upload_1(self)
        save_index_load = {
            # "image[0]": "%s" % operation_file_upload["result"],
            "adName": "店铺首页轮播图片",
            "path": "http://www.eslink.cc/",
            "orders": "1",
            "adMemo": "店铺首页轮播图片",
            "status": "1",
            "type": "1",
            "commont": "%s" % operation_file_upload["result"],
        }
        data = ExcelUtil(report_xlsx, Sheet_Name).dict_data()
        test_id = 2
        s = requests.session()
        res = send_requests(s, data[test_id], send_load=save_index_load, cookie=self.token)
        if str(res["responseCode"]) == '100000':
            logger_message.loginfo("接口返回信息：%s" % res)
        else:
            logger_message.logwarning("接口返回信息：%s" % res)
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


class operation_saveIndex(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            logging = new_Loging_etbc()
            write_yaml(logging)
            cls.token = get_token()
            warnings.simplefilter("ignore", ResourceWarning)
            logger_message.loginfo("获取到token值：%s" % cls.token)

        def test_operation_saveIndex_1(self):
            operation_saveIndex_3(self)

        @classmethod
        def tearDownClass(cls):
            logger_message.loginfo("用例运行结束")

if __name__ == '__main__':
    unittest.main()