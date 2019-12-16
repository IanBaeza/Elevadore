from django.contrib import admin
from django.urls import path
from . import views
from .views import inicio, crearcliente,listaclientes,crearorden,success

app_name="mantencion"
urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('inicio/',views.inicio,name='inicio'),
    path('panel/',views.panel,name='panel'),
    path('crearcliente/',views.crearcliente,name='crearcliente'),
    path('crearorden/',views.crearorden,name='crearorden'),
    path('listaclientes/',views.listaclientes,name='listaclientes'),
    path('success/', views.success, name='success'),
]