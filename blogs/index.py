# -*- coding: utf-8 -*-
from .base import Base
from .models import Index


class Index_(Base):
    def add(**kwarg):
        assert kwarg
        one = Index(**kwarg)
        one.save()
    
    def rm(**kwarg):
        assert kwarg
        Index.objects.filter(*kwarg).delete()

    def all():
        return Index.objects.all()
    
    def update(condition, **kwarg):
        assert isintance(condition, dict), \
            'update condition must dict'
        Index.objects.get(*condition).update(*kwarg)

    def get(**kwarg):
        assert kwarg
        return Index.objects.get(**kwarg)

    def filter(limit=None, **kwarg):
        assert kwarg
     
        result = Index.objects.filter(**kwarg)
        if limit:
            return result[limit:limit*10]
        return result
