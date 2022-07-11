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
    result = db.create('insert into tb_project(`project_id`, `project_name`, `project_desc`)'
                       ' values (%s, %s, %s)',
                       (project_info['project_id'], project_info['project_name'], project_info['project_desc']))
    return ResponseUtil.success(result)


@api.route('/projectManage/delete', methods=['POST'])
def delete_project():
    project_info = request.get_json()
    result = db.create('delete from tb_project where project_id = %s', (project_info['project_id']))
    return ResponseUtil.success(result)


@api.route('/projectManage/detail', methods=['POST'])
def detail_project():
    project_info = request.get_json()
    result = db.get_one('select * from tb_project where project_id = %s', (project_info['project_id']))
    return ResponseUtil.success(result)


@api.route('/projectManage/getProjectList', methods=['POST'])
def get_project_list():
    result = db.get_list('select * from tb_project')
    print(result)
    return ResponseUtil.success(result)

