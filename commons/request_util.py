# -*- coding: utf-8 -*-
"""
request_util.py

作者: Devcer
创建日期: 2025/8/2
描述: 
"""
import logging

from pip._internal.network import session
from requests import Session

logger = logging.getLogger(__name__)
class RequestUtil:

    session = Session()

    def send_all_request(self, **kwargs: object):
        # 处理公共参数
        total_params = {

        }

        for key, value in kwargs.items():
            if key == "params":
                kwargs["params"].update(total_params)
            elif key == "files":
                for file_key,file_value in value.items():
                    value[file_key] = open(file_value, 'rb')
        res = RequestUtil.session.request(**kwargs)
        logger.info(res.text)
        return res
