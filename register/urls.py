from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('regi', views.regi, name="regi"),
    path('login_page', views.login_page, name="login_page"),
    path('logout_page', views.logout_page, name="logout_page"),
]
