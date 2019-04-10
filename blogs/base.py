# -*- coding: utf-8 -*-

class Base:
    def add(self, **kwarg):
        """插入单条数据"""

    def rm(self, **kwarg):
        """删除单条数据"""

    def update(self, **kwarg):
        """更改单条数据"""

    def get(self, **kwarg):
        """查询单条数据"""
    
    def all(self):
        """查询所有数据"""
