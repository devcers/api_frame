# -*- coding: utf-8 -*-
"""
main_util.py

作者: Devcer
创建日期: 2025/8/3
描述: 
"""
from commons.extract_util import ExtractUtil
from commons.model_util import verify_yaml
from commons.request_util import RequestUtil

eu = ExtractUtil()
ru = RequestUtil()
def stand_case_flow(caseinfo):
    new_caseinfo = verify_yaml(caseinfo)
    print(new_caseinfo)
    new_request = eu.change(new_caseinfo.request)

    responses = ru.send_all_request(**new_request)
    if new_caseinfo.extract:
        print(new_caseinfo.extract)
        for key, value in new_caseinfo.extract.items():
            eu.extract(responses, key, *value)