from django.shortcuts import render, redirect
from .models import Project

# Create your views here.
def dashboard_view(request):
    if request.user.is_authenticated:
        context = {
            "user": request.user
        }
        return render(request, "dashboard.html", context)
    else:
        return redirect("users:index")
    
def create_project_view(request):
    return render(request, "create_project.html")

def project_post_view(request):
    if request.method == "POST":
        data = request.user.project_set.create(
            proj_name = request.POST["name"],
            proj_desc = request.POST["description"],
            requirements = request.POST["requirements"],
            proj_links = request.POST["project_links"],
        )
        data.save()
        return redirect("feed:dashboard")
    
def project_list_view(request):
    data = Project.objects.filter(proj_id=request.user.id)
    context = {
        "data": data
    }
    return render(request, "project_list.html", context)

def project_contribution_view(request):
    return render(request, "project_contributions.html")