# -*- coding: utf-8 -*-
"""
model_util.py

作者: Devcer
创建日期: 2025/8/3
描述: 
"""
from dataclasses import dataclass


@dataclass
class CaseInfo:
    # 必填
    feature: str
    story: str
    title: str
    request: dict
    vaildate: dict

    # 选填
    extract: dict = None

def verify_yaml(case_info :dict):
    try:
        new_case = CaseInfo(**case_info)
        return new_case
    except Exception as e:
        raise Exception("YAML测试用例不符合框架规范")