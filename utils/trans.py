# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/5/10 20:38
LastEditors: John Holl
LastEditTime: 2022/5/10 20:38
"""


def convert_to_dict(obj):
    """把Object对象转换成Dict对象"""
    dict = {}
    dict.update(obj.__dict__)
    return dict


def convert_to_dicts(objs):
    """把对象列表转换为字典列表"""
    obj_arr = []

    for o in objs:
        # 把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)

    return obj_arr


def class_to_dict(obj):
    """把对象(支持单个对象、list、set)转换成字典"""
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__

    if is_list or is_set:
        obj_arr = []
        for o in obj:
            # 把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict
