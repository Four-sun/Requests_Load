# coding:utf-8
"""
Created: on 2018-07-11
@author: Four
Project: config\re_token.py
Description:token值读取
"""
import yaml
import os

current_path = os.path.dirname(os.path.realpath(__file__))


def get_token(yamlName = "token.yaml"):
    """
    从token.yaml读取token值
    :param yamlName: 配置文件名称
    :return: token值
    """
    path = os.path.join(current_path, yamlName)
    file = open(path)
    text_read = file.read()
    t = yaml.load(text_read)
    file.close()
    return t

if __name__ == "__main__":
    print(get_token())
