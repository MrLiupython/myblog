from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path('', views.index_page, name='index'),
    path('list', views.list_page, name='list'),
    path('blog', views.blog_page, name='blog'),
    path('blog/edit', views.blog_edit, name='edit'),
    path('blog/update', views.blog_update, name='update'),
    path('blog/create', views.blog_create, name='create')
]
