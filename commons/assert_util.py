# -*- coding: utf-8 -*-
"""
@File    : assert_util.py
@Time    : 2025/8/4 15:48
@Author  : 昭阳
@Email   : devcer@163.com
@Description : 断言的处理文件
"""
import copy

import pymysql
from pymysql import Connection
from pymysql.cursors import Cursor


class AssertUtil:


    def conn_database(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='<PASSWORD>',
            db='test',
            charset='utf8'
        )
        return self.conn

    def execute_sql(self, sql):
        # 创建连接
        conn = self.conn_database()
        # 创建游标
        cursor = conn.cursor()
        # 执行sql
        cursor.execute(sql)

        value = cursor.fetchone()

        cursor.close()
        conn.close()
        return value

    def assert_all_case(self,res,assert_type,value):
        new_res = copy.deepcopy(res)
        # 把new_res的json()改成json属性
        try:
            new_res.json = new_res.json()
        except Exception:
            new_res.json = {"msg": "response is not JSON"}

        for msg, yq_and_sj_data in value.items():
            # 得到预期和实际结果的值
            yq_data = yq_and_sj_data[0]
            sj_data = yq_and_sj_data[1]

            print(f"断言预期结果 {yq_data}")
            print(f"断言实际结果 {sj_data}")

            # 根据实际的值,从属性中获取,比如 json,text status_code
            try:
                sj_value= getattr(new_res, sj_data)
            except Exception:
                sj_value = value

            print(f"实际的值为 {sj_value}")

            match assert_type:
                case "equals":
                    assert yq_data == sj_value,msg

                case "contains":
                    assert yq_data in sj_data,msg

                case "db_equals":
                    db_value = self.execute_sql(yq_data)
                    assert db_value[0] == sj_value, msg

                case "db_contains":
                    db_value = self.execute_sql(yq_data)
                    assert db_value[0] in sj_value,msg
