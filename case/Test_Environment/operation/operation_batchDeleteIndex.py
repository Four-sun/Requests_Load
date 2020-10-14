# -*- coding: utf-8 -*-
"""
Created: on 2018-12-24
@author: Four
Project: operation_batchDeleteIndex.py
URL:http://operation-pc-qa.eslink.net.cn/etbc/product/batchDeleteIndex
Description:云商城-删除店铺首页公告列表记录
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
from case.Test_Environment.operation.operation_queryAdIndexList import operation_queryAdIndexList_1
from case.Test_Environment.operation.operation_queryNewsIndexList import operation_queryNewsIndexList_1
from case.Test_Environment.operation.operation_queryCircleIndexList import operation_queryCircleIndexList_1
from case.Test_Environment.operation.operation_saveIndex import operation_saveIndex_1, operation_saveIndex_2, operation_saveIndex_3

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
xlsx_path = os.path.join(path, "config")
report_xlsx = os.path.join(xlsx_path, "test_operation.xlsx")
Sheet_Name = "operation_batchDeleteIndex"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


def operation_batchDeleteIndex_1(self):
    u"""删除店铺首页公告列表记录接口"""
    try:
        operation_saveIndex_1(self)     # 先新增店铺首页公告
        queryAdIndexList = operation_queryAdIndexList_1(self)       # 执行查询店铺首页最后一条公告的id
        get_queryAdIndexList = queryAdIndexList[-1]["id"]
        queryAdIndex = {"ids": "%s" % get_queryAdIndexList}
        data = ExcelUtil(report_xlsx, Sheet_Name).dict_data()
        test_id = 0
        s = requests.session()
        res = send_requests(s, data[test_id], send_load=queryAdIndex, cookie=self.token)
        if str(res["responseCode"]) == '100000':
            logger_message.loginfo("接口返回信息：%s" % res)
        else:
            logger_message.logwarning("接口返回信息：%s" % res)

    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


def operation_batchDeleteIndex_2(self):
    u"""删除店铺首页广告列表记录接口"""
    try:
        operation_saveIndex_2(self)     # 先新增店铺首页广告
        queryNewsIndexList = operation_queryNewsIndexList_1(self)       # 执行查询店铺首页最后一条广告的id
        get_queryNewsIndexList = queryNewsIndexList[-1]["id"]
        queryAdIndex = {"ids": "%s" % get_queryNewsIndexList}
        data = ExcelUtil(report_xlsx, Sheet_Name).dict_data()
        test_id = 0
        s = requests.session()
        res = send_requests(s, data[test_id], send_load=queryAdIndex, cookie=self.token)
        if str(res["responseCode"]) == '100000':
            logger_message.loginfo("接口返回信息：%s" % res)
        else:
            logger_message.logwarning("接口返回信息：%s" % res)
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise

def operation_batchDeleteIndex_3(self):
    u"""删除店铺首页轮播图片接口"""
    try:
        operation_saveIndex_3(self)     # 先新增店铺首页轮播图片
        queryCircleIndexList = operation_queryCircleIndexList_1(self)       # 执行查询店铺首页最后一条轮播图片的id
        get_queryCircleIndexList = queryCircleIndexList[-1]["id"]
        queryAdIndex = {"ids": "%s" % get_queryCircleIndexList}
        data = ExcelUtil(report_xlsx, Sheet_Name).dict_data()
        test_id = 0
        s = requests.session()
        res = send_requests(s, data[test_id], send_load=queryAdIndex, cookie=self.token)
        if str(res["responseCode"]) == '100000':
            logger_message.loginfo("接口返回信息：%s" % res)
        else:
            logger_message.logwarning("接口返回信息：%s" % res)
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise

class operation_batchDeleteIndex(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            logging = new_Loging_etbc()
            write_yaml(logging)
            cls.token = get_token()
            warnings.simplefilter("ignore", ResourceWarning)
            logger_message.loginfo("获取到token值：%s" % cls.token)

        def test_operation_batchDeleteIndex(self):
            operation_batchDeleteIndex_3(self)

        @classmethod
        def tearDownClass(cls):
            logger_message.loginfo("用例运行结束")

if __name__ == '__main__':
    unittest.main()
