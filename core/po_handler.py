"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 13:42:16
LastEditors: John Holl
LastEditTime: 2022-03-19 15:24:12
"""

import os
from constant.constant import *

po_manager = {}


def load_project():
    dir = APP['framework']['po']['file-path']
    files = os.listdir(dir)
    for file in files:
        po = read_po(dir + file)
        po_manager[file.split('.')[0]] = po
        return po_manager


def read_po(file_path: object) -> object:
    with open(file_path, 'r', encoding="utf-8") as f:
        file_date = f.read()
        data = yaml.load(file_date, Loader=yaml.FullLoader)
        po_new = dict()
        for obj, obj_v in data.items():
            po_new[obj] = obj_v

        return po_new
