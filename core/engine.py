"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 13:44:11
LastEditors: John Holl
LastEditTime: 2022-03-19 15:12:43
"""
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from entity.case_entity import CaseEntity
from typing import Dict
from selenium import webdriver
from constant.constant import *
from main import db
from utils.common import get_time


def execute(driver: WebDriver, handle: Dict, case: CaseEntity) -> (str, str):
    """
    核心执行逻辑
    :rtype: object
    """
    try:
        ele = WebDriverWait(driver, 15, ignored_exceptions=None).until(lambda x: x.find_element(by=handle['locate_type'],
                                                                       value=handle['locate_value']))
        if handle['action'] == 'input':
            logging.info("input")
            ele.send_keys(case['input_value'])
        elif handle['action'] == 'click':
            logging.info("click")
            ele.click()
        elif handle['action'] == 'check':  # 此处后续扩展，可接收check数组，并且可以接收多种比对方式
            logging.info('check')
            if ele.text == case['expect_value']:
                logging.info('----------pass------------')
                return '0', ''
            else:
                logging.info('----------fail------------')
                msg = '实际：%s 不等于 预期：%s' % (ele.text, case['expect_value'])
                return '1', msg
        return '0', ''
    except TimeoutException:
        return '1', '15秒内没找到对应元素，请确认定位是否正确'
    except Exception as e:
        return '1', e.__repr__()


def run(project_id: str):
    """
    总执行方法
    :rtype: object
    """
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path=PROJECT['selenium']['driver-path'], options=option)
    driver.get(PROJECT['selenium']['web-url'])
    driver.maximize_window()
    start_time = get_time()
    cases = db.get_list('select * from tb_case where project_id = %s order by create_time asc', project_id)
    run_case(driver, cases, start_time)


def run_case(driver: WebDriver, case_list: list, start_time: str):
    """
    case: {
        caseId
    }
    :param driver:
    :param start_time:
    :param case_list:
    :return:
    """
    for case in case_list:
        steps = db.get_list('select * from tb_case_step where case_id = %s order by create_time asc', case['case_id'])
        run_case_step(driver, steps, start_time)


def run_case_step(driver, case_steps, start_time):

    for step in case_steps:
        print(step)
        handle = db.get_one('select * from tb_page_object where po_id = %s', (step['po_id']))
        code, msg = execute(driver, handle, step)
        # db.create('insert into tb_result(`case_id`, `result`, `message`, `start_time`) values (%s, %s, %s, %s)',
        #           (case['case_id'], code, msg, start_time))


