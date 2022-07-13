# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/5/11 11:45
LastEditors: John Holl
LastEditTime: 2022/5/11 11:45
"""
from flask import request

from app.controller import api
from utils.response.response_util import ResponseUtil
from core import engine


@api.route('/engine/run', methods=['POST'])
def run():
    project_info = request.get_json()
    engine.run(project_info['project_id'])
    return ResponseUtil.success({})
