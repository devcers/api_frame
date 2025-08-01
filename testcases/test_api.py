# -*- coding: utf-8 -*-
"""
@File    : test_api.py
@Time    : 2025/8/1 18:15
@Author  : 昭阳
@Email   : devcer@163.com
@Description : 
"""



class TestApi:

    # @pytest.fixture(scope="作用域", autouse="自动/手动",params="参数化",ids="参数化时参数别名",name="固件别名")
    # @pytest.mark.usefixtures("exe_sql") 手动调用固件方法(类使用) 如果是函数使用,则将固件方法传入函数参数中
    def test_api(self, test_api):
        print(test_api)

    def test_order(self):
        print("测试订单")