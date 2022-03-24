"""定义learning_logs的URL模式"""
from django.urls import path

from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的详情页面
    path('topics/<topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的网页
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    # 用于修改特定条目的网页
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]
