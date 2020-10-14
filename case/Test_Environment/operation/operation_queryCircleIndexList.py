# -*- coding: utf-8 -*-
"""
Created: on 2018-12-26
@author: Four
Project: operation_queryCircleIndexList.py
URL:http://operation-pc-qa.eslink.net.cn/etbc/product/queryCircleIndexList
Description:云商城-查询店铺首页轮播图片列表
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

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
xlsx_path = os.path.join(path, "config")
report_xlsx = os.path.join(xlsx_path, "test_operation.xlsx")
Sheet_Name = "operation_queryCircleIndexList"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


def operation_queryCircleIndexList_1(self):
    u"""查询店铺首页轮播图片列表"""
    try:
        data = ExcelUtil(report_xlsx, Sheet_Name).dict_data()
        test_id = 0
        s = requests.session()
        res = send_requests(s, data[test_id], cookie=self.token)
        return res["result"]
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


class operation_queryNewsIndexList(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            logging = new_Loging_etbc()
            write_yaml(logging)
            cls.token = get_token()
            warnings.simplefilter("ignore", ResourceWarning)
            logger_message.loginfo("获取到token值：%s" % cls.token)

        def test_operation_queryAdIndexList(self):
            operation_queryCircleIndexList_1(self)

        @classmethod
        def tearDownClass(cls):
            logger_message.loginfo("用例运行结束")

if __name__ == '__main__':
    unittest.main()
