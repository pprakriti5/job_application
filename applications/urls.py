from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_form, name='application_form'),
    path('success/', views.success, name='success'),
]