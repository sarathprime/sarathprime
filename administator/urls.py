from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin_login/', views.admin_login),
    path('a_index/', views.a_index),
    path('set_currency/', views.set_currency),
    path('A_logout/', views.A_logout),
    path('view_reciptient/', views.view_reciptient),
    path('id_generator/', views.id_generator),
    path('r_id/', views.r_id),
    path('r_send/', views.r_send),
    path('ae_mail/<int:id>/', views.ae_mail),
    path('view_donor/', views.view_donor),
    path('view_donor/', views.view_donor),
    path('generate_donor/', views.generate_donor),
    path('d_send/', views.d_send),
    path('view_autenticator/', views.view_autenticator),
    path('re_mail/<int:id>/', views.re_mail),
    path('de_mail/<int:id>/', views.de_mail),

]