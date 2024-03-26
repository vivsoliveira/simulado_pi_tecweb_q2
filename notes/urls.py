from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:note_id>/', views.delete, name='delete'),
    path('update/<int:note_id>/', views.update, name='update'),
    path('tags/', views.tag_list, name='list'),
    path('tags/<int:tag_id>/', views.tag_details, name='tag_details'),
    path('fun_facts/', views.fun_facts, name='fun_facts'),
]