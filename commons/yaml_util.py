# -*- coding: utf-8 -*-
"""
yaml_util.py

作者: Devcer
创建日期: 2025/8/2
描述: 
"""
import yaml


def read_yaml(path):
     with open(path,"r",encoding='utf-8') as f:
         value = yaml.load(f,Loader=yaml.SafeLoader)
         return value


def read_all():
    with open("extract.yaml", "r", encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.SafeLoader)
        return value

def write_yaml(value):
    with open("extract.yaml","a+",encoding='utf-8') as f:
        yaml.safe_dump(value,f,allow_unicode=True)

def clean_yaml(path):
    with open(path,"r",encoding='utf-8') as f:
        pass