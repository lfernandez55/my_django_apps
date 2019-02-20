from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskgroupList.as_view(), name='taskgroup_list'),
    path('taskgroup/add/', views.TaskgroupTaskCreate.as_view(), name='taskgroup_add'),
    path('taskgroup/<int:taskgroup_id>', views.TaskgroupTaskUpdate.as_view(), name='taskgroup_update'),
    # path('taskgroup/<int:taskgroup_id>/delete/', views.TaskgroupDelete.as_view(), name='taskgroup_delete'),
    path('taskgroup/<int:taskgroup_id>/delete/', views.TaskgroupDelete, name='taskgroup_delete'),
]


# urlpatterns = [
#     url(r'^$', views.ProfileList.as_view(), name='profile-list'),
#     url(r'profile/add/$', views.ProfileFamilyMemberCreate.as_view(), name='profile-add'),
#     url(r'profile/(?P<pk>[0-9]+)/$', views.ProfileFamilyMemberUpdate.as_view(), name='profile-update'),
#     url(r'profile/(?P<pk>[0-9]+)/delete/$', views.ProfileDelete.as_view(), name='profile-delete'),
# ]
