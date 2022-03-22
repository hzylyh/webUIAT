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


def get_conf(filename) -> object:
    with open(filename, mode='r', encoding='utf-8') as f:
        file_date = f.read()
        data = yaml.load(file_date, Loader=yaml.FullLoader)
        # po_new = dict()
        print(data)
        return data


def get_app_conf():
    return get_conf('application.yml')


def get_project_conf():
    app_conf = get_conf('application.yml')
    return get_conf(app_conf['project']['path'] + '/project.yml')


APP = get_app_conf()
PROJECT = get_project_conf()

PO_SUFFIX = '/po'
CASE_SUFFIX = '/testcase'
