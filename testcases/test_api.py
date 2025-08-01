# -*- coding: utf-8 -*-
"""
@File    : test_api.py
@Time    : 2025/8/1 18:15
@Author  : 昭阳
@Email   : devcer@163.com
@Description : 
"""
import allure


@allure.epic("项目名称:昭阳的开发项目")
@allure.feature("模块名称:登录模块")
class TestApi:

    # @pytest.fixture(scope="作用域", autouse="自动/手动",params="参数化",ids="参数化时参数别名",name="固件别名")
    # @pytest.mark.usefixtures("exe_sql") 手动调用固件方法(类使用) 如果是函数使用,则将固件方法传入函数参数中
    @allure.story("接口名称:登录接口")
    @allure.title("验证登录是否成功")
    def test_api(self, test_api):
        print(test_api)
        allure.dynamic.title("登录接口成功")
        with allure.step("第一步"):
            with open("","rb") as f:
                allure.attach(f.read(),name="输入用户名截图",attachment_type=allure.attachment_type.PNG)

    def test_order(self):
        print("测试订单")