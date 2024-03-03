from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('back_login', views.back_login, name='back_login'),

]