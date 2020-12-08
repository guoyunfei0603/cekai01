"""
============================
Author:小白31
Time:2020/12/6 21:22
E-mail:1359239107@qq.com
============================
"""
import requests

from common.handle_conf import conf
from common.handle_log import log
from tools.tools import username


def setup_login(cls):
    """登录"""
    # 测试数据
    url = conf.get("env", "base_url") + "/user/login/"
    method = "POST"
    params = {"username": "yunfei001", "password": "123456"}

    # 请求接口
    res = requests.request(method, url, json=params).json()

    # 提取返回的token，设置为类属性
    cls.token = res["token"]


def setup_projects(cls):
    """创建项目"""

    method = "post"
    url = conf.get("env", "base_url") + "/projects/"

    params = {
        "name": username(), "leader": "江姐", "tester": "水易寒",
        "programmer": "童可", "publish_app": "勤学app", "desc": "勤能补拙"}
    headers = {"Authorization": "JWT" + " " + cls.token}

    res = requests.request(method, url, json=params, headers=headers).json()

    # 设置项目id为类属性
    cls.project_id = res["id"]


def setup_interfaces(cls):
    """创建接口"""
    url = conf.get("env", "base_url") + "/interfaces/"
    method = "post"
    params = {"name": username(), "tester": "水易寒", "project_id": cls.project_id, "desc": "创建加入购物车接口"}
    headers = {"Authorization": "JWT" + " " + cls.token}

    res = requests.request(method, url, json = params, headers=headers).json()

    # 设置接口返回id为类属性
    cls.interfaces_id = res["id"]
