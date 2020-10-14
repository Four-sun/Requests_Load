# -*- coding: utf-8 -*-
"""
Created: on 2018-12-24
@author: Four
Project: operation_saveProduct.py
URL:http://operation-pc-qa.eslink.net.cn/etbc/product/saveProduct
Description:云商城-保存商品接口
"""

import sys
import time
import json
import unittest
import requests
import warnings
from common.log import Logger
from common.mysql_db import MySQL
from config.re_token import get_token
from config.Login_comment import write_yaml
from config.Login_comment import new_Loging_etbc
from case.Test_Environment.operation.operation_upload_picture import operation_picture_upload

# 获取xlsx路径
logger_message = Logger()
send_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
Id = 8


class operation_saveProduct(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            warnings.simplefilter("ignore", ResourceWarning)
            logging = new_Loging_etbc()
            write_yaml(logging)
            cls.token = get_token()
            logger_message.loginfo("获取到token值：%s" % cls.token)

        def saveProduct(self, Id):
            u"""保存商品接口"""
            try:
                url = 'http://operation-pc-qa.eslink.net.cn/etbc/product/saveProduct'
                get_product_id = self.query_product_info(Id=Id)
                upload_picture = operation_picture_upload(product_id=get_product_id['product_id'])
                save_data = {
                    'weight': '1',            # 重量
                    'isMarketable': '1',      # 是否上下架
                    'type': '1',              # 类型（1-普通商品  2- 赠品 3-兑换商品）
                    'introduction': upload_picture,             # 详情图片
                    'productBaseImage': [upload_picture[1]],    # 商品底图
                    'productImages': upload_picture[1:3],       # 轮播图片
                    'storeProductCategoryId': '132',            # 店铺商品所属分类id
                    'name': '%s' % get_product_id['product_name'],       # 商品名称
                    'supplierId': '103',  # 供应商
                    'supplierName': '',   # 供应商名称
                    'tag': '2',           # 标签id
                    'caption': '',        # 副标题
                    'categoryArr': ['102', '109'],  # '商品类目id(父级-子集)'
                    'tagName': '测试标签',   # 测试标签
                    'productRate': '13',    # 商品税率
                    'rebateRate': '0',      # 商品返点率
                    'productStatus': '1',   # '商品状态  1-启用，2-停用 '
                    'businessType': '2',    # '运营类型  1-自营，2-直运)'
                    'distributionChannel': ['1', '2', '3'],   # '销售渠道:1-微信商城，2-网页商城，3-门店'
                    'logisticsType': 'TRANSPORT_DIRECT',  # '物流类型EXPRESS_DELIVERY-快递，COME_ON-自提，EXPRESS_DISTRIBUTION-配送
                                                          # TRANSPORT_DIRECT-直运，1，2-快递或者自提'
                    'isBuyLimit': '2',  # '是否限购（1-是；2-否）'
                    'buyLimit': '0',    # '每人限购数量'
                }
                logger_message.loginfo(u"请求时间:%s\t请求地址:%s\t请求参数:%s" % (send_time, url, save_data))
                s = requests.session()
                res = s.request(method='post', url=url, data=save_data)
                logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, res.text))
                result = json.loads(res.text).get('result')
                global productId
                productId = result
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def saveProductParameter(self, Id):
            u"""商品参数"""
            try:
                info = self.query_product_specification(Id=Id)
                url = 'http://operation-pc-qa.eslink.net.cn/etbc/product/saveProductParamet'
                request_session = requests.session()
                for spe_info in info:
                    save_product_paramet = {
                        'key': spe_info[0],
                        'value': spe_info[1],
                        'productId': '%d' % 57,
                    }
                    logger_message.loginfo(u"请求时间:%s\t请求地址:%s\t请求参数:%s" % (send_time, url, save_product_paramet))
                    res = request_session.request(method='post', url=url, data=save_product_paramet)
                    logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, res.text))
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def saveProductSpecification(self, Id):
            u"""商品规格"""
            try:
                info = self.query_product_specification(Id=Id, specification='颜色')
                url = 'http://operation-pc-qa.eslink.net.cn/etbc/product/saveProductSpecification'
                request_session = requests.session()
                for spe_info in info:
                    save_product_specification = {
                        'key': spe_info[0],
                        'value': spe_info[1],
                        'productId': '%d' % productId,
                    }
                    logger_message.loginfo(u"请求时间:%s\t请求地址:%s\t请求参数:%s" % (send_time, url, save_product_specification))
                    res = request_session.request(method='post', url=url, data=save_product_specification)
                    logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, res.text))
                    return res.text
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def querySpecificationList(self):
            u"""查询商品规格"""
            try:
                url = 'http://operation-pc-qa.eslink.net.cn/etbc/product/querySpecificationList'
                request_session = requests.session()
                save_product_specificationList = {
                    'productId': '%d' % productId,
                }
                logger_message.loginfo(u"请求时间:%s\t请求地址:%s\t请求参数:%s" % (send_time, url, save_product_specificationList))
                res = request_session.request(method='post', url=url, data=save_product_specificationList)
                logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, res.text))
                return res.text
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def saveProductSku(self, Id):
            u"""添加商品sku信息"""
            try:
                url = 'http://operation-pc-qa.eslink.net.cn/etbc/product/saveProductSku'
                get_product_id = self.query_product_info(Id=Id)
                get_specification = self.querySpecificationList()
                json_specification = json.loads(get_specification).get('result')[0].get('specificationValue')
                upload_picture = operation_picture_upload(product_id=get_product_id['product_id'], spilt=1)
                request_session = requests.session()
                save_product_sku = {
                    "marketPrice": get_product_id['product_price'],
                    "sellPrice": get_product_id['product_price'],
                    "cost": get_product_id['product_price'],
                    "giftPoint": get_product_id['product_price'],
                    "skuStatus": "1",
                    "inventory": "0",
                    "specificationValue": "%s" % json_specification[0]['value'],
                    "specificationGroup": "%d" % json_specification[0]['id'],
                    "productId": "%d" % productId,
                    "productImage": [upload_picture[0]],
                }
                logger_message.loginfo(u"请求时间:%s\t请求地址:%s\t请求参数:%s" % (send_time, url, save_product_sku))
                res = request_session.request(method='post', url=url, data=save_product_sku)
                logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, res.text))
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def updateProductTemplateId(self):
            u"""添加物流模版"""
            try:
                url = 'http://operation-pc-qa.eslink.net.cn/etbc/product/updateProductTemplateId'
                request_session = requests.session()
                ProductTemplateId= {
                    "productId": "%d" % productId,
                    "deliveryTemplateId": "2",
                    "weight": "1"
                }
                logger_message.loginfo(u"请求时间:%s\t请求地址:%s\t请求参数:%s" % (send_time, url, ProductTemplateId))
                res = request_session.request(method='post', url=url, data=ProductTemplateId)
                logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, res.text))
                return res.text
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def query_product_info(self, Id =None):
            u"""查询商品信息"""
            try:
                database = MySQL()
                query_product_info = 'SELECT name product_name, product_id, price price ' \
                                     'from operation_base_info WHERE id = "%d"' % Id
                result = database.query(query_product_info)
                name = ['product_name', 'product_id', 'product_price']
                kong_list = []
                for info in result[0]:
                    kong_list.append(str(info))
                dict_product = dict(zip(name, kong_list))
                logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, dict_product))
                return dict_product
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def query_product_specification(self, Id=None, specification=None):
            u"""查询商品参数信息"""
            try:
                database = MySQL()
                if specification:
                    query_product_info = 'SELECT s.specification_key, s.specification_value from  operation_base_info o ' \
                                         'LEFT JOIN operation_product_specification s ON o.product_id = s.product_id ' \
                                         'where o.id = "%d" AND specification_key = "%s"' % (Id, specification)
                    result = database.query(query_product_info)
                    kong_list = []
                    for info in result:
                        kong_list.append(list(info))
                    dict_product = kong_list
                    logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, dict_product))
                    return dict_product
                else:
                    query_product_info = 'SELECT s.specification_key, s.specification_value from  operation_base_info o ' \
                                         'LEFT JOIN operation_product_specification s ON o.product_id = s.product_id ' \
                                         'where o.id = "%d"' % Id
                    result = database.query(query_product_info)
                    kong_list = []
                    for info in result:
                        kong_list.append(list(info))
                    dict_product = kong_list
                    logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, dict_product))
                    return dict_product
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def batchUpdateProduct(self, isMarketable):
            u"""商品批量上下架: 1 下架 2 上架 3 作废"""
            try:
                url = 'http://operation-pc-qa.eslink.net.cn/etbc/product/batchUpdateProduct'
                request_session = requests.session()
                update_product = {
                    "productIds": "%d" % productId,
                    "isMarketable": "%d" % isMarketable,
                    "type": "3",
                }
                logger_message.loginfo(u"请求时间:%s\t请求地址:%s\t请求参数:%s" % (send_time, url, update_product))
                res = request_session.request(method='post', url=url, data=update_product)
                logger_message.loginfo(u"返回时间:%s\t返回参数:%s" % (send_time, res.text))
            except Exception as Error:
                logger_message.logwarning(u"%s\t方法名：%s\t异常原因：%s" % (send_time, sys._getframe().f_code.co_name, Error))
                raise

        def test_saveProduct(self):
            self.saveProduct(Id=Id)
            self.saveProductParameter(Id=Id)
            self.saveProductSpecification(Id=Id)
            self.saveProductSku(Id=Id)
            self.updateProductTemplateId()
            self.batchUpdateProduct(isMarketable=2)

        @classmethod
        def tearDownClass(cls):
            logger_message.loginfo("用例运行结束")

if __name__ == '__main__':
    unittest.main()
