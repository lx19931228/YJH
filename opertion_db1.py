"""
dict 数据库处理
提供服务端所有数据库操作
"""
import pymysql
import hashlib

SALT = "%y&j$h_"


class Database:
    def __init__(self, host='localhost',
                 port=3306,
                 user='root',
                 passwd='123456',
                 charset='utf8',
                 database='dict'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.database = database
        self.connect_db()  # 连接数据库

    # 链接数据库
    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)

    # 创建游标
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 关闭数据库
    def close(self):
        self.db.close()

    # 注册操作
    def register(self, name, passwd):
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()  # 如果有查询结果则name存在
        if r:
            return False

        # 密码加密处理
        hash = hashlib.md5((name + SALT).encode())
        hash.update(passwd.encode())  # 算法加密
        passwd = hash.hexdigest()  # 提取加密后的密码

        # 插入数据库
        sql = "insert into user (name,passwd) values (%s,%s)"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    # 数据库登录处理
    def login(self, name, passwd):
        hash = hashlib.md5((name + SALT).encode())
        hash.update(passwd.encode())
        passwd = hash.hexdigest()
        sql = "select * from user where name='%s' and passwd='%s' " % (name, passwd)
        self.cur.execute(sql)
        r = self.cur.fetchone()  # 如果有查询结果则name存在
        if r:
            return True
        else:
            return False

    def insert_history(self, name, word):
        sql = "insert into history(user,word) values('%s','%s')" % (name, word)
        try:
            self.cur.execute(sql)
            self.db.commit()
            return sql
        except Exception:
            self.db.rollback()
            return False

    def query(self, name, word):
        sql = "select mean from words where word='%s'" % word
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return r[0]

    def history(self, name):
        sql = "select* from history where user='%s'order by time desc" % name
        self.cur.execute(sql)
        return self.cur.fetchmany(10)
