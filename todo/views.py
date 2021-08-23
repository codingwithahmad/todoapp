from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import Note
from .forms import NoteForm

# Create your views here.

def index(request):
    return HttpResponse("Hello from todo app")


class NoteCreate(CreateView):
    model = Note
    template_name = "todo/create.html"
    form_class = NoteForm

