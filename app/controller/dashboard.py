# -*-coding:utf-8 -*-
"""
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022/5/10 14:31
LastEditors: John Holl
LastEditTime: 2022/5/10 14:31
"""
from flask import request

from app.controller import api
from utils.response.response_util import ResponseUtil
from main import db


@api.route('/dashboard/getPanelInfo', methods=['POST'])
def get_info():
    project_info = request.get_json()

    # TODO 将几个sql合并，避免多次查询消耗
    last_run_time = db.get_one('select tr.start_time from tb_result tr '
                               'left join tb_case_step tcs on tr.step_id = tcs.step_id '
                               'left join tb_case tc on tcs.case_id = tc.case_id '
                               'where tc.project_id = %s '
                               'order by tr.start_time desc limit 1', project_info['project_id'])
    case_num = db.get_one('select count(1) as case_num from tb_case tc where tc.project_id = %s',
                          project_info['project_id'])
    # success_num = db.get_one("select count(1) as success_num from tb_result tr "
    #                          "where tr.result = '0' and tr.start_time = %s", last_run_time['start_time'])
    # fail_num = db.get_one("select count(1) as fail_num from tb_result tr "
    #                       "where tr.result = '1' and tr.start_time = %s", last_run_time['start_time'])


    res = {
        "last_run_time": last_run_time['start_time'] if last_run_time['start_time'] is not None else '暂无',
        "case_num": case_num['case_num'],
        # "success_num": success_num['success_num'],
        # "fail_num": fail_num['fail_num']
    }
    return ResponseUtil.success(res)


@api.route('/dashboard/getCaseResult', methods=['POST'])
def get_case_result():
    project_info = request.get_json()
    result = db.get_list('select tcs.step_id, tc.case_name, tcs.step_name, tr.start_time, tr.result, tr.message '
                         'from tb_result tr '
                         'left join tb_case_step tcs '
                         'on tr.step_id = tcs.step_id '
                         'left join tb_case tc '
                         'on tcs.case_id = tc.case_id '
                         'where tr.start_time = %s',
                         project_info['start_time'])
    return ResponseUtil.success(result)
