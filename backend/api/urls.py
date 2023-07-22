from django.urls import path

from . import views

urlpatterns = [

    path('1/', views.api_home),
]