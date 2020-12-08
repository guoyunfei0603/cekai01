"""
============================
Author:小白31
Time:2020/12/5 22:20
E-mail:1359239107@qq.com
============================
"""
import unittest
import os

import requests

from common.handle_conf import conf
from common.handle_log import log
from tools.tools import assert_dict_item
from common.handle_excel import HandExcel
from common.handle_path import DATA_DIR
from common.myddt import data,ddt


@ddt
class TestLogin(unittest.TestCase):
    excel = HandExcel(os.path.join(DATA_DIR, "case_data.xlsx"), "login")
    test_data = excel.read_excel()

    @data(*test_data)
    def test_login(self,item):
        # 1. 准备测试数据
        url = conf.get("env","base_url") + item["url"]
        method = item["method"]
        params = eval(item["data"])
        expected = eval(item["expected"])

        # 2. 请求接口，获取实际结果
        res = requests.request(method,url,json = params).json()

        print("-------当前执行的用例是:{}----------".format(item["title"]))
        print("请求参数：", params)
        print("预期结果：", expected)
        print("实际结果：", res)
        print("===============执行结束===============\n")

        # 3. 断言

        try:
            assert_dict_item(expected, res)
        except AssertionError as e:
            log.exception(e)
            log.error("--测试用例：{}--执行失败".format(item["title"]))
            raise e
        else:
            log.info("--测试用例：{}--执行通过".format(item["title"]))

if __name__ == '__main__':
    unittest.main()