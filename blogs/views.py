# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .index import Index_
from .blog import Blog_
from markdown import markdown
from datetime import datetime
import time

def  index_page(request):
    indexs = Index_.all()
    return render(
        request, 
        'blogs/index.html',
        {'indexs': indexs}
        )


def list_page(request):
     kind = request.GET.get('kind')
     if kind:
         index_object = Index_.get(kind=kind)
         blogs = index_object.blog_set.all()
         return render(
             request,
             'blogs/list.html',
             {'blogs': blogs}
             )
     return HttpResponse('你迷路了。。。')


def blog_page(request):
    blog_id = request.GET.get('_id')
    if not blog_id:
        return HttpResponse('nothing')
    blog = Blog_.get(id=blog_id)
    text = markdown(blog.text.text)
    return render(
        request,
        'blogs/blog.html',
        {'blog': blog, 'text': text}
        )


def blog_edit(request):
    blog_id = request.GET.get('_id')
    if blog_id:
        blog = Blog_.get(id=blog_id)
        text = blog.text.text
    else:
        blog = None
        text = None
    return render(
        request,
        'blogs/edit.html',
        {'blog': blog, 'text': text}
        )

def blog_create(request):
    now = str(datetime.now().date())
    year, mounth, day = now.split('-')
    title = request.POST.get('title')
    kind = request.POST.get('kind')
    text = request.POST.get('text')

    if not (title and kind and text):
        return HttpResponse("you must filled all!")
    
    _id = int(time.time())
    p_dict = ({
        'id': _id,
        'title': title,
        'kind': kind,
        'text': text,
        'year': year,
        'mounth': mounth,
        'day': day
        })
    print(p_dict)
    Blog_.add(**p_dict)
    return HttpResponse('OK')

def blog_update(request):
    _id = request.POST.get('_id')
    title = request.POST.get('title')
    kind = request.POST.get('kind')
    text = request.POST.get('text')
    
    if not (_id and title and kind and text):
        return HttpResponse("you must filled all!")
    
    p_dict = {
        'id': _id,
        'title': title,
        'kind': kind,
        'text': text,
        }

    condition = {'id': p_dict.pop('_id')}
    if condition['id']:
        BLog_.update(condition, **p_dict)
        return HttpResponse('OK')
    return HttpResponse('Something error')
