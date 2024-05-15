from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home-page"),
    path('getstarted/', views.getstarted, name="get-started-page"),


]