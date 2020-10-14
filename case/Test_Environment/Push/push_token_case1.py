# -*- coding: utf-8 -*-
"""
Created: on 2018-05-31
@author: Four
Project: case\member_businessHallCardRecharge.py
URL:http://member-pc-qa.eslink.net.cn/member/queryMemberCard
Description:会员卡充值接口
"""
import unittest
import time
import sys
import requests
from common.log import Logger
from config.re_token import get_token

logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class Pushcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = get_token()
        print("获取到token值：%s"%cls.token)

    def test_01(self):

        '''测试用例1'''
        push_body = {
            'templateCode': 'SMS_25115012',
            'customer': '张阳',
            'recNum': '18858271978',
            'paramString': '{"customer":"张阳"}'
        }
        logger_message.loginfo(u'%s\t入参%s\t'%(send_time,push_body))
        login_etbc=requests.post('http://push-pc-qa.eslink.net.cn/push/sms/send', data=push_body,cookies=self.token)
        # logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,login_etbc.url,login_etbc.status_code,login_etbc.text))
        print(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,login_etbc.url,login_etbc.status_code,login_etbc.text))

    def test_02(self):

        '''测试用例1'''
        push_body = {
            'templateCode': 'SMS_25115012',
            'customer': '张阳1',
            'recNum': '18858271978',
            'paramString': '{"customer":"张阳1"}'
        }
        logger_message.loginfo(u'%s\t入参%s\t'%(send_time,push_body))
        login_etbc=requests.post('http://push-pc-qa.eslink.net.cn/push/sms/send', data=push_body,cookies=self.token)
        # logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,login_etbc.url,login_etbc.status_code,login_etbc.text))
        print(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,login_etbc.url,login_etbc.status_code,login_etbc.text))

if __name__ == '__main__':
    unittest.main()















