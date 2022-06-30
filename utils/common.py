# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/6/30 15:32
LastEditors: John Holl
LastEditTime: 2022/6/30 15:32
"""
import time


def get_time():
    now = time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    return now_time
