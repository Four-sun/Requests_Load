# -*- coding: utf-8 -*-
"""
Created: on 2018-04-11
@author: Four
Project: common\Request_Package.py
Request重新封装
"""

import json
import time
from common.log import Logger

Logger_Message = Logger()
send_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))  #获取当前时间


def send_requests(s, testdata, cookie=None,):
    '''封装requests请求'''
    method = testdata["method"]
    description = testdata["description"]
    url = testdata["url"]
    # url后面的params参数d
    try:
        params = eval(testdata["params"])
    except:
        params = None
    # 请求头部headers
    try:
        headers = eval(testdata["headers"])
    except:
        headers = None
    # post请求body类型
    type = testdata["type"]

    test_nub = testdata['caseid']

    Logger_Message.loginfo("-------------正在执行用例：%s 描述：%s  -------------" % (test_nub,description))
    print("-------------正在执行用例：%s 描述：%s  -------------" % (test_nub,description))
    print("%s\n 请求头部：%s \n 请求方式：%s\n 请求url:%s \n 请求参数：%s" % (send_time,headers,method, url,params))
    Logger_Message.loginfo("%s\n 请求头部：%s \n 请求方式：%s\n 请求url:%s \n 请求参数：%s" % (send_time,headers,method, url,params))

    # post请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}

    # post上传files内容
    try:
        files = eval(testdata["files"])
    except:
        files = {}

    # 判断传data数据还是json
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata

    if method == "post":

        if type == "files":
            print("%s\n post请求body类型为：%s \tfiles内容为：%s" % (send_time, type, files))
            Logger_Message.loginfo("%s\n post请求body类型为：%s \tfiles内容为：%s" % (send_time,type, files))
        else:
            print("%s\n post请求body类型为：%s \tbody内容为：%s" % (send_time, type, body))
            Logger_Message.loginfo("%s\n post请求body类型为：%s \tbody内容为：%s" % (send_time,type, body))

    verify = False  # 是否检验
    res = {}   # 接受返回数据

    try:
        r = s.request(method=method,
                      cookies=cookie,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify)
        print("页面返回信息：%s" % r.content.decode("utf-8"))
        Logger_Message.loginfo("页面返回信息：%s" % r.content.decode("utf-8"))
        res["statuscode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        res["times"] = str(r.elapsed.total_seconds())   # 接口请求时间转str
        if res["statuscode"] != "200":
            res["error"] = res["text"]
            return False
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            res["text"] = r.content.decode("utf-8")
            print("%s \t接口请求时间：%ss \t用例测试结果:%s---->%s " % (send_time,res["times"],test_nub, res["result"]))
            Logger_Message.loginfo("%s \t接口请求时间：%ss \t用例测试结果:%s---->%s " % (send_time,res["times"],test_nub, res["result"]))
            return True
        else:
            res["result"] = "fail"
            print("%s \t 接口请求时间：%ss \t用例测试结果:%s---->%s  %s Not in %s" % (send_time,res["times"],test_nub, res["result"],testdata["checkpoint"],res["text"]))
            Logger_Message.loginfo("%s \t 接口请求时间：%ss \t用例测试结果:%s---->%s  %s Not in %s" % (send_time,res["times"],test_nub, res["result"],testdata["checkpoint"],res["text"]))
            return False

    except Exception as msg:
        res["msg"] = str(msg)
        Logger_Message.logwarning("%s\t%s" % (send_time, msg))
        return res

