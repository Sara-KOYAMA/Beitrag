from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_user, name='create'),
    path('login/', views.login, name='login'),
    path('error/', views.error, name='error'),
    path('message/', views.create_message, name='message'),
    path('list/', views.list, name='list'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('edit/<int:blog_id>/', views.edit, name='edit'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment')
]