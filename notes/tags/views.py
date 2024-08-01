from django.shortcuts import render, get_object_or_404
from notes.models import Note, Tag
from projects.models import Project



def tags(request):
    tags = Tag.get_tags()

    context = {
        'title':'Tags',
        'tags': tags,
    }
    return render(request,'uniques/tags.html',context)

def tag(request,slug):
    tag = get_object_or_404(Tag,slug=slug)
    tags = Tag.get_tags().exclude(id=tag.id)

    context = {
        'title':tag.name,
        'tag': tag,
        'tags':tags
    }
    return render(request,'generic/single-tag.html',context)
