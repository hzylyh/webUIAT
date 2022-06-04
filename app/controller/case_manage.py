# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/6/4 14:23
LastEditors: John Holl
LastEditTime: 2022/6/4 14:23
"""

from app.controller import api
from utils.response.response_util import ResponseUtil
from main import db


@api.route('/caseManage/getCaseList', methods=['POST'])
def get_case_list():
    result = db.get_list('select * from tb_case')
    print(result)
    return ResponseUtil.success(result)
