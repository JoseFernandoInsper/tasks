from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post_task, name='post'),
    path('get/', views.get_tasks, name='get'),
    path('delete/', views.delete_tasks, name='delete'),
]
