"""
============================
Author:小白31
Time:2020/12/6 19:50
E-mail:1359239107@qq.com
============================
"""
import unittest

import requests

from common.handle_conf import conf
from common.handle_excel import HandExcel
from common.handle_log import log
from common.handle_path import DATA_DIR
import os
from common.myddt import data, ddt
from tools.tools import assert_dict_item,username

@ddt
class TestProjects(unittest.TestCase):
    excel = HandExcel(os.path.join(DATA_DIR, "case_data.xlsx"), "projects")
    test_data = excel.read_excel()

    @classmethod
    def setUpClass(cls):
        """登录"""
        # 测试数据
        url = conf.get("env", "base_url") + "/user/login/"
        method = "POST"
        params = {"username": "yunfei001", "password": "123456"}

        # 请求接口
        res = requests.request(method, url, json=params).json()

        # 提取返回的token，设置为类属性
        cls.token = res["token"]

    @data(*test_data)
    def test_projects(self, item):
        # 1. 准备测试数据
        method = item["method"]
        url = conf.get("env", "base_url") + item["url"]
        # 替换name
        if "#name#" in item["data"]:
            item["data"] = item["data"].replace("#name#",username())
        params = eval(item["data"])
        headers = {"Authorization": "JWT" + " " + self.token}
        expected = eval(item["expected"])

        # 2. 请求接口，获取实际结果
        res = requests.request(method, url, json=params, headers=headers).json()

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