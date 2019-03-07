from django.urls import path

from . import views

urlpatterns = [
    path('', views.choregroupList, name='choregroup_list'),
    path('choregroup/add/', views.choregroupCreate, name='choregroup_create'),
    path('choregroup/<int:pk>/', views.choregroupUpdate, name='choregroup_update'),
    path('choregroup/<int:pk>/delete/', views.choregroupDelete, name='choregroup_delete'),
]
