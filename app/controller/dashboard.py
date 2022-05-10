# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/5/10 14:31
LastEditors: John Holl
LastEditTime: 2022/5/10 14:31
"""
from app.controller import api


@api.route('/dashboard/getResult', methods=['POST'])
def get_info():
    return {'name': 'name'}
