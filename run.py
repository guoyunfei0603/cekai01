"""
============================
Author:柠檬班-木森
Time:2020/8/1   10:23
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from unittestreport import TestRunner

from common.handle_conf import conf
from common.handle_path import CASE_DIR, REPORT_DIR


# 加载套件
suite = unittest.defaultTestLoader.discover(CASE_DIR)



# 执行用例
runner = TestRunner(suite,
                    filename=conf.get('report', "filename"),
                    report_dir=REPORT_DIR,
                    title='测开测试报告',
                    tester='水易寒',
                    desc="水易寒执行测试生产的报告",
                    templates=1
                    )

runner.run()

# 发送测试报告到邮箱
# runner.send_email(host="smtp.qq.com",
#                   port=465,
#                   user="musen_nmb@qq.com",
#                   password="algmmzptupjccbab",
#                   to_addrs=["3247119728@qq.com"])
