
import os
# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)

# 用例数据excel的项目路径
DATA_DIR = os.path.join(BASE_DIR,"data")

# 测试用例类
CASE_DIR = os.path.join(BASE_DIR,"testcase")

# 测试报告的目录路径
REPORT_DIR = os.path.join(BASE_DIR,"reports")

# 日志目录的项目路径
LOG_DIR = os.path.join(BASE_DIR,"logs")

# 配置文件目录的路径
CONF_DIR = os.path.join(BASE_DIR,"conf")