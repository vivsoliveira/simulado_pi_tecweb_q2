from django.shortcuts import render, redirect
from .models import Note
from .models import Tag

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_name = request.POST.get('tag')
        tag_name = "#" + tag_name
        tag = Tag.objects.filter(name=tag_name)
        if len(tag) == 0:
            tag = Tag.objects.create(name=tag_name)
            tag.save()
        else:
            tag = tag[0]
        note = Note.objects.create(title=title, content=content, tag=tag)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')

def update(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note.title = title
        note.content = content
        note.save()
        return redirect('index')
    else:
        return render(request, 'notes/update.html', {'note': note})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'notes/list.html', {'tags': tags})

def tag_details(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    notes = Note.objects.filter(tag=tag)
    return render(request, 'notes/tag_details.html', {'notes': notes, 'tag': tag})
