from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # path('foo/', views.foo, name='foo'),
    #
    # path('apply/', views.apply, name='new_presentation'),
    # path('new_presentation_a/', views.new_presentation_a, name='new_presentation_a'),
    # path('new_presentation_diff_formats/', views.new_presentation_diff_formats, name='new_presentation_diff_formats'),


    path('todogroups/', views.todo_groups, name='all_todo_groups'),
    path('groups_and_todos/', views.groups_and_todos, name='groups_and_todos'),
    path('todos_by_group/<int:todo_group_id>', views.todos_by_group, name='todos_by_group'),
    path('manage_group_of_todos/<int:todo_group_id>', views.manage_group_of_todos, name='manage_group_of_todos'),
    path('new_todo/<int:todo_group_id>', views.new_todo, name='new_todo'),
    path('create_todos/<int:todo_group_id>', views.create_todos, name='create_todos'),
    path('update_todos/<int:todo_group_id>', views.update_todos, name='update_todos'),

    # path('presentations_list_view/', views.presentations_list_view.as_view(), name='all_presentations_list_view'),
    #
    # path('presentation/<int:presentation_id>/', views.presentation, name="presentation"),
    # path('<int:pk>/presentation_detail_view/', views.presentation_detail_view.as_view(), name="presentation_detail_view"),
    #
    # path('protected_view/', views.protected_view, name='protected_view'),
    #
    #
    #
    # path('email/', views.email, name="email"),
]
