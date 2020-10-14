# -*- coding: utf-8 -*-
"""
Created: on 2019-05-31
@author: Four
Project: operation_upload_picture.py
URL: http://operation-pc-qa.eslink.net.cn/file/upload
Description: 云商城-上传图片
"""
import os
import sys
import time
import json
import requests
from common.log import Logger

logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

file_dir = 'D:\pycharm-5.0.4\spitle_photo\mzitu'


def get_picture(file_dir, product_id, spilt=None):
    try:
        path = os.listdir(file_dir)
        upload_picture = []
        for picture in path:
            if product_id is None:
                print('product is None!')
                break
            elif product_id in picture:
                upload_picture.append(picture)
        if spilt is None:
            return upload_picture
        else:
            return upload_picture[:1]
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise


def operation_picture_upload(product_id, spilt=None):
    u"""上传图片接口"""
    try:
        url = 'http://operation-pc-qa.eslink.net.cn/file/upload'
        get_picture_list = get_picture(file_dir, product_id, spilt)
        upload_url = []
        for file in range(len(get_picture_list)):
            files = {"clientFile": open("%s\\%s" % (file_dir, get_picture_list[file]), "rb")}
            res = requests.post(url=url, files=files)
            user_dict = json.loads(res.text)
            upload_url.append(user_dict['result'])
        return upload_url
    except Exception as Error:
        logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
        raise

# if __name__ == '__main__':
#     product_id = '100385824'
    # get_picture(file_dir, product_id=product_id,)
    # operation_picture_upload(product_id,)
