# -*- coding: utf-8 -*-
from .base import Base
from .models import Blog as blog, Index, Text

class Blog(Base):
    def add(self, **kwarg):
        assert kwarg

        index = kwarg.pop('index', 'other')
        text = kwarg.pop('text', 'Nothing')

        one = blog(*kwarg)

        condition = Index.objects.get(index=index)
        if condition:
            one.index.add(condition)
        else:
            one.index.add(
                Index.objects.create(index=index)
                )
        
        one.text.add(
            Text.objects.create(text=text)
            )
        one.save()

    def rm(self, **kwarg):
        assert kwarg
        blog.objects.get(*kwarg).delete()
    
    def update(self, condition, **kwarg):
        assert isinstance(condition, dict),
            'condition must dict'
        assert kwarg

        one = blog.objects.get(*condition)
        if not one:
           return
        
        text = kwarg.pop('text')
        
        if kwarg:
            one.update(*kwarg)
    
        if text:
            one.text.update(text=text)

    def get(self, **kwarg):
        assert kwarg
 
        return blog.objects.get(*kwarg)

    def filter(self, limit=None, **kwarg):
        assert kwarg
    
        result = blog.objects.filter(**kwarg)
        if limit:
            return result[limit:limit*10]
        return result
