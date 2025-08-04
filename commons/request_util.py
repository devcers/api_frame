# -*- coding: utf-8 -*-
"""
request_util.py

作者: Devcer
创建日期: 2025/8/2
描述: 
"""
import logging
from typing import Any

from pip._internal.network import session
from requests import Session

logger = logging.getLogger(__name__)
class RequestUtil:

    session = Session()

    def send_request(self, **kwargs: object):
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
        return res


    def send_all_request(self, **kwargs: dict[str, Any]):
        # 处理公共参数（示例：实际应添加具体公共参数）
        total_params = {
            # "common_param1": "value1",
            # "common_param2": "value2"
        }

        # 处理params：确保存在再更新，避免KeyError
        if "params" in kwargs:
            # 确保params是字典类型（防御性编程）
            if isinstance(kwargs["params"], dict):
                kwargs["params"].update(total_params)
            else:
                logger.warning("params不是字典类型，无法更新公共参数")
        else:
            # 若没有params，直接设置为公共参数
            kwargs["params"] = total_params

        # 处理files：使用上下文管理器确保文件关闭
        if "files" in kwargs and isinstance(kwargs["files"], dict):
            files = kwargs["files"]
            for file_key, file_path in files.items():
                try:
                    # 用with打开文件，自动关闭
                    with open(file_path, 'rb') as f:
                        files[file_key] = f.read()  # 读取内容而非文件对象
                except Exception as e:
                    logger.error(f"打开文件失败：{file_path}，错误：{str(e)}")
                    # 可根据需求选择抛出异常或继续执行
                    # raise ValueError(f"文件处理失败：{file_path}") from e

        try:
            res = RequestUtil.session.request(**kwargs)
            return res
        except Exception as e:
            logger.error(f"请求发送失败：{str(e)}")
            # 根据业务需求决定是否抛出异常
            # raise