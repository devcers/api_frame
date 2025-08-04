# -*- coding: utf-8 -*-
"""
@File    : ddt_util.py
@Time    : 2025/8/4 19:02
@Author  : 昭阳
@Email   : devcer@163.com
@Description : 
"""
import yaml


# 读取测试用例
def read_testcase(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        value = yaml.safe_load(f)
        if len(value) >= 2:
            return [value]
        else:
            if "parametrize" in dict(*value).keys():
                new_caseinfo = ddts(*value)
                return new_caseinfo
            else:
                return value


def ddts(caseinfo:dict):
    data_list = caseinfo["parametrize"]

    len_flag = True

    # 先获取参数名的长度
    name_len = len(data_list[0])

    for data in data_list:
        if len(data) != name_len:
            len_flag = False
            break

    # 如果长度没有问题
    str_caseinfo = yaml.dump(caseinfo)
    new_caseinfo = []

    for x in range(1,len(data_list)): # x表示行
        raw_caseinfo = str_caseinfo

        for y in range(0,name_len): # y 表示列
            if isinstance(data_list[x][y], str) and data_list[x][y].isdigit():
                data_list[x][y] = "'" + data_list[x][y] + "'"
            raw_caseinfo = raw_caseinfo.replace("$ddt{"+data_list[0][y]+"}", data_list[x][y])

        case_dict = yaml.safe_load(raw_caseinfo)
        case_dict.pop("parametrize")
        new_caseinfo.append(case_dict)

    return new_caseinfo