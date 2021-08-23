from django.urls import path
from . import views
# Set Urls here

app_name = "todo"
urlpatterns = [
    path("", views.AllNote.as_view(), name="home"),
    path("create", views.NoteCreate.as_view(), name="create"),
]