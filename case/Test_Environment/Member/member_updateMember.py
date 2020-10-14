# -*- coding: utf-8 -*-
"""
Created: on 2018-05-02
@author: Four
Project: case\member_updateMember.py
URL: http://patrol-mobile-qa.eslink.net.cn/member/member/updateMenber
Description:会员信息上传图片
"""
import unittest
import os
import time
import requests
from common.Request_Package import send_requests
from common.Excel_readline import ExcelUtil
from common.log import Logger

# 获取xlsx路径
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
testxlsx = os.path.join(path, "config")
reportxlsx = os.path.join(testxlsx, "test_member_interface.xlsx")
Sheet_Name = "member_updateMember"
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))


class member_updateMember(unittest.TestCase):

    def test_updateMember_1(self):

        u"""上传图片"""
        try:
            data = ExcelUtil(reportxlsx,Sheet_Name).dict_data()
            # login_cookies = member_updateMember.logging_wx(self)
            # cookie = requests.utils.dict_from_cookiejar(login_cookies.cookies)
            cookies = {
                "SERVERID": "0134fdb44fbd67e7f77378a1b20ddd4e|1525331625|1525330551",
                "SESSION": "a476febd-f88d-4a94-ae6e-2d6d3631c63a",
                "acw_tc": "AQAAAO+vXWy6awsAiV8RcK9IYhuUdZan",
            }
            test_id = 0
            s = requests.session()
            res = send_requests(s,data[test_id],cookie=cookies)
            return res
        except Exception as Error:
            logger_message.logwarning('%s\t%s\t' % (send_time,Error))
            raise

if __name__ == '__main__':
    unittest.main()