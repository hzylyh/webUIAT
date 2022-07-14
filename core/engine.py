"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 13:44:11
LastEditors: John Holl
LastEditTime: 2022-03-19 15:12:43
"""
import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from core import case_handler
from core import po_handler
from entity.case_entity import CaseEntity
from typing import List, Dict
from selenium import webdriver
from constant.constant import *
from main import db
from utils.common import get_time


def load_case(project_id: str) -> List[CaseEntity]:
    """
    加载用例
    :rtype: object
    """
    return case_handler.from_database(project_id)


def load_po() -> Dict:
    """
    加载po
    :rtype: object
    """
    return po_handler.load_project()


def execute(driver: WebDriver, handle: Dict, case: CaseEntity) -> bool:
    """
    核心执行逻辑
    :rtype: object
    """
    ele = WebDriverWait(driver, 15).until(lambda x: x.find_element(by=handle['locate_type'],
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
            return True
        else:
            logging.info('----------fail------------')
            return False
    return True


def run(project_id: str):
    """
    总执行方法
    :rtype: object
    """
    cases = load_case(project_id)
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path=PROJECT['selenium']['driver-path'], options=option)
    driver.get(PROJECT['selenium']['web-url'])
    driver.maximize_window()

    start_time = get_time()
    for case in cases:
        handle = db.get_one('select * from tb_page_object where po_id = %s', (case['po_id']))
        print(handle)
        try:
            if execute(driver, handle, case):
                db.create('insert into tb_result(`case_id`, `result`, `start_time`) values (%s, %s, %s)',
                          (case['case_id'], "0", start_time))
            else:
                db.create('insert into tb_result(`case_id`, `result`, `start_time`) values (%s, %s, %s)',
                          (case['case_id'], "1", start_time))
        except Exception as e:
            print(e)
            db.create('insert into tb_result(`case_id`, `result`, `start_time`) values (%s, %s, %s)',
                      (case['case_id'], "1", start_time))
