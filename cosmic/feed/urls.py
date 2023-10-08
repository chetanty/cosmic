from django.urls import path, include
from . import views

app_name = "feed"

urlpatterns = [
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("create_project", views.create_project_view, name="create_project"),
    path("project_post", views.project_post_view, name="project_post"),
    path("project_list", views.project_list_view, name="project_list"),
    path("project_contribution", views.project_contribution_view, name="project_contribution")
]