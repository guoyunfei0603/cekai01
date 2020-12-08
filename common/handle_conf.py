
from configparser import ConfigParser
from common.handle_path import CONF_DIR
import os


class Config(ConfigParser):
    def __init__(self, filename, encoding="utf-8"):
        super().__init__()
        self.read(filename, encoding=encoding)
        self.filename = filename
        self.encoding = encoding

    def write_data(self, select, option, value):
        """往配置文件中写入数据"""
        self.set(select, option, value)
        self.write(fp=open(self.filename, "w", encoding=self.encoding))


conf = Config(os.path.join(CONF_DIR, "config.ini"))

# conf.write_data("test_data","name","小白")
# print(conf.get("report","filename"))
