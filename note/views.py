from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import NoteForm
from .models import Note
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def notes(request):
    keyword = request.GET.get("keyword")
    if keyword:
        notes = Note.objects.filter(title__contains = keyword)
        return render(request, "notes.html", {"notes" : notes})
    notes = Note.objects.filter(author = request.user)
    return render(request, "notes.html", {"notes" : notes})

def index(request):
    return render(request,"index.html")

@login_required(login_url = "user:login")
def mynotes(request):
    notes = Note.objects.filter(author = request.user)
    context = {
        "notes" : notes
    }
    return render(request, "mynotes.html", context)

@login_required(login_url = "user:login")
def addnote(request):
    form = NoteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        note = form.save(commit = False)
        note.author = request.user
        note.save()
        messages.success(request, "Not başarıyla eklendi.")
        return redirect("note:mynotes")

    context = {
        "form" : form
    }
    return render(request, "addnote.html", context)

@login_required(login_url = "user:login")
def detail(request, id):
    note = get_object_or_404(Note, id = id)
    return render(request, "detail.html", {"note":note})

@login_required(login_url = "user:login")
def updateNote(request, id):
    note = get_object_or_404(Note, id = id)
    form = NoteForm(request.POST or None or request.FILES or None, instance = note)
    if form.is_valid():
        note = form.save(commit = False)
        note.author = request.user
        note.save()
        messages.success(request, "Not başarıyla güncellendi.")
        return redirect("note:mynotes")
    return render(request, "update.html", {"form" : form})

@login_required(login_url = "user:login")
def deleteNote(request, id):
    note = get_object_or_404(Note, id = id)
    note.delete()
    messages.success(request, "Not başarıyla silindi.")
    return redirect("note:mynotes")
