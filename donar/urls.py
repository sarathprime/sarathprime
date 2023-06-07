from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('donor_index/', views.donor_index),
    path('d_register/', views.d_register),
    path('d_login/', views.d_login),
    path('donate/', views.donate),
    path('view_reciptient_request/', views.view_reciptient_request),
    path('donor_purpose_form/', views.donor_purpose_form),
    path('donor_wallet/', views.donor_wallet),
    path('donor_current_wallet/', views.donor_current_wallet),
    path('donor_tax_pay/', views.donor_tax_pay),
    path('donor_send_reciptient/', views.donor_send_reciptient),
    path('donor_logout/', views.donor_logout),
    path('currency_converter/', views.currency_converter),
    path('donar_link_account/', views.donar_link_account),



]