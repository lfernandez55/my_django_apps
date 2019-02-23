from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskgroupList.as_view(), name='taskgroup_list'),
    path('taskgroup/add/', views.TaskgroupTaskCreate.as_view(), name='taskgroup_add'),
    path('taskgroup/<int:pk>/', views.TaskgroupTaskUpdate.as_view(), name='taskgroup_update'),
    path('taskgroup/<int:pk>/delete/', views.TaskgroupDelete.as_view(), name='taskgroup_delete'),
    path('foo/', views.foo, name='foo'),
    # path('foo/',views.Foo.as_view(), name='foo'),
]
