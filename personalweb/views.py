from django.shortcuts import render, get_object_or_404
from notes.models import Note, Tag
from projects.models import Project
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from personalweb.settings import DOMAIN


def home(request):
    notes = Note.objects.filter(status='published')[:5]
    tags = Tag.get_tags()
    projects = Project.objects.all()[:3]

    context = {
        'notes': notes,
        'tags': tags,
        'projects': projects,
    }
    return render(request,'uniques/index.html',context)


def robots(request):
    return render(request, "txts/robots.txt", context={'domain_url':DOMAIN}, content_type="text/plain")


def handler404(request, *args, **argv):
    return render(request, "errors/404.html", status=404)


def handler500(request, *args, **argv):
    return render(request, "errors/500.html", status=500)
