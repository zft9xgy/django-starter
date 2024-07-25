from django.shortcuts import render,redirect, get_object_or_404
from notes.models import Note
from django.http import HttpResponse

# Create your views here.


def notes(request):

    if request.user.is_staff:
        notes = Note.objects.all()
    else:
        notes = Note.objects.filter(status='published')
        
    years ={ note.created_date.year for note in notes }
    years = sorted(years,reverse=True)
    print(years)

    context = {
        'title': 'Notes',
        'notes': notes,
        'years': years,
    }
    return render(request,'uniques/notes.html',context)


def note(request,slug):

    note = get_object_or_404(Note,slug=slug)

    if note.status == 'draft' and not request.user.is_staff:
        return redirect('home')

    context = {
        'title': note.title,
        'note':note,
    }  

    try:
        if note.seo:
            context['seometa'] = note.seo
    except Note.seo.RelatedObjectDoesNotExist:
        pass

    return render(request,'generic/single-note.html',context)
