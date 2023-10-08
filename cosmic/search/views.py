from django.shortcuts import render
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

        context = {
            "projects": projects
        }
        return render(request, "search_res.html", context)
