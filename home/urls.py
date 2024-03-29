from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('contact/',views.contact,name="contact"),
    path('search/',views.search,name="search"),
    path('about/',views.about,name="about"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.handlelogin,name="login"),
    path('logout/',views.handlelogout,name="logout"),
]