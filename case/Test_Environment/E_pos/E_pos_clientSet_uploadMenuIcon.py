# -*- coding: utf-8 -*-
"""
Created: on 2018-04-20
@author: Four
Project: case\E-pos_clientSet_uploadMenuIcon.py
URL: http://epos-pc-qa.eslink.net.cn/clientSet/uploadMenuIcon
"""
import unittest
import os
import time
import sys
import requests
import json
from case.Test_Environment.E_pos import Login_ecc
from common.Request_PictureFile import send_requests
from common.Excel_readline import ExcelUtil
from common.log import Logger

# 获取demo_api.xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "Epos-eccManager-testcase.xlsx")
logger_message = Logger()
#获取当前时间
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
Sheet_Name = "clientSet_uploadMenuIcon"
Sheet_Name1 = "clientSet_updateMenu"


class clientSet_uploadMenuIcon(unittest.TestCase):

    def uploadMenuIcon(self):
        u"""上传图片"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            test_id = 0
            s = requests.session()
            res = send_requests(s,data[test_id])
            return res
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def delMenuPic(self):
        u"""删除上传的照片"""
        try:
            uploadMenuIcon = clientSet_uploadMenuIcon.uploadMenuIcon(self)
            dict_result = json.loads(uploadMenuIcon)
            case = dict_result["result"]
            send_load = {"fileNames": [case["menuPicName"]],
                         "ids": [case["id"]],
                         "doType": 0}
            print(u'%s\t入参%s\t'% (send_time,send_load))
            logger_message.loginfo(u'%s\t入参%s\t'% (send_time,send_load))
            delMenuPic = requests.post("http://epos-pc-qa.eslink.net.cn/clientSet/delMenuPic", json=send_load)
            print(delMenuPic.status_code,delMenuPic.text)

        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))

    def test_uploadMenuIcon_3(self):
        u"""上传图片:jpg格式"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            test_id = 1
            s = requests.session()
            res = send_requests(s,data[test_id])
            return res
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_updateMenu_1(self):
        u"""添加菜单"""
        try:
            #登陆Ecc获取登陆
            logging_cookie = Login_ecc.Login_ecc()
            cookies = requests.utils.dict_from_cookiejar(logging_cookie.cookies)
            #上传图片得到图片id
            uploadMenuIcon = clientSet_uploadMenuIcon.uploadMenuIcon(self)
            dict_result = json.loads(uploadMenuIcon)
            case = dict_result["result"]
            send_load = {"posMenuName": "菜单名称",
                         "id": case["id"],
                         "posMenuRemark": "测试"}
            #发送请求
            data = ExcelUtil(reportxlsx, Sheet_Name1).dict_data()
            test_id = 0
            s = requests.session()
            res = send_requests(s, data[test_id], send_load, cookies,)
            self.assertTrue(res)
            return res
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time, Error))
            raise

    def test_updateMenu_2(self):
        u"""新增菜单，缺少参数posMenuName"""
        try:
            #登陆Ecc获取登陆
            logging_cookie = Login_ecc.Login_ecc()
            cookies = requests.utils.dict_from_cookiejar(logging_cookie.cookies)
            #上传图片得到图片id
            uploadMenuIcon = clientSet_uploadMenuIcon.uploadMenuIcon(self)
            dict_result = json.loads(uploadMenuIcon)
            case = dict_result["result"]
            send_load = {"posMenuName": "",
                         "id": case["id"],
                         "posMenuRemark": "测试"}
            #发送请求
            data = ExcelUtil(reportxlsx, Sheet_Name1).dict_data()
            test_id = 1
            s = requests.session()
            res = send_requests(s, data[test_id], send_load, cookies,)
            self.assertTrue(res)
            #删除照片
            delMenuPic_load = {"fileNames": [case["menuPicName"]],
                               "ids": [case["id"]],
                               "doType": 0}
            logger_message.loginfo(u'%s\t入参%s\t' % (send_time,delMenuPic_load))
            delMenuPic = requests.post("http://epos-pc-qa.eslink.net.cn/clientSet/delMenuPic", json=delMenuPic_load)
            self.assertTrue(delMenuPic)
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time, Error))
            raise

    def test_updateMenu_3(self):
        u"""添加菜单缺少参数id"""
        try:
            #登陆Ecc获取登陆
            logging_cookie = Login_ecc.Login_ecc()
            cookies=requests.utils.dict_from_cookiejar(logging_cookie.cookies)
            #发送请求
            data = ExcelUtil(reportxlsx, Sheet_Name1).dict_data()
            test_id = 2
            s = requests.session()
            res = send_requests(s, data[test_id], cookie=cookies,)
            self.assertTrue(res)
            return res
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

    def test_updateMenu_4(self):
        u"""参数最大字符数验证posMenuName:10"""
        try:
            #登陆Ecc获取登陆
            logging_cookie = Login_ecc.Login_ecc()
            cookies=requests.utils.dict_from_cookiejar(logging_cookie.cookies)
            #上传图片得到图片id
            uploadMenuIcon= clientSet_uploadMenuIcon.uploadMenuIcon(self)
            dict_result = json.loads(uploadMenuIcon)
            case = dict_result["result"]
            send_load = {"posMenuName": "菜单名称最大字符数限制",
                         "id": case["id"],
                         "posMenuRemark": "测试"}
            #发送请求
            data = ExcelUtil(reportxlsx, Sheet_Name1).dict_data()
            test_id = 3
            s = requests.session()
            res = send_requests(s, data[test_id], send_load,cookies,)
            self.assertTrue(res)
            #删除照片
            delMenuPic_load = {"fileNames": [case["menuPicName"]],
                               "ids": [case["id"]],
                               "doType": 0}
            logger_message.loginfo(u'%s\t入参%s\t' % (send_time,delMenuPic_load))
            delMenuPic = requests.post("http://epos-pc-qa.eslink.net.cn/clientSet/delMenuPic", json=delMenuPic_load)
            self.assertTrue(delMenuPic)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))
            raise

if __name__ == '__main__':
    unittest.main()
