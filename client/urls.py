from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('c_register/', views.c_register),
    path('c_index/', views.c_index),
    path('c_login/', views.c_login),
    path('C_logout/', views.C_logout),
    path('purpose_form/', views.purpose_form),
    path('walletid/', views.walletid),
    path('reciptient_Wallet/', views.reciptient_Wallet),
    path('link_account_details/', views.link_account_details),
    path('upload_requirement/', views.upload_requirement),
    path('currency_converter/', views.currency_converter),

]