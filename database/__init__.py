# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/5/10 20:53
LastEditors: John Holl
LastEditTime: 2022/5/10 20:53
"""
import pymysql


def create_db():
    db = pymysql.connect(host='localhost', user='root', password='123456', db='ui_at', port=3306)
    return db
