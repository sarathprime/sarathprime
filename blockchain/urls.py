from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('b_index/', views.b_index),
    path('b_login/', views.b_login),
    path('B_register/', views.B_register),
    path('view_transaction_b/', views.view_transaction),
    path('view_hashed/', views.view_hashed),
    path('block_logout/', views.block_logout),
    path('encryption_data/', views.encryption_data),
    path('encryption/', views.encryption),
    path('view_encrypted/', views.view_encrypted),
    path('enc/<int:id>/', views.enc),
    path('hash/<int:id>/', views.hash),
    # path('approve_)



]