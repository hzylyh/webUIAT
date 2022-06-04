"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 15:15:33
LastEditors: John Holl
LastEditTime: 2022-03-19 15:22:06
"""

import csv
import os
from entity.case_entity import CaseEntity
from constant.constant import *
from main import db


def from_csv() -> object:
    """
    从csv中读取测试用例
    :rtype: object
    :return:
    """
    cases = []
    case_dir = APP['project']['path'] + CASE_SUFFIX
    files = os.listdir(case_dir)
    for file in files:
        with open(case_dir + '/' + file, mode='r', encoding='utf-8') as f:
            f_csv = csv.reader(f)
            for i, line in enumerate(f_csv):
                if i == 0:
                    continue
                case = CaseEntity(line)
                cases.append(case)
    return cases


def from_database() -> object:
    """
    从数据库中读取测试用例
    :rtype: object
    """
    cases = db.get_list('select * from tb_case')
    return cases
