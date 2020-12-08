"""
============================
Author:柠檬班-木森
Time:2020/9/5   10:55
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

res1 = {
    "password": [
        "该字段是必填项。"
    ]
}

expected1 = {
    "password": [
        "该字段是必填项。"
    ]
}

res2 = {
    "email": [
        "该字段是必填项。"
    ]
}

expected2 = {
    "email": [
        "该字段是必填项。"
    ]
}

res3 = {
    "id": 4,
    "username": "musen0033",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Im11c2VuMDAzMyIsImV4cCI6MTU5OTM2MTAyOCwiZW1haWwiOiJtdXNlbjAwMTJAcXEuY29tIn0.cwVJm3U_JEATzUgDYMNnj91XiMQlWwpO29NmPPrMD_E"
}

expected3 = {
    "username": "musen00332",
}


def assert_dict_item(dic1, dic2):
    """
    断言dic1中的所有元素都是dic2中的成员，成立返回True,不成立引发断言错误
    :param dic1: 字典
    :param dic2: 字典
    :return:
    """
    for item in dic1.items():
        if item not in dic2.items():
            raise AssertionError("{} items not in {}".format(dic1, dic2))


assert_dict_item(expected2, res2)
