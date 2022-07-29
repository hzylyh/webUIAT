# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/7/25 08:36
LastEditors: John Holl
LastEditTime: 2022/7/25 08:36
"""
from app.controller import api
from utils.response.response_util import ResponseUtil
from main import db
from flask import request


@api.route('/caseStepManage/add', methods=['POST'])
def add_case_step():
    case_step_info = request.get_json()
    result = db.create('insert into tb_case_step(`step_id`, `step_name`, `case_id`, `page_id`, `po_id`,'
                       ' `input_value`, `expect_value`) '
                       'values (%s, %s, %s, %s, %s, %s, %s)',
                       (case_step_info['step_id'], case_step_info['step_name'],
                        case_step_info['case_id'], case_step_info['page_id'], case_step_info['po_id'],
                        case_step_info['input_value'], case_step_info['expect_value']))
    return ResponseUtil.success(result)


@api.route('/caseStepManage/delete', methods=['POST'])
def delete_case_step():
    case_step_info = request.get_json()
    result = db.create('delete from tb_case_step where step_id = %s', (case_step_info['step_id']))
    return ResponseUtil.success(result)


@api.route('/caseStepManage/edit', methods=['POST'])
def edit_case_step():
    case_step_info = request.get_json()
    result = db.create('update tb_case_step set step_name = %s, page_id = %s, '
                       'po_id = %s, input_value = %s, expect_value = %s '
                       'where step_id = %s',
                       (case_step_info['step_name'], case_step_info['page_id'], case_step_info['po_id'],
                        case_step_info['input_value'], case_step_info['expect_value'], case_step_info['step_id']))
    return ResponseUtil.success(result)


@api.route('/caseStepManage/list', methods=['POST'])
def get_case_step_list():
    case_step_info = request.get_json()
    result = db.get_list('select * from tb_case_step where case_id = %s order by create_time asc',
                         (case_step_info['case_id']))
    return ResponseUtil.success(result)
