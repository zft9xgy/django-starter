from django.shortcuts import render
from projects.models import Project

# Create your views here.

def projects(request):
    projects = Project.objects.all()

    context = {
        'title': 'Projects',
        'projects': projects,
    }
    return render(request,'uniques/projects.html',context)