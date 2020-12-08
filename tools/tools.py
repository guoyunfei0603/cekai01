"""
============================
Author:小白31
Time:2020/12/1 23:24
E-mail:1359239107@qq.com
============================
"""
import random


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


def username():
    """生成随机名字"""
    str1 = '皮卡丘'
    random_num = random.randint(1, 10000000)
    username = str1 + str(random_num)
    return username

def email():
    """生成随机邮箱"""
    str1 = "@qq.com"
    num1 = random.randint(1000000000,9999999999)
    email = str(num1) + str1
    return email

# if __name__ == '__main__':
#     res = username()
#     print(type(res))
#
#     res2 = email()
