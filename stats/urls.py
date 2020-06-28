from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('maharashtra/', views.maharashtra, name="MH")
]
