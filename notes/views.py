from django.shortcuts import render, redirect
from .models import Note
from .models import Tag
from .models import Fact

def index(request, name='index.html'):
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
        return render(request, f'notes/{name}', {'notes': all_notes})

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

def fun_facts(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        fact = Fact.objects.create(descricao=descricao, curtidas=0)
        fact.save()
        return redirect('fun_facts')
    else:
        fun_facts = Fact.objects.all()
        all_facts = fun_facts.count()
        return render(request, 'notes/fun_facts.html', {'fun_facts': fun_facts, 'all_facts': all_facts})
    
def like_fact(request, id):
    fact = Fact.objects.get(id=id)
    fact.curtidas += 1
    fact.save()
    return redirect('fun_facts')
