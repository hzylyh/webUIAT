'''
Description: 
Author: John Holl
Github: https://github.com/hzylyh
Date: 2022-03-19 14:02:48
LastEditors: John Holl
LastEditTime: 2022-03-19 14:19:05
'''


class POEntity:
    def __init__(self, type, value, action, expect_val):
        self._type = type
        self._value = value
        self._action = action
        self._expect_val = expect_val

    # getter
    @property
    def type(self):
        return self._type

    # setter
    @type.setter
    def type(self, type):
        self._type = type

    # getter
    @property
    def value(self):
        return self._value

    # setter
    @value.setter
    def value(self, value):
        self._value = value

    # getter
    @property
    def action(self):
        return self._action

    # setter
    @action.setter
    def action(self, action):
        self._action = action

    # getter
    @property
    def expect_val(self):
        return self._expect_val

    # setter
    @expect_val.setter
    def expectVal(self, expect_val):
        self._expect_val = expect_val

    def __repr__(self) -> str:
        return 'POEntity(%s, %s, %s, %s) ' % (self.type, self.value, self.action, self.expect_val)
