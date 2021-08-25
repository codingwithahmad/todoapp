from django.urls import path
from . import views
# Set Urls here

app_name = "todo"
urlpatterns = [
    path("", views.AllNote.as_view(), name="home"),
    path("create/", views.NoteCreate.as_view(), name="create"),
    path("update/", views.AllUpdate.as_view(), name="all_update"),
    path("update/<int:pk>", views.NoteUpdate.as_view(), name="update"),
    path("remove/", views.AllRemove.as_view(), name="all_remove"),
    path("remove/<int:pk>", views.NoteDelete.as_view(), name="remove"),
]