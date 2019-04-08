# -*- coding: utf-8 -*-

from django.shortcuts import render
from .index import Index
from .blog import Blog
from markdown import markdown


def  index_page(request):
    indexs = Index.all()
    return render(
        request, 
        'myblog/index.html',
        {'indexs': indexs}
        )


def list_page(request):
      if request.method == 'GET':
         kind = request.GET.get('kind')
         index_object = index.filter({'kind': kind})
         blogs = index_object.blog_set.all()
         return render(
             request,
             'myblog/list.html',
             {'blogs': blogs}
             )


def blog_page(request):
    blog_id = request.GET.get('_id')
    if not blog_id:
        return 'nothing'
    blog = Blog.get(id=blog_id)
    text = markdown(blog.text.text)
    return render(
        request,
        'myblog/blog.html',
        {'blog': blog, 'text': text}
        )


def blog_edit(request):
    blog_id = request.GET.get('_id')
    if blog_id:
        blog = Blog.get(id=blog_id)
        text = markdown(blog.text.text)
    else:
        blog = None
        text = None
    return render(
        request,
        'myblog/edit.html',
        {'blog': blog, 'text': text}
        )

