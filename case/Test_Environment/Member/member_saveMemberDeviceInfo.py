# -*- coding: utf-8 -*-
"""
Created: on 2018-06-11
@author: Four
Project: case\member_saveMemberDeviceInfo
URL: http://member-pc-qa.eslink.net.cn/member/saveMemberDeviceInfo
Description:新增会员设备信息接口
"""
import os
import sys
import time
import unittest
import requests
from common.log import Logger
from common.Excel_readline import ExcelUtil
from common.Request_Package import send_requests
from config.re_token import get_token
from config.Login_comment import write_yaml
from config.Login_comment import new_Loging_etbc

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "test_member_interface.xlsx")
Sheet_Name = "member_saveMemberDeviceInfo"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class member_saveMemberDeviceInfo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging = new_Loging_etbc()
        write_yaml(logging)
        cls.token = get_token()
        logger_message.loginfo("获取到token值：%s" % cls.token)
        print("获取到token值：%s" % cls.token)

    def member_saveMemberDeviceInfo_id(self):
        """删除新绑定的设备信息"""
        A = MysqlUtil()
        sql = "DELETE FROM biz_member_device_info " \
              "WHERE device_no = 'fffffffff7f0f5d65375dfac0033c589' AND user_id = '1490';"
        A.mysql_execute(sql)
        result=A.mysql_getrows(sql)
        A.mysql_close()
        return result

    def test_member_updateDiscountActivity_1(self):
        u"""新增会员设备信息接口"""
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
            Delect_memberdevice = member_saveMemberDeviceInfo.member_saveMemberDeviceInfo_id(self)
            logger_message.loginfo(u"%s\t方法名：%s\t执行结果：%s" % (send_time, sys._getframe().f_code.co_name, Delect_memberdevice))

    def test_member_updateDiscountActivity_2(self):
        u"""会员设备信息接口,当用户重复绑定设备的情况"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 1
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_member_updateDiscountActivity_3(self):
        u"""会员设备信息接口,当用户重复绑定设备的情况"""
        try:
            data = ExcelUtil(reportxlsx, Sheet_Name).dict_data()
            test_id = 2
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=self.token)
            self.assertTrue(res)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

if __name__ == '__main__':
    unittest.main()