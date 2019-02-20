"""conference URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
# from accounts import views as accounts_views
#from u2 import views
from . import views
from accounts import views as accounts_views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homeward'),
    path('u2/', include('u2.urls')),
    path('todo/', include('todo.urls')),
    path('task/', include('task.urls')),

    path('login_logout_resources/', views.login_logout_resources, name='login_logut_resources'),

    path('signup', accounts_views.signup, name='signup'),

    #this is called alternate because the auth module has a default logout route
    path('logout_alternate', auth_views.LogoutView.as_view(), name='logout_alternate'),

    # this is called login_alternate because the auth module provides a default login route that is
    # automatically associated with the template in registration/login.html
    path('login_alternate', auth_views.LoginView.as_view(template_name='registration/login_alternate.html'), name='login_alternate'),
    #the following automatically serve various auth related url urlpatterns
    # see https://docs.djangoproject.com/en/2.1/topics/auth/default/#module-django.contrib.auth.views
    #including login, logout, password_change, password_reset.  the only one it doesn't do is signup
    path('accounts/', include('django.contrib.auth.urls')),

    # I'm overriding password_change because it brings up an admin interface that is cosmetically wrong
    path('password_change_alternate', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change_alternate'),
    # path('password_change_done_alternate', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    #     name='password_change_done_alternate'),
    # path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    # name='password_change_done_alternate'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
        name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
        name='password_change_done'),

    path('warning/', views.warning, name="warning"),




    # path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='accounts_login'),






]
