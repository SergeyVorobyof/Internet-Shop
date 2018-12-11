from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    #path('register/', views.register, name = 'register'),
    path('customer/new/', views.create_customer, name='create_customer'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('customer/<pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customer/<pk>/order/', views.add_order_to_customer, name='add_order_to_customer'),
    ####
    path('good/new/', views.good_create, name='good_create'),
    path('good/<int:pk>/', views.good_detail, name='good_detail'),
    path('good_list/', views.good_list, name='good_list'),
    path('customer/<pk>/order', views.good_buy, name = 'good_buy'),
    path('bucket/', views.bucket, name='bucket'),
    path('customer/<pk>/checked_and_delivered/', views.checked_and_delivered, name='checked_and_delivered'),
]