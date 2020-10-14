# -*- coding: utf-8 -*-
"""
Created on 2018-03-01
@author: Four
Project: case\invoice_getPaymentRecordList.py
"""
import requests
import unittest
import time,sys
from common.log import Logger
from common.Excel_readline import ExcelUtil

logger_message=Logger()
send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间


class invoice_getPaymentRecordList(unittest.TestCase):

    def getpayment(self):
        u"""获取未开票交易的用户号"""
        for i in range(2):
            filepath = "D:\\pycharm-5.0.4\\Report_test\\Four_jiekou\\config\\mobiles.xlsx"
            sheetName = "Sheet1"
            data = ExcelUtil(filepath, sheetName)
            cute_data=data.dict_data()
            # payload={
            #     "userNo":cute_data[1],
            #     "ownership":'0140',
            # }
            # logger_message.loginfo(u'%s\t入参%s\t'%(send_time,payload))
            get_paymentRecordList=requests.post("http://app.eslink.cc/invoice-zyzt/invoice/bzzy/getPaymentRecordList?userNo=0%s&ownership=0140"%cute_data[i])
            logger_message.loginfo(u"%s\t方法名：%s\t请求地址：%s\t请求状态：%s\t返回内容：%s" % (send_time,sys._getframe().f_code.co_name,get_paymentRecordList.url,get_paymentRecordList.status_code,get_paymentRecordList.text))
            json_result=get_paymentRecordList.json()
            # print(json_result["responseCode"])
            if json_result["result"] != {} and  json_result["responseCode"]=="100000":
                print(cute_data[i])

    def test_case(self):
        self.getpayment()

if __name__ == "__main__":
    unittest.main()