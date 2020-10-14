# -*- coding: utf-8 -*-
"""
Created: on 2018-11-30
@author: Four
Project: Login_App.py
URL: http://safecheck-qa.eslink.net.cn/safecheck/front/app/sendVerCode
Description:登录App获取app_token
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

# # 获取xlsx路径
# path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
# logger_message = Logger()
# send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# Url = "http://cloudcall-pc-qa.eslink.net.cn/services/session/list"\
#


# files = {'clientFile': open("C:\\Users\\Administrator\Desktop\图片\EC6002-MC5.jpg", 'rb')}
# response = requests.post("http://47.93.158.61:16085/file/upload", files=files)
# print(response.text)

response = {"message":"运行正确","responseCode":"100000","result":"http://eslink-operation-test.oss-cn-beijing.aliyuncs.com/EC6002-MC5.jpg"}
print(type(response))
print(response["result"])