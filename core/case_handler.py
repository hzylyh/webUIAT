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


def from_csv() -> object:
    cases = []
    case_dir = APP['project']['path'] + CASE_SUFFIX
    files = os.listdir(case_dir)
    for file in files:
        with open(case_dir + '/' + file, mode='r', encoding='utf-8') as f:
            f_csv = csv.reader(f)
            for i, line in enumerate(f_csv):
                if i != 0:
                    if len(line) == 5:
                        case = CaseEntity(line[0], line[1], line[2], line[3], line[4])
                    else:
                        case = CaseEntity(line[0], line[1], line[2], line[3], '')
                    cases.append(case)
        return cases
