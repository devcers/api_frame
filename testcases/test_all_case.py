# -*- coding: utf-8 -*-
"""
test_all_case.py

作者: Devcer
创建日期: 2025/8/2
描述: 
"""
from pathlib import Path

import pytest

from commons.extract_util import ExtractUtil
from commons.model_util import CaseInfo, verify_yaml
from commons.request_util import RequestUtil
from commons.yaml_util import read_yaml


class TestAllCase:
    pass

eu = ExtractUtil()

def create_testcase(yaml_path):

    @pytest.mark.parametrize("caseinfo",read_yaml(yaml_path))
    def fun(self,caseinfo):
        new_caseinfo = verify_yaml(caseinfo)
        print(new_caseinfo)
        new_request = eu.use_extract_value(new_caseinfo.request)

        responses = RequestUtil().send_all_request(**new_request)
        if new_caseinfo.extract:
            print(new_caseinfo.extract)
            for key,value in new_caseinfo.extract.items():
                eu.extract(responses,key,*value)

    return fun


test_path = Path(__file__).parent
yaml_case_list = test_path.glob("**/*.yaml")

for yaml_path in yaml_case_list:
    print(yaml_path)
    print(yaml_path.stem)
    # 通过反射创建测试接口的方法
    setattr(TestAllCase,"test_"+yaml_path.stem,create_testcase(yaml_path))