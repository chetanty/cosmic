from django.urls import path, include
from . import views

app_name = "feed"

urlpatterns = [
    path("dashboard", views.dashboard_view, name="dashboard"),
    path("create_project", views.create_project_view, name="create_project"),
    path("project_post", views.project_post_view, name="project_post"),
    path("project_list", views.project_list_view, name="project_list"),
    path("project_contribution", views.project_contribution_view, name="project_contribution"),
    path("skills", views.skills_view, name="skills"),
    path("update_skills", views.update_skills_view, name="update_skills"),
    path("remove_proj", views.remove_proj_view, name="remove_proj"),
    path("update_project", views.update_project_view, name="update_project"),
    path("delete_project", views.delete_project_view, name="delete_project")
]