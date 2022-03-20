"""
Description:
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 14:02:48
LastEditors: John Holl
LastEditTime: 2022-03-19 14:19:05
"""


class CaseEntity:
    def __init__(self, case_id, name, page, step, val):
        self._case_id = case_id
        self._name = name
        self._page = page
        self._step = step
        self._val = val

    # getter
    @property
    def case_id(self):
        return self._case_id

    # setter
    @case_id.setter
    def case_id(self, case_id):
        self._case_id = case_id

    # getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, name):
        self._name = name

    # getter
    @property
    def page(self):
        return self._page

    # setter
    @page.setter
    def page(self, page):
        self._page = page

    # getter
    @property
    def step(self):
        return self._step

    # setter
    @step.setter
    def step(self, step):
        self._step = step

    # getter
    @property
    def val(self):
        return self._val

    # setter
    @val.setter
    def val(self, val):
        self._val = val

    def __repr__(self) -> str:
        return 'CaseEntity(%s, %s, %s, %s, %s) ' % (self.case_id, self.name, self.page, self.step, self.val)
