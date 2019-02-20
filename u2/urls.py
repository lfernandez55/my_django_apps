from django.urls import path

from . import views

app_name = 'u2'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('foo/', views.foo, name='foo'),

    path('apply/', views.apply, name='new_presentation'),
    path('new_presentation_a/', views.new_presentation_a, name='new_presentation_a'),
    path('new_presentation_diff_formats/', views.new_presentation_diff_formats, name='new_presentation_diff_formats'),


    path('presentations/', views.presentations, name='all_presentations'),
    path('presentations_list_view/', views.presentations_list_view.as_view(), name='all_presentations_list_view'),

    path('presentation/<int:presentation_id>/', views.presentation, name="presentation"),
    path('<int:pk>/presentation_detail_view/', views.presentation_detail_view.as_view(), name="presentation_detail_view"),

    path('protected_view/', views.protected_view, name='protected_view'),



    path('email/', views.email, name="email"),
]
