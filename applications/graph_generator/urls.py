from django.urls import path
from applications.graph_generator import views

urlpatterns = [
    path('graph1', views.home, name="home"),
]
