"""
URL configuration for taskmate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from todolist_app import views as todolistapp_views

urlpatterns = [
    path('', todolistapp_views.index, name="index"),
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact', todolistapp_views.contact, name="contact"),
    path('about', todolistapp_views.about, name="about"),
]
