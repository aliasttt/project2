
from django.urls import path 
from . import views


urlpatterns = [
    path('ali',views.ali),
    path("<str>",views.yourname),
    path('',views.welcome),
    path("home",views.home),
    path("gholi",views.gholi)
]
