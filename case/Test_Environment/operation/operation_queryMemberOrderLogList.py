# -*- coding: utf-8 -*-
"""
Created: on 2018-12-24
@author: Four
Project: operation_queryMemberOrderLogList.py
URL:http://operation-pc-qa.eslink.net.cn/etbc/order/log/queryMemberOrderLogList
Description:云商城-查询订单日志
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
from case.Test_Environment.operation.operation_queryMemberOrderList import operation_queryMemberOrderList_1

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
xlsx_path = os.path.join(path, "config")
report_xlsx = os.path.join(xlsx_path, "test_operation.xlsx")
Sheet_Name = "queryMemberOrderLogList"
logger_message = Logger()


def operation_queryMemberOrderLogList_1(self):
    u"""查询订单日志"""
    try:
        operation_queryMemberOrderList = operation_queryMemberOrderList_1(self)         #查询交易列表
        get_queryMemberOrderLogList = operation_queryMemberOrderList["list"][-1]["orderCode"]      #选择最后一条记录
        queryMemberOrderLogList_data = {
            "orderCode": "%s" % get_queryMemberOrderLogList,
            "pageSize": "10",
            "pageNum": "1",
        }
        data = ExcelUtil(report_xlsx, Sheet_Name).dict_data()
        test_id = 0
        s = requests.session()
        res = send_requests(s, data[test_id], send_load=queryMemberOrderLogList_data, cookie=self.token)
        return res["result"]
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


class operation_queryMemberOrderLogList(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            logging = new_Loging_etbc()
            write_yaml(logging)
            cls.token = get_token()
            warnings.simplefilter("ignore", ResourceWarning)
            logger_message.loginfo("获取到token值：%s" % cls.token)

        def test_operation_queryMemberOrderLogList(self):
            operation_queryMemberOrderLogList_1(self)

        @classmethod
        def tearDownClass(cls):
            logger_message.loginfo("用例运行结束")

if __name__ == '__main__':
    unittest.main()
