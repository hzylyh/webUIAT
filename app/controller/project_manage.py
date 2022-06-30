# -*-coding:utf-8 -*-
"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/6/5 17:27
LastEditors: John Holl
LastEditTime: 2022/6/5 17:27
"""

from app.controller import api
from utils.response.response_util import ResponseUtil
from main import db
from flask import request


@api.route('/projectManage/add', methods=['POST'])
def add_project():
    project_info = request.get_json()
    print(project_info)
    result = db.create('insert into tb_case(`case_name`, `module_name`, `step`, `po`, `po_attr`,'
                       ' `input_value`, `expect_value`)'
                       ' values (%s, %s, %s, %s, %s, %s, %s)',
                       (project_info['case_name'], project_info['module_name'], project_info['step'],
                        project_info['po'], project_info['po_attr'], project_info['input_value'],
                        project_info['expect_value']))
    return ResponseUtil.success(result)


@api.route('/projectManage/getProjectList', methods=['POST'])
def get_project_list():
    result = db.get_list('select * from tb_project')
    print(result)
    return ResponseUtil.success(result)

