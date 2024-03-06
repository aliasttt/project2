from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,),
    path('ali',views.ali,),
    path('<str:name>',views.name)
] 