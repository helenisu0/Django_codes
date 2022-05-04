import re
from django.shortcuts import render

import projects
from projects.models import Project
from .forms import ProjectForm

def hello_world(request):
  
    # print(request, "===")
    data = request.POST
    form = ProjectForm(data=data)
    print (data, "===data===")

    if request.method =="POST":
        form = ProjectForm(data=data)
        if form.is_valid() and data.get("technology") != "person":
            form.save()
            form = ProjectForm()
        else:
            print("This object will not save")
            print("The technology should not be person")
            print(form.errors)

    return render(request, 'hello_world.html', {"form":form})

def get_Project(request):
    projects = Project.objects.all()
    return render(request, "list_html", {"projects":projects})

def filter_projects(request):
    data = request.POST
    key = data.get('filter')
    if key is not None:
        projects= Project.objects.filter(title__contains=key)
    else:
        projects={}
    return render(request, "filtered_projects.html", {'projects':projects})
