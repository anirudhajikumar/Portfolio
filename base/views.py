from django.shortcuts import render
from .models import Skill, Project, Experience
from django.db import models


# Create your views here.
def home(request):
    skills = Skill.objects.all()
    experience = Experience.objects.all()
    q = request.GET.get('q', '')  # clean and safe

    projects = Project.objects.all()

    if q:
        projects = projects.filter(
            skills__name__iexact=q
        ).distinct()


    images = list(range(1, 22))  # 1 to 21

    context = {
        'skills': skills,
        'projects': projects,
        'images': images,  
        'experience':experience,
    }
    return render(request, "index.html", context)
