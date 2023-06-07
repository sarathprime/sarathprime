from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('t_register/', views.t_register),
    path('t_login/', views.t_login),
    path('t_index/', views.t_index),
    path('table/', views.table),
    path('approve_project/<int:id>/', views.approve_project),
    path('tableaccept/<int:id>/', views.tableaccept),
    path('donor_accept/<int:id>/', views.donor_accept),
    path('transaction_update/<int:id>/', views.transaction_update),
    path('c_walletid/', views.c_walletid),
    path('access_Wallet/', views.access_Wallet),
    path('tech_Wallet/', views.tech_Wallet),
    path('view_donor_technical/', views.view_donor),
    path('technical_logout/', views.technical_logout),
    path('view_transaction/', views.view_transaction),
    path('analysing/', views.analysing),
    path('view_transaction1/', views.view_transaction1),



]