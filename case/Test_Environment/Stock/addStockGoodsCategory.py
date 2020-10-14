# -*- coding: utf-8 -*-
"""
Created: on 2018-06-04
@author: Four
Project: case\addStockGoodsCategory.py
URL: http://stock-pc-qa.eslink.net.cn/stockGoodsCategory/addStockGoodsCategory
Description:商品管理添加类别名称
"""
import unittest
import json
import time
import sys
import requests
from common.log import Logger
import random

logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
add_url = "http://stock-pc-qa.eslink.net.cn/stockGoodsCategory/addStockGoodsCategory"


class addStockGoodsCategory(unittest.TestCase):

    def Login_etbc(self):
        u'''发送请求登陆etbc'''
        payload={
            "loginName":"zhangyang1",
            "loginPwd":"zj03030418"
        }
        logger_message.loginfo(u'%s\t入参%s\t'%(send_time,payload))
        login_etbc=requests.post('http://etbc-qa.eslink.net.cn/user/login',data=payload)
        logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" %
                               (send_time,sys._getframe().f_code.co_name,login_etbc.url,login_etbc.status_code,login_etbc.text))
        return login_etbc

    def addStockGoodsCategory_1(self):
        u'''商品管理添加类别名称'''
        try:
            model_test=random.randrange(1, 10000)
            header = {"Connection": "keep-alive",
                      "Content-Length": "65",
                      "Content-Type": "application/json;charset=UTF-8"
                      }
            addStockGoodsCategory_detail={"stockCategory":[{"name":"机械器材%d"%model_test,"parentId":"0","level":1}]}
            add_values = json.dumps(addStockGoodsCategory_detail)
            login_cookies = addStockGoodsCategory.Login_etbc(self)
            print(login_cookies)
            cookie=requests.utils.dict_from_cookiejar(login_cookies.cookies)
            print(cookie)
            res = requests.post(url=add_url, data=add_values, cookies=cookie, headers=header)
            print(res.text)
        except Exception as Error:
            logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
            raise

    def test_addGood(self):

        for i in range(1):

            self.addStockGoodsCategory_1()

if __name__ == '__main__':
    unittest.main()
