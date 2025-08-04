# -*- coding: utf-8 -*-
"""
test_all_case.py

作者: Devcer
创建日期: 2025/8/2
描述: 
"""
from pathlib import Path

import allure
import pytest

from commons.extract_util import ExtractUtil
from commons.main_util import stand_case_flow
from commons.model_util import CaseInfo, verify_yaml
from commons.request_util import RequestUtil
from commons.yaml_util import read_yaml

#@pytest.mark.skip
def create_testcase(path):

    @pytest.mark.parametrize("case_info",read_yaml(path))
    def fun(self,case_info):
        # 校验yaml中的数据
        case_obj = verify_yaml(case_info)
        allure.dynamic.feature(case_obj.feature)
        allure.dynamic.story(case_obj.story)
        allure.dynamic.title(case_obj.title)
        stand_case_flow(case_obj)
    return fun

class TestAllCase:
    pass

test_path = Path(__file__).parent
yaml_case_list = test_path.glob("**/*.yaml")

for yaml_path in yaml_case_list:
    print("重点!!!!!!")
    print(yaml_path)
    # 通过反射创建测试接口的方法
    setattr(TestAllCase,"test_"+yaml_path.stem,create_testcase(yaml_path))