"""
URL configuration for onlyflans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.base, name='base'),
    path('', views.indice, name='indice'),
    path('acerca/', views.acerca, name='acerca'),
    path('bienvenidos/', views.bienvenidos, name='bienvenidos'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/exito/', views.exito, name='contacto_exito'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.usuario_login, name='login'),
    path('logout/', views.usuario_logout, name='logout'),
    path('registro/', views.registro_view, name='registro'),
  
]
