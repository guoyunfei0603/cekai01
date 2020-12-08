

import pymysql

from common.handle_conf import conf


class DB():
    def __init__(self, host, port, user, password):
        # 第一步、连接数据库
        self.con = pymysql.connect(host=host,
                              port=int(port),
                              user=user,
                              password=password,
                              charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor
                              )

        # 第二步、创建一个游标对象
        self.cur = self.con.cursor()

    def find_data(self, sql):
        '''查询数据'''
        # 先提交事务，同步数据库最新的数据
        self.con.commit()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res


db = DB(
    host=conf.get("mysql", "host"),
    port=conf.get("mysql", "port"),
    user=conf.get("mysql", "user"),
    password=conf.get("mysql", "password")
)

if __name__ == '__main__':
    res= db.find_data("select * from futureloan.member limit 3")
    print(res)