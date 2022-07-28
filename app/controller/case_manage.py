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
    result = db.create('insert into tb_case(`case_id`, `case_name`, `case_desc`, `project_id`) '
                       'values (%s, %s, %s, %s)',
                       (case_info['case_id'], case_info['case_name'], case_info['case_desc'], case_info['project_id']))
    return ResponseUtil.success(result)


@api.route('/caseManage/delete', methods=['POST'])
def delete_case():
    case_info = request.get_json()
    result = db.create('delete from tb_case where case_id = %s', (case_info['case_id']))
    return ResponseUtil.success(result)


@api.route('/caseManage/edit', methods=['POST'])
def edit_case():
    case_info = request.get_json()
    result = db.create('update tb_case set case_name = %s, case_desc = %s, case_creator = %s where case_id = %s',
                       (case_info['case_name'], case_info['case_desc'], case_info['case_creator'], case_info['case_id']))
    return ResponseUtil.success(result)


@api.route('/caseManage/getCaseList', methods=['POST'])
def get_case_list():
    case_info = request.get_json()
    result = db.get_list('select * from tb_case where project_id = %s order by create_time asc',
                         (case_info['project_id']))
    return ResponseUtil.success(result)


@api.route('/caseManage/getCaseResult', methods=['POST'])
def get_case_result():
    project_info = request.get_json()
    result = db.get_list('select tc.case_id, tc.module_name, tc.case_name, tc.step, tr.start_time, tr.result, tr.message'
                         ' from tb_result tr '
                         'left join tb_case tc on tc.case_id = tr.case_id'
                         ' where tr.start_time = %s', project_info['start_time'])
    return ResponseUtil.success(result)
