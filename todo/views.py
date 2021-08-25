from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm
from django.urls import reverse, reverse_lazy

# Create your views here.

def index(request):
    return HttpResponse("Hello from todo app")


class NoteCreate(CreateView):
    model = Note
    template_name = "todo/create.html"
    form_class = NoteForm

    def get_success_url(self):
        return reverse('todo:home')


class AllNote(ListView):
    model = Note
    context_object_name = "notes"
    queryset = Note.objects.all()
    template_name = "todo/index.html"


class AllUpdate(ListView):
    model = Note
    context_object_name = "notes"
    queryset = Note.objects.all()
    template_name = "todo/all_update.html"


class AllRemove(ListView):
    model = Note
    context_object_name = "notes"
    queryset = Note.objects.all()
    template_name = "todo/all_r.html"

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy("todo:home")
    template_name = "todo/delete.html"

class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "todo/update.html"
    success_url = reverse_lazy("todo:home")