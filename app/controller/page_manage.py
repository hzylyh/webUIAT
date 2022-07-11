# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/7/11 14:50
LastEditors: John Holl
LastEditTime: 2022/7/11 14:50
"""
from app.controller import api
from utils.response.response_util import ResponseUtil
from main import db
from flask import request


@api.route('/pageManage/add', methods=['POST'])
def add_page():
    # TODO 目前不是树形结构，只能嵌套一级，后续可能有需求多级嵌套，待开发
    page_info = request.get_json()
    print(page_info)
    result = db.create('insert into tb_page(`page_id`, `page_name`, `project_id`)'
                       ' values (%s, %s, %s)',
                       (page_info['page_id'], page_info['page_name'], page_info['project_id']))
    return ResponseUtil.success(result)


@api.route('/pageManage/delete', methods=['POST'])
def delete_page():
    page_info = request.get_json()
    result = db.create('delete from tb_page where page_id = %s', (page_info['page_id']))
    return ResponseUtil.success(result)


@api.route('/pageManage/getPageList', methods=['POST'])
def get_page_list():
    page_info = request.get_json()
    result = db.get_list('select * from tb_page where project_id = %s', (page_info['project_id']))
    # project_info = db.get_one('select tp.project_id, tp.project_name from tb_project tp where project_id = %s',
    #                           (page_info['project_id']))
    return ResponseUtil.success(result)
