# -*- coding: utf-8 -*-
"""
Created: on 2018-06-12
@author: Four
Project: case\member_updateMemberDeviceInfo
URL: http://member-pc-qa.eslink.net.cn/member/updateMemberDeviceInfo
Description:修改会员设备信息接口,设备信息修改正确
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
Sheet_Name = "member_updateMemberDeviceInfo"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class member_updateMemberDeviceInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging = new_Loging_etbc()
        write_yaml(logging)
        cls.token = get_token()
        logger_message.loginfo("获取到token值：%s" % cls.token)
        print("获取到token值：%s" % cls.token)

    def member_updateMemberDeviceInfo_id(self):
        u"""查询修改绑定的设备信息"""
        A = MysqlUtil()
        sql = "SELECT user_id FROM biz_member_device_info WHERE id = '61';"
        A.mysql_execute(sql)
        result=A.mysql_getrows(sql)
        A.mysql_close()
        return result

    def test_member_updateMemberDeviceInfo_1(self):
        u"""修改会员设备信息接口,设备信息修改正确"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise
        finally:
            user_id = member_updateMemberDeviceInfo.member_updateMemberDeviceInfo_id(self)
            self.assertEqual(1332, user_id[0][0], msg="修改会员设备信息不匹配")

    def test_member_updateMemberDeviceInfo_2(self):
        u"""修改会员设备信息接口,设备信息修改用户已经绑定设备"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 1
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

if __name__ == '__main__':
    unittest.main()
