from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from pages.models import Page


# Create your views here.


def page(request,slug):

    page = get_object_or_404(Page,slug=slug)

    context = {
        'title':page.title,
        'page':page,
    }
    return render(request,'generic/single-page.html',context)
