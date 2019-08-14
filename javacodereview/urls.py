from django.urls import path
from . import views

urlpatterns = [
    path('codeupload/', views.upload_code, name='codeupload'),
    path('findings/', views.findings, name='findings'),
    path('', views.home, name = 'home')
]
