# # -*- coding: utf-8 -*-
# """
# @File    : test_api.py
# @Time    : 2025/8/1 18:15
# @Author  : 昭阳
# @Email   : devcer@163.com
# @Description :
# """
# import re
#
# import allure
# import pytest
# import requests
#
# from commons.request_util import RequestUtil
# from commons.yaml_util import read_yaml, write_yaml
#
#
# @allure.epic("项目名称:昭阳的开发项目")
# @allure.feature("模块名称:登录模块")
# class TestApi:
#
#     # # @pytest.fixture(scope="作用域", autouse="自动/手动",params="参数化",ids="参数化时参数别名",name="固件别名")
#     # # @pytest.mark.usefixtures("exe_sql") 手动调用固件方法(类使用) 如果是函数使用,则将固件方法传入函数参数中
#     # @allure.story("接口名称:登录接口")
#     # @allure.title("验证登录是否成功")
#     # def test_api(self, test_api):
#     #     print(test_api)
#     #     allure.dynamic.title("登录接口成功")
#     #     with allure.step("第一步"):
#     #         with open("","rb") as f:
#     #             allure.attach(f.read(),name="输入用户名截图",attachment_type=allure.attachment_type.PNG)
#     #
#     # @pytest.mark.parametrize("caseinfo",read_yaml('./testcases/test_api.yaml'))
#     # def test_order(self):
#     #     print("测试订单")
#
#     @pytest.mark.parametrize("caseinfo",read_yaml('./testcases/test_phpwind.yaml'))
#     def test_phpwid(self,caseinfo):
#         print("test_phpwind的参数为%s" %caseinfo)
#         method = caseinfo["request"]["method"]
#         url = caseinfo["request"]["url"]
#         res = RequestUtil().send_all_request(method=method,url=url)
#         #print(res.text)
#         search_value = re.search('name="csrf_token" value="(.*?)"',res.text).group(1)
#         #print(search_value)
#         data = {"csrf_token":search_value}
#         write_yaml('./testcases/test_phpwind.yaml',data)
#         # res = RequestUtil.session.request()
#         # print(res.text)
#         # assert res.status_code == 200
#         # assert "本站新帖" in res.text
#
#     @pytest.mark.parametrize("caseinfo",read_yaml('./testcases/test_login.yaml'))
#     def test_login(self,caseinfo):
#         print(caseinfo)
#         method = caseinfo["request"]["method"]
#         url = caseinfo["request"]["url"]
#         data= caseinfo["request"]["data"]
#         headers = caseinfo["request"]["headers"]
#
#         res = RequestUtil().send_all_request(method=method,url=url,headers=headers,data=data)
#
#         print(res.text)
