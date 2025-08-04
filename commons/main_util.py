# -*- coding: utf-8 -*-
"""
main_util.py

作者: Devcer
创建日期: 2025/8/3
描述: 
"""
from commons.assert_util import AssertUtil
from commons.extract_util import ExtractUtil
from commons.model_util import verify_yaml
from commons.request_util import RequestUtil

eu = ExtractUtil()
ru = RequestUtil()
au = AssertUtil()
def stand_case_flow(new_caseinfo):
    new_request = eu.change(new_caseinfo.request)

    responses = ru.send_all_request(**new_request)
    if new_caseinfo.extract:
        for key, value in new_caseinfo.extract.items():
            eu.extract(responses, key, *value)

    # 请求之后,做断言判断
    print("准备做断言处理")
    if new_caseinfo.validate:
        for key, value in eu.change(new_caseinfo.validate).items():
            au.assert_all_case(responses, key, value)
    else:
        print("此用例没有断言")