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
from flask import request


@api.route('/caseManage/add', methods=['POST'])
def add_case():
    case_info = request.get_json()
    print(case_info)
    result = db.create('insert into tb_case(`case_id`, `case_name`, `module_name`, `step`, `po_id`, `page_id`,'
                       ' `input_value`, `expect_value`, `project_id`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (case_info['case_id'], case_info['case_name'], case_info['module_name'], case_info['step'],
                        case_info['po_id'], case_info['page_id'], case_info['input_value'], case_info['expect_value'],
                        case_info['project_id']))
    return ResponseUtil.success(result)


@api.route('/caseManage/delete', methods=['POST'])
def delete_case():
    case_info = request.get_json()
    result = db.create('delete from tb_case where case_id = %s', (case_info['case_id']))
    return ResponseUtil.success(result)


@api.route('/caseManage/getCaseList', methods=['POST'])
def get_case_list():
    case_info = request.get_json()
    result = db.get_list('select * from tb_case where project_id = %s order by create_time asc',
                         (case_info['project_id']))
    print(result)
    return ResponseUtil.success(result)


@api.route('/caseManage/getCaseResult', methods=['POST'])
def get_case_result():
    result = db.get_list('select tc.case_id, tc.module_name, tc.case_name, tc.step, tr.start_time, tr.result'
                         ' from tb_result tr '
                         'left join tb_case tc on tc.case_id = tr.case_id')
    print(result)
    return ResponseUtil.success(result)
