# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/5/11 09:32
LastEditors: John Holl
LastEditTime: 2022/5/11 09:32
"""

import pymysql
import threading

DB_CONFIG = {
    # "host": "192.168.1.201",
    "host": "127.0.0.1",
    # "port": 3316,
    "port": 3306,
    "user": "root",
    # "passwd": "Mysql_123",
    "passwd": "123456",
    "db": "ui_at",
    "charset": "utf8"
}

lock = threading.Lock()


class SQLManager(object):

    # 初始化实例方法
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    # 连接数据库
    def connect(self):
        self.conn = pymysql.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            passwd=DB_CONFIG["passwd"],
            db=DB_CONFIG["db"],
            charset=DB_CONFIG["charset"]
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 查询多条数据
    def get_list(self, sql, args=None):
        # self.conn.ping(reconnect=True)
        lock.acquire()
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        lock.release()
        return result

    # 查询单条数据
    def get_one(self, sql, args=None):
        # self.conn.ping(reconnect=True)
        lock.acquire()
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        lock.release()
        return result

    # 执行单条SQL语句
    def moddify(self, sql, args=None):
        # self.conn.ping(reconnect=True)
        lock.acquire()
        self.cursor.execute(sql, args)
        self.conn.commit()
        lock.release()

    # 我如果要批量执行多个创建操作，虽然只建立了一次数据库连接但是还是会多次提交，可不可以改成一次连接，
    # 一次提交呢？
    # 可以，只需要用上pymysql的executemany()
    # 方法就可以了。
    # 执行多条SQL语句
    def multi_modify(self, sql, args=None):
        # self.conn.ping(reconnect=True)
        lock.acquire()
        self.cursor.executemany(sql, args)
        self.conn.commit()
        lock.release()

    # 创建单条记录的语句
    def create(self, sql, args=None):
        # self.conn.ping(reconnect=True)
        lock.acquire()
        self.cursor.execute(sql, args)
        self.conn.commit()
        lock.release()
        last_id = self.cursor.lastrowid
        return last_id

    # 关闭数据库cursor和连接
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 最后，我们每次操作完数据库之后都要手动关闭，可不可以写成自动关闭的呢？
    # 联想到我们之前学过的文件操作，使用with语句可以实现缩进结束自动关闭文件句柄的例子。
    # 我们来把我们的数据库连接类SQLManager类再优化下，使其支持with语句操作。
    # 进入with语句自动执行
    def __enter__(self):
        return self

    # 退出with语句块自动执行
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
