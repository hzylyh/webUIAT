# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/5/10 20:01
LastEditors: John Holl
LastEditTime: 2022/5/10 20:01
"""

from .response_model import Response
import json
from utils.trans import class_to_dict


class ResponseUtil:
    @staticmethod
    def success(data) -> json:
        response = Response()
        response.code = '00000'
        response.msg = '请求成功'
        response.result = data
        return class_to_dict(response)

    @staticmethod
    def fail() -> Response:
        response = Response()
        response.code = '000001'
        response.msg = '请求失败'
        return response
