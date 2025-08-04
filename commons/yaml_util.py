# -*- coding: utf-8 -*-
"""
yaml_util.py

作者: Devcer
创建日期: 2025/8/2
描述: 
"""
import yaml


def read_yaml(path):
    print("read_yaml 开始")
    try:
        with open(path, "r", encoding='utf-8') as f:
            value = yaml.safe_load(f)
            # 使用更安全的打印方式
            print(f"read_yaml方法执行结果: {value}")
            return value
    except FileNotFoundError:
        print(f"错误: 文件 '{path}' 不存在")
    except yaml.YAMLError as e:
        print(f"错误: YAML格式解析失败 - {e}")
    except Exception as e:
        print(f"错误: 读取文件时发生意外 - {e}")


def read_all():
    with open("extract.yaml", "r", encoding='utf-8') as f:
        value = yaml.safe_load(f)
        return value

def write_yaml(value):
    with open("extract.yaml","a+",encoding='utf-8') as f:
        yaml.safe_dump(value,f,allow_unicode=True)

def clean_yaml(path):
    with open(path,"r",encoding='utf-8') as f:
        pass