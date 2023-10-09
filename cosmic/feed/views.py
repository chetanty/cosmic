from django.shortcuts import render, redirect
from .models import Project, SavedProject

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
    proj_contributes = request.user.savedproject_set.all()
    projs = []

    for proj in proj_contributes:
        projs.extend(Project.objects.filter(pk=proj.saved_proj_id))
    
    context = {
        "projs": projs
    }
    return render(request, "project_contribution.html", context)

def skills_view(request):
    try:
        context = {
            "user_skills": request.user.skillset_set.all()[0]
        }
    except Exception:
        context = {
            "user_skills": ""
        }
    return render(request, "skills.html", context)

def update_skills_view(request):
    if request.method == "POST":
        request.user.skillset_set.update_or_create(defaults={"skill_text":request.POST["skills"]})
        return redirect("feed:skills")

def remove_proj_view(request):
    if request.method == "POST":
        saved_proj = SavedProject.objects.filter(saved_proj_id=int(request.POST["pid"]), saved_id=request.user)
        saved_proj.delete()
        return redirect("feed:dashboard")
    
def update_project_view(request):
    if request.method == "POST":
        Project.objects.filter(id=request.POST["pid"], proj_id=request.user).update(
            proj_name=request.POST["name"],
            proj_desc=request.POST["description"],
            requirements=request.POST["requirements"],
            proj_links=request.POST["project_links"],
        )
    return redirect("feed:project_list")

def delete_project_view(request):
    if request.method == "POST":
        Project.objects.filter(id=request.POST["pid"], proj_id=request.user).delete()
    return redirect("feed:project_list")