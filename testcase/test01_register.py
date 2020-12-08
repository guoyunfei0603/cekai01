"""
============================
Author:小白31
Time:2020/12/1 23:02
E-mail:1359239107@qq.com
============================
"""
import os
import unittest
import requests
from common.handle_conf import conf
from common.handle_excel import HandExcel
from common.handle_log import log
from common.handle_path import DATA_DIR
from common.myddt import data, ddt
from tools.tools import assert_dict_item, username, email


@ddt
class TestRegister(unittest.TestCase):
    excel = HandExcel(os.path.join(DATA_DIR, 'case_data.xlsx'), 'register')
    test_data = excel.read_excel()

    @data(*test_data)
    def test_register(self, item):
        # 1. 准备测试数据
        method = item["method"]

        # ------------判断用户名和邮箱两个接口-------------
        # 替换pass_name
        if "#pass_name#" in item["url"]:
            item["url"] = item["url"].replace("#pass_name#", str(self.pass_name))
        # 替换pass_email
        if "#pass_email#" in item["url"]:
            item["url"] = item["url"].replace("#pass_email#", str(self.pass_email))

        url = conf.get('env', 'base_url') + item["url"]

        # ===============注册接口，替换参数===============
        # 替换参数username
        if "#username#" in item["data"]:
            item["data"] = item["data"].replace('#username#', username())
        # 替换参数email
        if "#email#" in item["data"]:
            item["data"] = item["data"].replace('#email#', email())

        params = eval(item["data"])
        expected = eval(item["expected"])

        # 2. 请求接口，获取实际结果
        res = requests.request(method, url, json=params).json()

        # 如果是"正常注册"接口,提取username 赋值给预期结果里面的username
        if item["title"] == "正常注册":
            # 设置为类属性
            TestRegister.pass_name = res["username"]
            expected["username"] = self.pass_name

            TestRegister.pass_email = params["email"]



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
