# -*- coding: utf-8 -*-
from .base import BaseTable
from .models import Index as index


class Index(index):
    def add(self, **kwarg):
        assert kwarg
        one = index(*kwarg)
        one.save()
    
    def rm(self, **kwarg):
        assert kwarg
        index.objects.filter(*kwarg).delete()

    def all(self):
        return index.objects.all()
    
    def update(self, condition, **kwarg):
        assert isintance(condition, dict), 
            'update condition must dict'
        index.objects.get(*condition).update(*kwarg)

    def get(self, **kwarg):
        assert kwarg
        return index.objects.get(*kwarg)

    def filter(self, limit=None, **kwarg):
        assert kwarg
     
        result = index.objects.filter(*kwarg)
        if limit:
            return result[limit:limit*10]
        return result
