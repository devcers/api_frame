# -*- coding: utf-8 -*-
"""
debug_talk.py

作者: Devcer
创建日期: 2025/8/3
描述: 
"""
from datetime import time

import yaml


class DebugTalk:

    def read_yaml(self,key):
        with open("extract.yaml", "r", encoding='utf-8') as f:
            value = yaml.safe_load(f)
            return value[key]

    def add(self,a,b):
        return int(a)+int(b)

    def md5(self):
        pass

    def get_random_number(self):
        return str(int(time.time()))