from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('export_pdf/', views.export_pdf, name='export_pdf'),
]
