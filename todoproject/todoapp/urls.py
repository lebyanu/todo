
from django.contrib import admin
from django.urls import path, include
from . import views
from todoapp import views

urlpatterns = [

    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/' ,views.todo_listview.as_view(),name='cbvhome'),
    path('cbdhome/<int:pk>/',views.todo_detailview.as_view(), name='cbdhome'),
    path('cbuhome/<int:pk>/',views.todo_upadateview.as_view(),name='cbuhome'),
    path('cbvdelete/<int:pk>/',views.todo_delete.as_view(),name='cbvdelete'),
]