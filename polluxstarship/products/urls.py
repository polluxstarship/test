from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:my_id>/', product_detail_view, name='product-detail'), #모델의 동적 url 사용하기 위해 이름붙임
    path('create/', product_create_view),
    path('delete/<int:my_id>/', product_delete_view, name='product-delete'),
    path('edit/<int:my_id>/', product_edit_view, name='product-edit'),
    path('', product_list_view),
    ]