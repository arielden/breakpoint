from django.urls import path
from . import views

app_name = 'app_reserva'

urlpatterns = [
    path("reserva/", views.reservaPage, name="reserva"),
    path("login/", views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]