# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/7/11 17:52
LastEditors: John Holl
LastEditTime: 2022/7/11 17:52
"""
from app.controller import api
from utils.response.response_util import ResponseUtil
from main import db
from flask import request


@api.route('/pageObjectManage/add', methods=['POST'])
def add_page_object():
    po_info = request.get_json()
    print(po_info)
    result = db.create('insert into tb_page_object(`po_id`, `po_name`, `locate_type`, `locate_value`, `action`,'
                       ' `page_id`)'
                       ' values (%s, %s, %s, %s, %s, %s)',
                       (po_info['po_id'], po_info['po_name'], po_info['locate_type'], po_info['locate_value'],
                        po_info['action'], po_info['page_id']))
    return ResponseUtil.success(result)


@api.route('/pageObjectManage/delete', methods=['POST'])
def delete_page_object():
    po_info = request.get_json()
    result = db.create('delete from tb_page_object where po_id = %s', (po_info['po_id']))
    return ResponseUtil.success(result)


@api.route('/pageObjectManage/edit', methods=['POST'])
def edit_page_object():
    po_info = request.get_json()
    result = db.create('update tb_page_object '
                       'set po_name = %s, locate_type = %s, locate_value = %s, `action` = %s, page_id = %s '
                       'where po_id = %s',
                       (po_info['po_name'], po_info['locate_type'], po_info['locate_value'], po_info['action'],
                        po_info['page_id'], po_info['po_id']))
    return ResponseUtil.success(result)


@api.route('/pageObjectManage/list', methods=['POST'])
def get_page_object_list():
    po_info = request.get_json()
    result = db.get_list('select * from tb_page_object where page_id = %s', (po_info['page_id']))
    # project_info = db.get_one('select tp.project_id, tp.project_name from tb_project tp where project_id = %s',
    #                           (page_info['project_id']))
    return ResponseUtil.success(result)
