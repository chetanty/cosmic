from django.shortcuts import render, redirect
from feed.models import Project
from users.models import CustomUser
from django.db.models import Q

# Create your views here.
def search_view(request):
    if request.method == "GET":
        search_param = request.GET["search"]

        if request.user.is_developer:
            usernames = CustomUser.objects.filter(Q(username__icontains = search_param))
            context = {
                    "usernames": usernames
                }
            return render(request, "search_res.html", context)
    
        projects = Project.objects.filter(
                Q(proj_name__icontains = search_param) |
                Q(proj_desc__icontains = search_param) |
                Q(requirements__icontains = search_param) |
                Q(proj_links__icontains = search_param)
        )
        cleaned_projects = []
        for project in projects:
            if not request.user.savedproject_set.filter(saved_proj_id = project.id):
                cleaned_projects.append(project)
                
        context = {
            "projects": cleaned_projects
        }
        return render(request, "search_res.html", context)

def save_project_view(request):
    if request.method == "POST":
        request.user.savedproject_set.create(saved_proj_id=int(request.POST["pid"]))

        return redirect("feed:dashboard")