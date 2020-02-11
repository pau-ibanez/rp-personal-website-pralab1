from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all() # SQL SELECT * FROM Project;

    context = {
        'projects': projects
    }

    return render(request, 'project_list.html', context)
