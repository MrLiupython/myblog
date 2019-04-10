# -*- coding: utf-8 -*-
from .base import Base
from .models import Blog, Index, Text

class Blog_(Base):
    def add(**kwarg):
        assert kwarg

        index = kwarg.pop('kind', 'other')
        text = kwarg.pop('text', 'Nothing')
        print(kwarg)
        
        text_ob = Text.objects.create(text=text)

        try:
            condition = Index.objects.get(kind=index)
        except:
            condition = Index.objects.create(kind=index)
        one = Blog(kind=condition, text=text_ob, **kwarg)
        
        one.save()

    def rm(**kwarg):
        assert kwarg
        Blog.objects.get(**kwarg).delete()
    
    def update(condition, **kwarg):
        assert isinstance(condition, dict), \
            'condition must dict'
        assert kwarg

        one = Blog.objects.get(*condition)
        if not one:
           return
        
        index = kwarg.pop('kind')
        text = kwarg.pop('text')
        
        if index:
            one.kind.update(kind=index)

        if kwarg:
            one.update(**kwarg)
    
        if text:
            one.text.update(text=text)

    def get(**kwarg):
        assert kwarg
 
        return Blog.objects.get(**kwarg)

    def filter(limit=None, **kwarg):
        assert kwarg
    
        result = Blog.objects.filter(**kwarg)
        if limit:
            return result[limit:limit*10]
        return result
