"""
URL configuration for password_manager_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from password_manager_app import views
from password_manager_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pass/', views.pass_view, name='pass_view'),
    path('password-list/', views.password_list, name='password_list'),
    path('', views.home_view, name='home_view'),  # Root URL
    # path('pass/', views.Password),
]
