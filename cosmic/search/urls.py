from django.urls import path
from . import views
app_name = "search"

urlpatterns = [
    path("", views.search_view, name="search"),
    path("save_project", views.save_project_view, name="save_project")
]