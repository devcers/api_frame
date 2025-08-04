# -*- coding: utf-8 -*-
"""
extract_util.py

作者: Devcer
创建日期: 2025/8/3
描述: 
"""
import copy
from string import Template
import re

import jsonpath
import yaml

from commons.yaml_util import write_yaml, read_all
from debugtalk.debug_talk import DebugTalk


class ExtractUtil:
    # 解析提取变量
    def extract(self,res,var_name,attr_name:str,extr:str,index):
        # 深拷贝
        new_res = copy.deepcopy(res)

        # 把new_res的json()改成json属性
        try:
            new_res.json = new_res.json()
        except Exception:
            new_res.json = {"msg":"response is not json"}

        # 通过反射获取值
        data = getattr(new_res,attr_name)
        print(data)

        if extr.startswith("$"):
            print("是以$开头")
            # 这个强制转换理论上也可以不加,加上的话,会更不容易出问题
            lis = jsonpath.jsonpath(dict(data),extr)
        else:
            print("正则")
            lis = re.findall(extr, data)[0]
        if lis:
            write_yaml({var_name:lis[index]})
        else:
            print("无法找到指定参数")

    # 使用提取后的公共参数
    def change(self,request_data:dict):
        data_str = yaml.dump(request_data)
        new_request_str = self.hotload_replace(data_str)
        data_dict = yaml.safe_load(new_request_str)
        return data_dict

    def hotload_replace(self,request_data:dict):
        data_str = yaml.dump(request_data)

        regexp = "\\$\\{(.*?)\\((.*?)\\)\\}"
        fun_list = re.findall(regexp,data_str)

        for fun in fun_list:
            print(fun)
            # fun[1]没有值代表没有参数
            if fun[1] == "":
                # 后面的()必不可少,代表调用了这个方法
                value = getattr(DebugTalk(),fun[0])()
            else:
                value = getattr(DebugTalk(),fun[0])(*fun[1].split(","))

            # 如果value是字符串且是数字,则给value左右各加一个单引号
            if isinstance(value,str) and value.isdigit():
                value = "'"+value+"'"

            # 旧的值
            old_value = "${"+fun[0]+"("+fun[1]+")}"

            data_str = data_str.replace(old_value,str(value))

        return data_str