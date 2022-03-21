# -*-coding:utf-8 -*-
"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/3/21 3:33 PM
LastEditors: John Holl
LastEditTime: 2022/3/21 3:33 PM
"""
import yaml


def get_conf() -> object:
    with open('app.yml', mode='r', encoding='utf-8') as f:
        file_date = f.read()
        data = yaml.load(file_date, Loader=yaml.FullLoader)
        # po_new = dict()
        print(data)
        return data


APP = get_conf()
