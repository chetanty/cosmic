from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("logout", views.logout_view, name="logout")
]