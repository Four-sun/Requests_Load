# -*- coding: utf-8 -*-
"""
Created: on 2018-09-06
@author: Four
Project: services_session_list.py
URL: http://cloudcall-pc-qa.eslink.net.cn/services/session/list
Description:云呼叫-会话历史
"""

import os
import sys
import time
import json
import unittest
import requests
from common.log import Logger
from config.re_token import get_token
from config.Login_comment import write_yaml
from config.Login_comment import new_Loging_etbc

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
Url = "http://cloudcall-pc-qa.eslink.net.cn/services/session/list"

class cloud_call_services_session_list(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            logging = new_Loging_etbc()
            write_yaml(logging)
            cls.token = get_token()
            logger_message.loginfo("获取到token值：%s" % cls.token)

        def test_services_session_list(self):
            try:
                pay_load = {
                    "nickname": "一",
                    "ps": "20",
                    "p": "1",
                    "config": "end"
                    }
                logger_message.loginfo(u'%s\t入参%s\t'%(send_time,pay_load))
                services_session_list = requests.post(url=Url,cookies=self.token, data=pay_load)
                logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,services_session_list.url,services_session_list.status_code,services_session_list.text))
                print(json.loads(services_session_list.text))
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s"%(send_time,sys._getframe().f_code.co_name,Error))

if __name__ == '__main__':
    unittest.main()