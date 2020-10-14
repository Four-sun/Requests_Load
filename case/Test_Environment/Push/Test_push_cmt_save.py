# -*- coding: utf-8 -*-
"""
Created on 2018-03-01
@author: Four
Project: case\Test_push_cmt_save.py
"""
import requests
import unittest
import time,sys
from common.log import Logger


logger_message=Logger()
send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间


class push_channel_template(unittest.TestCase):

    def Login_etbc(self):
        u"""发送请求登陆etbc"""
        payload={
            "loginName":"zhangyang1",
            "loginPwd":"zj03030418"
        }
        logger_message.loginfo(u'%s\t入参%s\t'%(send_time,payload))
        login_etbc=requests.post('http://etbc-qa.eslink.net.cn/user/login',data=payload)
        logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,login_etbc.url,login_etbc.status_code,login_etbc.text))
        return login_etbc

    def push_add_template(self):
        u"""新增渠道模版"""
        template_payload={
            'code':'1314520',
            'escapeContent':'转义模版',
            'signature':'易联云',
            'name':'测试模版',
            'state':'1',
            'content':'测试模版',
            'channelId':'9'
        }

        login_cookies=push_channel_template.Login_etbc(self)
        print(login_cookies)
        c=requests.utils.dict_from_cookiejar(login_cookies.cookies)
        logger_message.loginfo(u'%s\t入参%s\t'%(send_time,template_payload))
        send_message=requests.post('http://push-pc-qa.eslink.net.cn/cmt/save',data=template_payload,cookies=c)
        print(send_message.raw)
        print(send_message.content)
        logger_message.loginfo(u'%s\t出参%s\t请求地址：%s\t发送状态：%s\t返回内容：%s'%(send_time,sys._getframe().f_code.co_name,send_message.url,send_message.status_code,send_message.text))
        return login_cookies

    def test_case(self):
        self.Login_etbc()
        self.push_add_template()

if __name__ == "__main__":
    unittest.main()