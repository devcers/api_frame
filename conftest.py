# -*- coding: utf-8 -*-
"""
@File    : conftest.py
@Time    : 2025/8/1 18:15
@Author  : 昭阳
@Email   : devcer@163.com
@Description :
"""


import pytest


@pytest.fixture(scope="function", autouse=False, params=["登录成功", "登录失败", "登录一般"],
                ids=["success", "failure", "soso"],
                name="test_api")
def exe_sql(request):
    print("用例之前执行sql")
    yield request.param
    print("用例之后执行sql")

@pytest.fixture(scope="function",autouse=True)
def exe_order():
    print("用例之前:订单之前")
    yield
    print("用例之后:订单之后")