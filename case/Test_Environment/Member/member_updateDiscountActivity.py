# -*- coding: utf-8 -*-
"""
Created: on 2018-06-11
@author: Four
Project: case\member_updateDiscountActivity
URL: http://member-pc-qa.eslink.net.cn/member/updateDiscountActivity
Description:删除优惠活动接口
"""

import os
import sys
import time
import unittest
import requests
from common.log import Logger
from common.mysql_pub import MysqlUtil
from common.Excel_readline import ExcelUtil
from common.Request_Package import send_requests
from config.re_token import get_token
from config.Login_comment import write_yaml
from config.Login_comment import new_Loging_etbc

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "test_member_interface.xlsx")
Sheet_Name = "member_updateDiscountActivity"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class member_updateDiscountActivity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging = new_Loging_etbc()
        write_yaml(logging)
        cls.token = get_token()
        logger_message.loginfo("获取到token值：%s" % cls.token)
        print("获取到token值：%s" % cls.token)

    def member_selectDiscountActivity_id(self):

        A = MysqlUtil()
        sql = "SELECT id from biz_discount_activity WHERE version = '0' GROUP BY activity_start_time DESC  LIMIT 1;"
        A.mysql_execute(sql)
        result = A.mysql_getrows(sql)
        A.mysql_close()
        return result

    def test_member_updateDiscountActivity_1(self):
        u"""删除优惠活动接口"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            discountactivity_id = member_updateDiscountActivity.member_selectDiscountActivity_id(self)
            load_id = {"id": "%s" % discountactivity_id[0][0]}
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], send_load=load_id, cookie=self.token)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

if __name__ == '__main__':
    unittest.main()