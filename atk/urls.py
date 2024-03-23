from django.urls import path
from . import views

urlpatterns = [
    path('submit_atk_result/', views.submit_atk_result, name='submit_atk_result'),
    path('success/', views.success, name='success'),
]